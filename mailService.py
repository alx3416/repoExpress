import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = 'javiergtzmoras1@gmail.com'
toaddrs = 'jegmorales876@gmail.com'
subject = 'Test Message, Hello Javier'
body = 'Hello, this is a test message'

# Credentials
username = 'javiergtzmoras1@gmail.com'
password = 'zujfoxbgelghokql'  # Use an App Password generated from your Google account

# Create the message
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddrs
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# The actual mail send
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")
