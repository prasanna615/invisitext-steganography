from stegano import lsb
from tkinter import Tk, filedialog, simpledialog

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
