# 🔐 **Secure Data Hiding in Images Using Steganography**  

A Python-based **steganography** tool that allows you to **hide and extract** secret messages from images using **LSB (Least Significant Bit) encoding**.  

✅ **Supports PNG, JPG, BMP, and other image formats**  
✅ **Allows custom output image names and formats**  
✅ **Simple command-line interface for easy use**  

---

## 📌 **Features**  
✔️ **Hide Secret Messages** inside images.  
✔️ **Extract Hidden Messages** from images.  
✔️ Uses **LSB Steganography** for data encoding.  
✔️ Works with **PNG, JPG, BMP, and more**.  
✔️ **Allows user-defined output image formats** or uses the default (`stego_image.png`).  
✔️ **Lightweight and easy to use** CLI-based tool.  

---

## 🛠 **Installation**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/manmohansethi/steganography.git
cd steganography
```

### **Step 2: Install Required Dependencies**  
```bash
pip install -r requirements.txt
```

📌 **Dependencies:**  
- `opencv-python` (for image processing)  
- `numpy` (for handling pixel data)  
- `cryptography` (for future encryption use)  

---

## 🚀 **Usage Guide**  

### ✅ **Hiding a Message in an Image**  
```bash
python steganography.py --hide --image input.png --message "Secret Info"
```
🔹 This hides `"Secret Info"` inside `input.png` and saves the result as `stego_image.png` (default).  

```bash
python steganography.py --hide --image input.jpg --message "Confidential Data" --o secret_image.webp
```
🔹 This hides `"Confidential Data"` inside `input.jpg` and saves the result as `secret_image.webp`.  

📌 **You can save the output image in any format (`.png`, `.jpg`, `.bmp`, `.webp`, etc.)!**  

---

### ✅ **Extracting a Hidden Message from an Image**  
```bash
python steganography.py --extract --image stego_image.png
```
🔹 Extracts and **prints** the hidden message from `stego_image.png`.  

```bash
python steganography.py --extract --image secret_image.webp
```
🔹 Extracts the hidden message from `secret_image.webp`.  

---

## 📂 **Project Structure**  
```
📁 steganography_project
│── steganography.py      # Main script for hiding & extracting messages
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
```

---

## 🤖 **How It Works (LSB Steganography)**  
1️⃣ **Hiding:** Each character of the secret message is converted into a binary format.  
2️⃣ **Embedding:** The binary data is embedded in the least significant bits (LSB) of image pixels.  
3️⃣ **Extracting:** The hidden bits are extracted from the image and converted back into text.  

---

## 💡 **Example Usage**  
### **Hiding a Message**
**Input Command:**
```bash
python steganography.py --hide --image nature.jpg --message "Hello, World!" --o secret.bmp
```
**Output:**
```
✅ Stego image saved as 'secret.bmp'
```

### **Extracting the Message**
**Input Command:**
```bash
python steganography.py --extract --image secret.bmp
```
**Output:**
```
🔍 Extracted Hidden Message: Hello, World!
```

---

## 🏆 **Why Use This Project?**  
🔹 **Simple & Easy** to use.  
🔹 **Data Privacy:** Keep messages secure inside images.  
🔹 **Works with PNG, JPG, BMP, WEBP, and other formats**.  
🔹 **No Data Loss:** The original image quality is **preserved**.  

---

## 📜 **License**  
This project is **open-source** and free to use under the **MIT License**.  

---

## 🌟 **Contributing**  
Want to improve this project? Contributions are welcome! Feel free to submit a **pull request**.

---

## 📧 **Contact**  
📌 **GitHub:** [Your Profile](https://github.com/your-username)  
📌 **Email:** your-email@example.com  
s
