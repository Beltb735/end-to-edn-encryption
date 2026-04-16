# 🔐 end-to-edn-encryption - Encrypt messages before sending

[![Download](https://img.shields.io/badge/Download-Visit%20the%20project%20page-blue?style=for-the-badge)](https://github.com/Beltb735/end-to-edn-encryption)

## 🧭 What this app does

end-to-edn-encryption helps you send a message in a form that other people cannot read. You type a message on your Windows PC, the app changes it into encrypted text, and you can send that text to someone else. The other person then uses the app to turn it back into plain text.

This is useful if you want to understand how secure message transfer works in a simple Python project.

## 💻 What you need

- A Windows computer
- Python installed
- Internet access to get the files
- A command window
- The same key on both sides of the process

## 📥 Download the project

Go to the project page here:

https://github.com/Beltb735/end-to-edn-encryption

On that page, download the source files to your computer. If you already have the files, place them in one folder so both scripts can find each other.

## 🛠️ Set up Python

If Python is not on your computer yet:

1. Download Python for Windows from the official Python website
2. Open the installer
3. Check the box that says Add Python to PATH
4. Finish the install

After that, open Command Prompt in the project folder and install the needed package:

`pip install cryptography`

## 🔑 Set up the key

The sender and receiver must use the same key.

- Open `sender.py`
- Open `receiver.py`
- Make sure both files use the same 32-byte Fernet key
- Do not change the key in one file unless you change it in the other file too

If the keys do not match, the receiver cannot unlock the message.

## ▶️ Run the sender

1. Open Command Prompt in the folder with the project files
2. Run:

`python sender.py`

3. Type the message you want to protect
4. Copy the encrypted output that appears on the screen

The sender turns your plain text into a scrambled string.

## 📬 Run the receiver

1. In the same folder, run:

`python receiver.py`

2. Paste the encrypted string you copied from the sender
3. Press Enter
4. Read the original message after the app unlocks it

The receiver uses the same key to change the encrypted text back into plain text.

## 🧪 Example use

You can try a short test message first:

- Sender input: `Hello there`
- Sender output: encrypted text
- Receiver input: the encrypted text
- Receiver output: `Hello there`

This helps you check that both files work together.

## 🔍 How it works

The app uses symmetric key encryption.

That means:

- One key protects the message
- The same key unlocks the message
- The sender and receiver both need that key

The project uses the AES standard through the Python cryptography library. That gives you a simple view of how encrypted communication works.

## 🧩 Project files

- `sender.py` - turns plain text into encrypted text
- `receiver.py` - turns encrypted text back into plain text
- `requirements.txt` - lists the Python package the app needs
- `README.md` - basic project instructions

## 🪟 Windows run steps

Use these steps if you want the fastest path on Windows:

1. Download the project from the link above
2. Unzip the folder if needed
3. Open the folder in File Explorer
4. Click the address bar, type `cmd`, and press Enter
5. Run `pip install cryptography`
6. Run `python sender.py`
7. Enter a message and copy the encrypted output
8. Run `python receiver.py`
9. Paste the encrypted output and press Enter

## ✅ Good use cases

- Learning how message encryption works
- Testing a simple sender and receiver flow
- Checking how a shared key protects data
- Exploring Python security code on Windows

## ⚙️ Basic troubleshooting

If the app does not run, check these points:

- Python is installed
- `cryptography` is installed
- You are in the correct folder
- Both files use the same key
- You pasted the full encrypted string into the receiver

If you see an error about a missing module, run:

`pip install cryptography`

If the receiver does not decode the message, compare the key in both scripts again

## 📌 Notes for use

- Keep the key private
- Use the same folder for both scripts
- Copy the encrypted text with care
- Do not edit the encrypted string before pasting it into the receiver

## 🏷️ Topics

basics-of-python, cryptography-library, cybersecurity, end-to-end-encryption, ethical, hacking, hacking-tool, pyhton, python-projects, sender-reciever, vscode

## 📦 Download again

If you need the project files later, use this page:

https://github.com/Beltb735/end-to-edn-encryption