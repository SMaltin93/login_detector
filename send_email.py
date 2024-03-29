import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Import MIMEText
from email.mime.image import MIMEImage



def read_photo():
    # Try to capture a screenshot
    try: 
        with open("Screenshot_0.png", "rb") as photo_file:
            img = MIMEImage(photo_file.read())
            return img  
    except FileNotFoundError:
        print("File not found")
        return None
    
def send_email(img):
    # Set the sender and recipient email addresses
    sen_email = "from@gmail.com"
    rec_email = "to@gmail.com"
    password = "xxxx xxxx xxxx xxxx"
    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sen_email
    msg["To"] = rec_email
    msg["Subject"] = "Security Alert"
    msg_body = f"Someone has accessed your computer at {datetime.datetime.now()}\n"
    # Attach the photo
    if img:
        msg.attach(img)
        msg_body += "A photo has been taken."
    else:
        msg_body += "No photo has been taken."
    # Attach the text body
    text_part = MIMEText(msg_body, 'plain')
    msg.attach(text_part)
        # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(sen_email, password)
        server.sendmail(sen_email, rec_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error: {e}")




