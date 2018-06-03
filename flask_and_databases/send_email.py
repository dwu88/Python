import email.mime.text import MIMEText
import smtplib

# Fill out yours "from_email" and "from_password"
def send_email(email,height):
    from_email=""
    from_password=""
    to_email_email=email

    subject="Height data"
    message = "Hey there, your height is <strong>%s</strong>." %height

    msg =MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email_email
    msg['From'] = from_email

    '''
        Using the gmail smtp server if your email is gmail,
        otherwise, change it to another smtp server
    '''
    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
