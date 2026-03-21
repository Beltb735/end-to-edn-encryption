from cryptography.fernet import Fernet

key = "hEEX9Qz9RC-EWoxB-VdZO7rdepokoz_Y2aodEWppP7E="
cipher = Fernet(key)

cipher_text = input("🔓 Paste the encrypted data here: ")

try:
    decrypted_msg = cipher.decrypt(cipher_text.encode())
    print(f"\n MESSAGE DECODED: {decrypted_msg.decode()}")
except:
    print("\n ERROR: Wrong key or corrupted data! Hacker detected?")