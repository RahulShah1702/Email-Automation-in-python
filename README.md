# Email Automation Tool with Scheduling

This project provides a Python-based graphical user interface (GUI) application for automating the sending of emails. It includes features such as scheduling emails for a specific date and time (including seconds), attaching files, and detailed instructions for setting up Gmail app passwords.

# Features

1. Send Emails Instantly: Send emails to any recipient with a simple interface.

2. Scheduled Emails: Schedule emails to be sent at a specific date and time.

3. File Attachments: Attach files to your emails easily.

4. Secure Gmail Integration: Uses Gmail’s app passwords for secure email authentication.

5. Intuitive GUI: User-friendly design with scrollable instructions for ease of use.

6. Mouse Scroll Support: Navigate through the instructions using the mouse wheel or buttons.

# How to Use

## Prerequisites

1. Python: Make sure Python 3.11 is installed on your system. Download Python

2. Required Libraries: Install the required libraries using the following command:

pip install tk

## Setting Up the Application

1.Clone this repository or download the source code.

2. Open a terminal/command prompt and navigate to the directory containing the script.

3. Run the script using:

python email_automation.py

## GUI Instructions

1. Sender Email: Enter the Gmail address you will use to send the email.

2. Sender Password: Enter the 16-character app password generated from your Gmail account (see below for setup).

3. Receiver Email: Enter the recipient’s email address.

4. Subject: Enter the subject line of the email.

5. Body: Write the email content in the text area.

6. Attachment (Optional): Click "Browse" to select a file to attach.

7. Date: Enter the scheduled date in the format YYYY-MM-DD. Leave blank to send instantly.

8. Time: Enter the scheduled time in the format HH:MM:SS. Leave blank to send instantly.

9. Send Email: Click the "Send Email" button to either send or schedule the email.

# Steps to Generate a Gmail App Password

1. Enable 2-Step Verification:

Go to your Google Account Settings.

Navigate to the Security tab.

Enable 2-Step Verification if it’s not already enabled.

2. Generate an App Password:

Go to Security > App Passwords.

Select "Mail" as the app and "Windows Computer" as the device.

Click Generate and copy the 16-character app password.

3. Use the App Password:

Enter this app password in the "Sender Password" field in the application.

# Screenshots

1. Main Interface:
Displays fields for email, password, receiver details, subject, body, attachments, and scheduling options.

2. Scrollable Instructions:
A detailed instructions panel for step-by-step guidance.

# Troubleshooting

FileNotFoundError:
Ensure the file path for the attachment is correct.

Authentication Error:

Verify your app password.

Ensure 2-Step Verification is enabled in your Gmail account.

Scheduling Error:
Ensure the date and time format is correct and in the future.

# Code Overview

## Main Components

## 1. send_email():

Handles the email composition and sending logic.

Includes error handling for file attachments and SMTP issues.

## 2 .schedule_email():

Handles email scheduling using Python’s datetime and threading.Timer modules.

Validates scheduling time and sends emails immediately if no date/time is provided.

## 3. GUI:

Built using tkinter.

Includes input fields, buttons, and a scrollable instruction section for user guidance.

## Future Enhancements

Add support for multiple email providers (e.g., Yahoo, Outlook).

Add functionality to send emails to multiple recipients.

Enhance UI with more themes and dynamic layouts.

Add logging for sent and scheduled emails.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

## Acknowledgments

Special thanks to the open-source community for making tools and resources available to developers around the world.

