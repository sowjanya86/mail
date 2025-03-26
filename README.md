# OTP Email Verification Script
This is a Python script that sends an OTP (One Time Password) for email verification. It sends a random 4-digit OTP to a list of emails and asks the user to input the received OTP for verification.

Features:

Send OTP via Email: The script generates a random OTP and sends it to multiple email addresses.
SMTP Protocol: Utilizes the SMTP protocol to send emails through Gmail’s SMTP server.
OTP Validation: After sending the OTP, the script prompts the user to input the received OTP for validation.
Error Handling: Ensures OTPs are checked correctly and displays an appropriate message if the OTP doesn't match.
 
Prerequisites:

Before running the script, make sure you have the following:
Python 3.x installed on your system.
The smtplib and email.mime libraries, which are part of Python's standard library.
A Gmail account and an app password (if using two-factor authentication) for the sender email.
Setting Up Gmail for SMTP
If you're using a Gmail account, ensure you have enabled "Less secure apps" or use an "App Password" for a more secure method (recommended).
Enable "Less Secure Apps": Google less secure apps link
Using App Passwords: Google App Passwords

Installation:

Clone this repository to your local machine:
git clone https://github.com/yourusername/otp-email-verification.git
Navigate to the directory:
cd otp-email-verification
Ensure you have an active internet connection.
Usage
Modify the mails list with the email addresses you want to send OTPs to.
Update the server.login() method with your Gmail credentials. If using 2FA, use an App Password.
Run the script:
python otp_email_verification.py
The script will send OTPs to the emails and prompt you to enter the OTP you received for validation.
Upon entering the correct OTP, you will get a success message. Otherwise, it will notify you of an invalid OTP.
 
Example Output:
yaml
Copy
OTP for Verification is 1234
Enter OTP Received: 1234
OTP Verification Success
Code Explanation
Imports: The script imports necessary modules like smtplib for email sending, random for OTP generation, and email.mime for crafting email messages.
Email Setup: The email server (Gmail SMTP) is set up, and login credentials are used to send the email.
OTP Generation: A random 4-digit OTP is generated for each recipient.
User Input for OTP: After sending the email, the script waits for the user to input the OTP received.
Validation: The inputted OTP is compared to the sent OTP, and a success or failure message is displayed.
Example
python
Copy
mails = ["example1@example.com", "example2@example.com"]
for i in mails:
    otp = random.randint(1111, 9999)
    # Send OTP to each email
    # OTP validation happens after sending
 
Contributing:

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions, issues, and suggestions are welcome.
License
This project is open-source and available under the MIT License. See the LICENSE file for more details.
