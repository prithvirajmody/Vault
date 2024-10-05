from cryptography.fernet import Fernet

# Key Creator & Storer
def create_key(key_name):
    key = Fernet.generate_key()
    key_name = f'{key_name}.key'
    with open(key_name, 'wb') as key_file:
        key_file.write(key)
    return key

# Encryption Module
def encrypt(file_path, encryption_key):
    with open(file_path, 'rb') as target_file:
        file_content = target_file.read()

    encrypted_content = encryption_key.encrypt(file_content)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content)

# Decryption Module
def decrypt(file_path, encryption_key):
    with open(file_path, 'rb') as target_file:
        file_content = target_file.read()

    decrypted_content = encryption_key.decrypt(file_content)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_content)

def re_encrypt(file_path):
    file_path = input("What is the path?\t")
    i = int(input("How many times do you want to encrypt your data?\t"))
    
    keys = []
    
    # Generate and store multiple keys
    for j in range(0, i):
        key_name = f'{j+1}'  # Key name will be 1.key, 2.key, etc.
        key = create_key(key_name)  # Call the create_key function to generate and save the key
        keys.append(key)

    # Re-encrypt the file multiple times with the corresponding keys
    for j in range(0, i):
        key_name = f'{j+1}.key'  # Key file names will match the order of encryption
        with open(key_name, 'rb') as key_file:
            key = key_file.read()
            encryption_key = Fernet(key)

        encrypt(file_path, encryption_key)  # Call the encrypt function for each round of encryption

    print("Encryption Done")

def stacked_decrypt(file_path, num_times):
    for j in range(num_times, 0, -1):  # Reverse order of decryption
        key_name = f'{j}.key'
        with open(key_name, 'rb') as key_file:
            key = key_file.read()
            decryption_key = Fernet(key)

        decrypt(file_path, decryption_key)  # Call the decrypt function for each round
    print("Decryption Done")

'''
key_file = open(r'C:\Users\prith\OneDrive\Desktop\PRITHVIRAJ MODY\Computer Codes\Python Codes\Vault\key.key', 'rb')
key = key_file.read()
key_file.close()

#Key Creater & storer
def create_key():
    key = Fernet.generate_key()
    key_name = input("Key file name\n")
    key_name = f'{key_name}.key'
    key_file = open(key_name, 'wb')
    key_file.write(key)
    key_file.close()

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