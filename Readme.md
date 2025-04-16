# InvisiText Steganography

![Steganography Banner](https://img.shields.io/badge/Steganography-LSB_Method-brightgreen)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

InvisiText is a Python-based steganography tool that allows you to seamlessly hide secret messages within images using the Least Significant Bit (LSB) technique. This project provides an intuitive graphical interface for encoding and decoding hidden data.

## 🔍 What is Steganography?

Steganography is the practice of concealing information within other non-secret data or a physical object to avoid detection. Unlike encryption, which makes data unreadable, steganography hides the existence of the secret message altogether.

## ✨ Features

- **Message Encoding:** Hide text messages within PNG or JPG images
- **Message Decoding:** Extract hidden messages from previously encoded images
- **User-Friendly Interface:** Simple GUI with file dialogs for easy image and text selection
- **Minimal Image Alteration:** Uses LSB technique to ensure minimal visual changes to carrier images
- **Cross-Platform:** Works on Windows, macOS, and Linux

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prasanna615/invisitext-steganography.git
   cd invisitext-steganography
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Running the Application

Execute the main Python file to start the application:

```bash
python main.py
```

### Encoding a Message

1. Click the "Encode" button
2. Select an image file (PNG or JPG) using the file dialog
3. Enter your secret message in the text field
4. Choose a save location for the output image
5. The encoded image will be saved with your hidden message

### Decoding a Message

1. Click the "Decode" button
2. Select an image containing a hidden message
3. The secret message will be displayed on the screen

## 🔒 Security Considerations

- The LSB method provides basic steganographic hiding but is not cryptographically secure
- For sensitive information, consider encrypting your message before encoding it
- Large messages may cause noticeable changes in the carrier image

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Contact

Project Link: [https://github.com/prasanna615/invisitext-steganography](https://github.com/prasanna615/invisitext-steganography)
