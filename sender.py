from cryptography.fernet import Fernet

key = "hEEX9Qz9RC-EWoxB-VdZO7rdepokoz_Y2aodEWppP7E= "
cipher = Fernet(key)
message = input("Enter secret message to send: ")
encrypted_msg = cipher.encrypt(message.encode())

print("-" * 30)
print(f" COPY THIS DATA TO THE RECEIVER:\n{encrypted_msg.decode()}")
print("-" * 30)