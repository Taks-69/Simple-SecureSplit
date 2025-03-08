# **Simple-SecureSplit** 🔓🔀

SecureSplit is a **file splitting and merging tool** with optional **password-based encryption**. It allows users to split large files into smaller parts and later reassemble them. Encryption is very simple, so i don't recommend it for sensitive files.

---

## 🚀 Features

✅ **File Splitting** – Split any file into multiple parts \
✅ **Secure Encryption** – XOR-based password protection for confidential files \
✅ **File Merging** – Reassemble split files back into the original \
✅ **User-Friendly UI** – Simple and interactive Tkinter-based GUI 

---

## 📂 Repository Structure

```
SecureSplit/
│── SecureSplit.py  # Main script
```

---

## 📥 Installation

### **Prerequisites**
- **Python 3.x**
- **pip** (Python Package Installer)
- **Tkinter** (Included in most Python distributions)

### **Clone the Repository**
```bash
git clone https://github.com/Taks-69/Simple-SecureSplit.git
cd Simple-SecureSplit
```

### **Install Required Libraries**
```bash
pip install tk
```

---

## 🛠 Usage

### **Run the Application**
```bash
python SecureSplit.py
```

### **Splitting a File**
1. Click **"Select and Split"**.
2. Choose the file you want to split.
3. Enter the number of parts.
4. Choose whether to **encrypt** with a password.
5. The file will be split into numbered parts.

### **Merging Files**
1. Click **"Select parts and merge"**.
2. Choose the parts of the file.
3. Enter the password (if encrypted).
4. Save the reassembled file.

---

## 🔄 Workflow

1. **User selects a file to split**.
2. **File is divided into parts**, optionally **encrypted with a password**.
3. **Each part is saved separately**.
4. **User selects parts to merge** back into the original file.
5. **Password is required** if the file was encrypted.
6. **Reassembled file is saved** in the chosen directory.

---

## 🔮 Future Features

🔹 **Stronger Encryption** – Replace XOR with AES for enhanced security.\
🔹 **Drag & Drop Support** – Easier file selection.\
🔹 **Custom Save Paths** – User-defined output location.\
🔹 **Multi-Threading** – Faster processing for large files.

---

## 📜 Disclaimer

> This project is for **educational and personal use only**. I am **not responsible** for any misuse.

---

## 📚 License

This project is licensed under the **GNU General Public License v3.0**.

---

🔥 **Feel free to star ⭐ the repository if you find this project useful!** 🚀

