from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

print(f" YOUR SECRET KEY: {key.decode()}")
print("-" * 30)

# 2. THE MESSAGE (The 'Plain' Text)
message = input("Enter a secret message to encrypt: ")
secret_data = cipher_suite.encrypt(message.encode())

print(f"\n SENDING ENCRYPTED DATA: {secret_data.decode()}")

# 4. DECRYPTION (The Receiver uses the Key to read it)
decrypted_data = cipher_suite.decrypt(secret_data)
final_message = decrypted_data.decode()

print(f"\n RECEIVER UNLOCKED MESSAGE: {final_message}")