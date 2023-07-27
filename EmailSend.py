Solution:-import smtplib           # Import the 'smtplib' library for sending emails
import ssl               # Import the 'ssl' library for creating a secure SSL context
from email.message import EmailMessage  # Import 'EmailMessage' class from the 'email.message' module

# Define email-related variables
email_sender = ''
email_password = ''           # Sender's email password or app password
email_receiver = ['','','', ]         # Recipient's email address

subject = 'this is a python task  '   # Subject of the email
body = """
    I have completed python task successfully again.
"""                                                # Body of the email (multi-line string)

# Create an EmailMessage object to construct the email
em = EmailMessage()
em['From'] = email_sender              # Set the sender's email address
em['To'] = email_receiver              # Set the recipient's email address
em['Subject'] = subject                # Set the subject of the email
em.set_content(body)                   # Set the email body
    
# Create an SSL context for secure communication with the SMTP server
context = ssl.create_default_context()

# Connect to the Gmail SMTP server using SSL and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)      # Log in to the sender's Gmail account
    smtp.sendmail(email_sender, email_receiver, em.as_string())  # Send the email
