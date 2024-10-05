#Uses SMS & MMS gateway email to send messages to phone

import email, smtplib, ssl
from email import message

def send_sms(message:str, 
             subject:str = "Encryption Key", smtp_server = "smtp.gmail.com", 
             smtp_port:int = 465):
    receiver_email = "9198929004372646@airtelmail.com"  #Find proper email address / number of airtel mumbai

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login("prithvirajmody@gmail.com", "fgod ehrr hyqy hdsf")
        email.sendmail("prithvirajmody@gmail.com", receiver_email, email_message)

def main():
    message = "Test 1"
    send_sms(message)

if __name__ == "__main__":
    main()