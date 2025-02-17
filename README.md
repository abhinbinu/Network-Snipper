# **🔍 Network Scanner (Python)**

🚀 A powerful **network scanner** written in Python using **Scapy**. It **discovers active devices** on the local network by sending **ARP requests**.

## **📂 Features**
- ✅ **Hacker-style loading animation** (Sniffer effect)
- ✅ **Finds live devices** (IP & MAC addresses)
- ✅ **Command-line support** (Scan any subnet)
- ✅ **Debugging messages** for transparency
- ✅ **Optimized error handling** (No response detection)
- ✅ **Author credit: Abhin Binu**

---

## **📸 Demo**
![Network Scanner Demo](https://user-images.githubusercontent.com/your-image-link.gif)  
_*(Replace with your own GIF or screenshot)*_

---

## **⚙️ Installation**
### **1️⃣ Install Dependencies**
Ensure **Python 3** and `scapy` are installed:  
```bash
pip install scapy
```

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/abhinbinu/network-scanner.git
cd network-scanner
```

---

## **🚀 Usage**
Run the script with **sudo/root permissions** for best results:  
```bash
python3 scanner.py -t <target IP range>
```
Example:
```bash
sudo python3 scanner.py -t 192.168.1.1/24
```

---

## **📃 Output Example**
```
Initializing Network Sniffer...

Scanning Network: [■□□□□□□□□□] 10%
Scanning Network: [■■■■■■■■■■] 100%

✔ Scan Complete! Ready to sniff network packets.

Author: Abhin Binu
=======================================

Discovered Devices:
IP Address        MAC Address
-----------------------------------------
192.168.1.2      00:1A:2B:3C:4D:5E
192.168.1.3      00:1A:2B:3C:4D:5F

Final Results:
IP Address        MAC Address
-----------------------------------------
192.168.1.2      00:1A:2B:3C:4D:5E
192.168.1.3      00:1A:2B:3C:4D:5F
```

---

## **🛠️ How It Works**
- 🔹 **Sends ARP requests** to devices on the target network
- 🔹 **Captures responses** to find active devices
- 🔹 **Displays IP & MAC addresses** of detected devices
- 🔹 **Uses a progress bar animation** for a hacking-style effect

---

## **📂 To-Do / Future Updates**
- ✅ Add **MAC Vendor Lookup** (e.g., Apple, Cisco, etc.)
- ✅ Implement **multi-threading** for faster scanning
- ✅ Integrate **GUI support** (e.g., Tkinter, Flask)

---

## **👨‍💻 Author**
🛠️ Developed by **Abhin Binu**  

🌐 **Connect with me:**  
📧 Email: [your-email@example.com]  
🔖 LinkedIn: [linkedin.com/in/your-profile]  

---

## **🛡️ Disclaimer**
⚠️ This tool is intended for **educational and ethical** purposes **ONLY**. **Do not use** it for illegal activities. The developer is **not responsible** for any misuse.  

---

