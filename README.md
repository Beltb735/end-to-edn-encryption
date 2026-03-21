# end-to-edn-encryption

In modern networking, "Cleartext" (plain text) is a massive security risk. This project implements a Symmetric Key Encryption system using the AES (Advanced Encryption Standard) algorithm. It is designed to simulate a secure communication bridge where data is encrypted locally before being transmitted over an untrusted network.

##  How to Use
1. **Install Dependencies:** `pip install cryptography`
2. **Setup:** Ensure both `sender.py` and `receiver.py` share the same 32-byte Fernet key.
3. **Run Sender:** Execute `python sender.py`, enter your message, and copy the output.
4. **Run Receiver:** Execute `python receiver.py` and paste the encrypted string to reveal the plaintext.<img width="724" height="456" alt="Screenshot 2026-03-21 181315" src="https://github.com/user-attachments/assets/3c7a1e7d-444d-4d65-a9fd-0f78149fead2" />
<img width="1137" height="154" alt="Screenshot 2026-03-21 181323" src="https://github.com/user-attachments/assets/18004034-39bb-4d7e-b243-acdbdeb1e84d" />
<img width="758" height="266" alt="Screenshot 2026-03-21 181330" src="https://github.com/user-attachments/assets/28bc21e3-89ad-4839-ae91-a5564869a6d3" />
<img width="984" height="115" alt="Screenshot 2026-03-21 181340" src="https://github.com/user-attachments/assets/36e4fd7f-4008-4458-b841-c89123c00248" />
<img width="716" height="284" alt="Screenshot 2026-03-21 181347" src="https://github.com/user-attachments/assets/08e25ec3-5252-4821-9ce7-820d9491890a" />
<img width="1240" height="98" alt="Screenshot 2026-03-21 181357" src="https://github.com/user-attachments/assets/a67858ea-d650-4a7c-acf5-4d9feb6db438" />
