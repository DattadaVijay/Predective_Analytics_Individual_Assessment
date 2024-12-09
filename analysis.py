from cryptography.fernet import Fernet
import pandas as pd
def generate_key():
    return Fernet.generate_key()
def save_key(key, filename='encryption_key.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)
def load_key(filename='encryption_key.key'):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_emails(df, key):
    fernet = Fernet(key)
    encrypted_emails = df['Email'].apply(lambda x: fernet.encrypt(x.encode()).decode())
    df['Email'] = encrypted_emails
    return df

df = pd.read_csv('Office Data.csv') 

if 'Email' not in df.columns:
    raise ValueError("The dataset does not contain an 'Email' column!")

key = generate_key()

save_key(key)

df_encrypted = encrypt_emails(df, key)

df_encrypted.to_csv('encrypted_Office_Data.csv', index=False)

print("Encryption complete. The encrypted file is saved as 'encrypted_Office_Data.csv'.")
