import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Debugging information
        print("Attempting to connect to SMTP server...")

        # Use SSL instead of STARTTLS for better reliability
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.set_debuglevel(1)  # Enable debugging
            server.login(sender_email, sender_password)  # Login to your email
            print("Login successful!")
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email
            print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Usage example
sender_email = "sridhard.21cse@kongu.edu"
sender_password = "mkjm cesf oksw hvck"  # App-specific password
recipient_email = "sridhard.21cse@kongu.edu"
subject = "Test Email"
body = "This is a test email sent using Python!"

send_email(sender_email, sender_password, recipient_email, subject, body)
