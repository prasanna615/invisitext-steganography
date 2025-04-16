from stegano import lsb
from tkinter import Tk, filedialog, simpledialog

def encode_message():
    # Hide the root window of tkinter
    root = Tk()
    root.withdraw()

    # Step 1: Open file dialog to choose image
    print("Select the image you want to encode the message into...")
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    if not image_path:
        print("No image selected. Exiting.")
        exit()

    # Step 2: Input the message to encode
    message = simpledialog.askstring("Input", "Enter the message to encode:")

    if not message:
        print("No message entered. Exiting.")
        exit()

    # Step 3: Encode the message into the image
    print(f"Encoding image with message: {message}")
    encoded_image = lsb.hide(image_path, message)

    # Step 4: Ask where to save the encoded image
    print("Select where to save the encoded image...")
    output_path = filedialog.asksaveasfilename(title="Save Encoded Image As", defaultextension=".png", filetypes=[("PNG files", "*.png")])

    if not output_path:
        print("No output path selected. Exiting.")
        exit()

    # Save the encoded image
    encoded_image.save(output_path)
    print(f"✅ Message encoded successfully and saved at: {output_path}")

def decode_message():
    # Hide the root window of tkinter
    root = Tk()
    root.withdraw()

    # Step 1: Let the user choose the image file
    print("Select the encoded image to decode...")
    image_path = filedialog.askopenfilename(title="Select encoded image", filetypes=[("PNG files", "*.png")])

    if image_path:
        try:
            secret = lsb.reveal(image_path)
            if secret:
                print(f"🔓 Decoded message: {secret}")
            else:
                print("⚠️ No hidden message found in the selected image.")
        except Exception as e:
            print(f"❌ Error decoding image: {e}")
    else:
        print("❌ No file selected.")

if __name__ == "__main__":
    print("Welcome to InvisiText Steganography Tool")
    print("1. Encode Message\n2. Decode Message\n")
    choice = input("Select an option (1/2): ")

    if choice == "1":
        encode_message()
    elif choice == "2":
        decode_message()
    else:
        print("Invalid option! Exiting.")
