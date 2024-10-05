from cryptography.fernet import Fernet
import email, smtplib, ssl
from email import message
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Encryption Module
def encrypt(file_path):
    with open(file_path, 'rb') as target_file:
        file_content = target_file.read()

    key = Fernet.generate_key()
    encryption_key = Fernet(key)
    encryted_content = encryption_key.encrypt(file_content)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encryted_content)

    #return key
    print(key)

#Decryption Module
def decrypt(file_path, input_key):
    with open(file_path, 'rb') as target_file:
        file_content = target_file.read()

    encryption_key = Fernet(input_key)
    encryted_content = encryption_key.decrypt(file_content)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encryted_content)

def secure(file_path, email_address):


    #Same logic as encrypt function
    with open(file_path, 'rb') as target_file:
        file_content = target_file.read()

    key = Fernet.generate_key()
    encryption_key = Fernet(key)
    encryted_content = encryption_key.encrypt(file_content)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encryted_content)

    send_email_with_key(email_address, key_string=key)

#Sends email with encryption key
def send_email_with_key(recipient_email, key_string):
    # Email account credentials (using Gmail as an example)
    sender_email = "encryption.key.project@gmail.com"  # Replace with your email
    sender_password = "wpfi yexf jmmq qloo"      # Replace with your password/app password

    subject = "Your Encryption Key"
    body = f"Here is your encryption key:\n\n{key_string}"

    # Create the email message
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)  # Log in to the server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
            print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


'''

#Stacked Encryption
def re_encrypt(file_path):
    file_path = input("What is the path?\t")
    i = int(input("How many times over do you want to encrypt your data?\t"))
    key = Fernet.generate_key()
    for j in range(0, i):
        key = Fernet.generate_key()
        key_name = f'{i}.key'
        key_file = open(key_name, 'wb')
        key_file.write(key)
        key_file.close()
        j+=1
    for k in range(0, i):
        # Redefine key name
        key_name = f'{k}.key'
        key_file = open(key_name, 'rb')
        key = key_file.read()
        encryption_key = Fernet(key)

        with open(file_path, 'rb') as target_file:
            file_content = target_file.read()

        encryted_content = encryption_key.encrypt(file_content)

        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encryted_content)

        k+=1
    print("Done")


    #To be put in while loop
    if intent == 'n-encrypt':
        file_path == input("File path\t")
        re_encrypt()
        print("File encrypted")

while True:

    intent = input("What is your intent?\n")
    password = "prithviraj@mody$2006&"

    if intent == 'encrypt':
        file_path = input("File path of desired file\t")
        encrypt(file_path)
        print("File Encrypted")
    elif intent == 'decrypt':
        file_path = input("File path of desired file\t")
        passcode = input("What is the password?\t")
        if passcode == password:
            decrypt(file_path)
            print("File Decrypted")
'''

def main(command, file_path):
    # Add logic to handle different commands
    if command == "encrypt":
        encrypt(file_path)
        print("File Encrypted")

    elif command == "decrypt":
        enc_key = input("Enter the key:\t")
        decrypt(file_path, enc_key)
        print("File Decrypted")
        # Your analyzing logic here
    elif command == "secure":
        address = input("Enter the email address to whom the encryption key will be sent:\t")
        secure(file_path, address)
        print("File encrypted! The key has been sent to " + address)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: Vault <command> <filepath>")
    else:
        command = sys.argv[1]
        filepath = sys.argv[2]
        main(command, filepath)