from cryptography.fernet import Fernet
import email, smtplib, ssl
from email import message
import sys

key_file = open(r'C:\Users\prith\OneDrive\Desktop\PRITHVIRAJ MODY\Computer Codes\Python Codes\Vault\key.key', 'rb')
key = key_file.read()
key_file.close()

encryption_key = Fernet(key)

#Key Creater & storer
def create_key():
    key = Fernet.generate_key()
    key_name = input("Key file name\n")
    key_name = f'{key_name}.key'
    key_file = open(key_name, 'wb')
    key_file.write(key)
    key_file.close()

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

'''

#Sends email with encryption key
def send_email(message:str = key, 
             subject:str = "Encryption Key", smtp_server = "smtp.gmail.com", 
             smtp_port:int = 465):

    receiver_email = "prithvirajmody@gmail.com"
    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login("prithvirajmody@gmail.com", "fgod ehrr hyqy hdsf")
        email.sendmail("prithvirajmody@gmail.com", receiver_email, email_message)

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
        file_path = input("File path of desired file\t")
        encrypt(file_path)
        print("File Encrypted")
        # Your processing logic here
    elif command == "decrypt":
        file_path = input("File path of desired file\t")
        decrypt(file_path)
        print("File Decrypted")
        # Your analyzing logic here
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: Vault <command> <filepath>")
    else:
        command = sys.argv[1]
        filepath = sys.argv[2]
        main(command, filepath)