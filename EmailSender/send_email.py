import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials


def create_image_attachment(path: str) -> MIMEImage:
    # raise NotImplementedError("Code not implemented")

    with open(path, "rb") as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f"attachment; filename={path}")
        return mime_image


def send_email(to_email: str, subject: str, body: str, image: str | None):
    host: str = 'smtp-mail.outlook.com'
    port: int = 587

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with smtplib.SMTP(host, port) as server:
        print("Logging in...")
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(credentials.EMAIL, credentials.PASSWORD)

        # Prepare the email
        print("Attempting to send email...")
        message = MIMEMultipart()
        message["From"] = credentials.EMAIL
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, 'plain'))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        server.sendmail(from_addr=credentials.EMAIL, to_addrs=to_email, msg=message.as_string())

        # Success!
        print("Sent!")


if __name__ == '__main__':
    send_email(to_email="whateveremailyouwant@mail.com",
               subject="UDEMY - Sending email with Python,",
               body="Practise SMTP/Email send using Python", image=None)
