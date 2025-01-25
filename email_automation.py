import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import Tk, Label, Entry, Button, filedialog, Text, END, messagebox, Frame, Scrollbar, VERTICAL, Canvas
from datetime import datetime
from threading import Timer


def send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port, attachment=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment:
        filename = attachment.split("/")[-1]
        try:
            with open(attachment, "rb") as attachment_file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment_file.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition", f"attachment; filename= {filename}"
                )
                msg.attach(part)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Attachment file not found: {attachment}")
            return

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error sending email: {e}")


def schedule_email():
    try:
        sender_email = sender_email_entry.get()
        sender_password = sender_password_entry.get()
        receiver_email = receiver_email_entry.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", END).strip()
        attachment = attachment_entry.get()
        date = date_entry.get()
        time = time_entry.get()

        if not sender_email or not sender_password or not receiver_email or not subject or not body:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        if date and time:
            scheduled_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
            delay = (scheduled_time - datetime.now()).total_seconds()
            if delay <= 0:
                messagebox.showerror("Error", "Scheduled time must be in the future.")
                return

            Timer(delay, send_email, args=(sender_email, sender_password, receiver_email, subject, body, "smtp.gmail.com", 587, attachment)).start()
            messagebox.showinfo("Scheduled", f"Email scheduled for {scheduled_time}.")
        else:
            send_email(sender_email, sender_password, receiver_email, subject, body, "smtp.gmail.com", 587, attachment)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def browse_file():
    filename = filedialog.askopenfilename(title="Select a File")
    if filename:
        attachment_entry.delete(0, END)
        attachment_entry.insert(0, filename)


# GUI Setup
root = Tk()
root.title("Email Automation Tool with Scheduling")
root.geometry("750x850")
root.config(bg="#2C3E50")

# Header Frame
header_frame = Frame(root, bg="#34495E", pady=20)
header_frame.pack(fill="x")
Label(header_frame, text="Email Automation Tool with Scheduling", font=("Arial", 18, "bold"), bg="#34495E", fg="white").pack()

# Main Frame
main_frame = Frame(root, bg="#ECF0F1", padx=20, pady=20)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Sender Email
Label(main_frame, text="Sender Email:", font=("Arial", 12), bg="#ECF0F1", anchor="w").grid(row=0, column=0, sticky="w", pady=10)
sender_email_entry = Entry(main_frame, width=40, font=("Arial", 12))
sender_email_entry.grid(row=0, column=1)

# Sender Password
Label(main_frame, text="Sender Password (App Password):", font=("Arial", 12), bg="#ECF0F1", anchor="w").grid(row=1, column=0, sticky="w", pady=10)
sender_password_entry = Entry(main_frame, width=40, font=("Arial", 12), show="*")
sender_password_entry.grid(row=1, column=1)

# Receiver Email
Label(main_frame, text="Receiver Email:", font=("Arial", 12), bg="#ECF0F1", anchor="w").grid(row=2, column=0, sticky="w", pady=10)
receiver_email_entry = Entry(main_frame, width=40, font=("Arial", 12))
receiver_email_entry.grid(row=2, column=1)

# Subject
Label(main_frame, text="Subject:", font=("Arial", 12), bg="#ECF0F1", anchor="w").grid(row=3, column=0, sticky="w", pady=10)
subject_entry = Entry(main_frame, width=40, font=("Arial", 12))
subject_entry.grid(row=3, column=1)

# Body
Label(main_frame, text="Body:", font=("Arial", 12), bg="#ECF0F1", anchor="w").grid(row=4, column=0, sticky="nw", pady=10)
body_text = Text(main_frame, width=40, height=5, font=("Arial", 12))
body_text.grid(row=4, column=1)

# Attachment
Label(main_frame, text="Attachment (optional):", font=("Arial", 12), bg="#ECF0F1", anchor="w").grid(row=5, column=0, sticky="w", pady=10)
attachment_entry = Entry(main_frame, width=40, font=("Arial", 12))
attachment_entry.grid(row=5, column=1)
Button(main_frame, text="Browse", command=browse_file, bg="#2980B9", fg="white").grid(row=5, column=2, padx=5)

# Date
Label(main_frame, text="Date (YYYY-MM-DD):", font=("Arial", 12), bg="#ECF0F1", anchor="w").grid(row=6, column=0, sticky="w", pady=10)
date_entry = Entry(main_frame, width=40, font=("Arial", 12))
date_entry.grid(row=6, column=1)

# Time
Label(main_frame, text="Time (HH:MM:SS):", font=("Arial", 12), bg="#ECF0F1", anchor="w").grid(row=7, column=0, sticky="w", pady=10)
time_entry = Entry(main_frame, width=40, font=("Arial", 12))
time_entry.grid(row=7, column=1)

# Send Button
Button(root, text="Send Email", command=schedule_email, bg="#27AE60", fg="white", font=("Arial", 14)).pack(pady=10)


instructions_frame = Frame(root, bg="#ECF0F1")
instructions_frame.pack(fill="both", expand=True, padx=20, pady=10)

canvas = Canvas(instructions_frame, bg="#ECF0F1")
scrollbar = Scrollbar(instructions_frame, orient=VERTICAL, command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#ECF0F1")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

instructions_label = Label(scrollable_frame, text="Steps to Use and Obtain App Password:", font=("Arial", 14, "bold"), bg="#ECF0F1")
instructions_label.pack(anchor="w", pady=10)

instructions_text = Label(scrollable_frame, text="""
1. Enable 2-Step Verification on your Gmail account:
   - Go to Google Account Settings.
   - Under 'Security', enable '2-Step Verification'.

2. Generate an App Password:
   - Go to 'Google Account Settings > Security > App Passwords'.
   - Select 'Mail' as the app and 'Windows Computer' as the device.
   - Click 'Generate' and copy the 16-character app password.

3. Use the App Password:
   - Enter the app password in the 'Sender Password' field in this tool.

4. Scheduling:
   - If you provide a valid date and time (including seconds), the email will be sent at the scheduled time.
   - If left blank, the email will be sent immediately.
""", font=("Arial", 12), bg="#ECF0F1", justify="left", anchor="nw")
instructions_text.pack(anchor="w", pady=10)

root.mainloop()
