from stegano import lsb
from tkinter import Tk, filedialog

# Hide the root window of tkinter
root = Tk()
root.withdraw()

# Step 1: Open file dialog to choose the encoded image
print("Select the encoded image to decode...")
image_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG files", "*.png")])

if not image_path:
    print("No image selected. Exiting.")
    exit()

# Step 2: Decode the message from the selected image
try:
    secret = lsb.reveal(image_path)
    if secret:
        print(f"🔓 Decoded message: {secret}")
    else:
        print("⚠️ No hidden message found in the selected image.")
except Exception as e:
    print(f"❌ Error decoding image: {e}")
