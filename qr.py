import csv
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def generate_qr_code(data, image_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(image_path)

def send_email(sender_email, sender_password, receiver_email, subject, message, image_paths):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the text message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Attach images to the email
    for image_path in image_paths:
        with open(image_path, 'rb') as f:
            img_data = f.read()
        
        image = MIMEImage(img_data, name=image_path)
        msg.attach(image)

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the sender's email account
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)

    # Disconnect from the SMTP server
    server.quit()

# Example usage
sender_email = "codehopper123@gmail.com"
sender_password = "gxvkelgklylekxfm"
subject = "message from COHO"
message = "Hello, Thank ou for participating in coho!"

# Read data and email addresses from CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        data = f"s.no-{row[0]} name-{row[1]}"
        receiver_email = row[4]
        image_path = f"qrcode_{data}.png"

        # Generate QR code image
        generate_qr_code(data, image_path)

        # Send email with QR code attachment
        send_email(sender_email, sender_password, receiver_email, subject, message, [image_path])
