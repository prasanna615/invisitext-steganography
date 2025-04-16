<<<<<<< HEAD
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
output_path = filedialog.asksaveasfilename(title="Save Encoded Image As", defaultextension=".png", filetypes=[("PNG image", "*.png")])

if not output_path:
    print("No output path selected. Exiting.")
    exit()

# Save the encoded image
encoded_image.save(output_path)
print(f"✅ Message encoded successfully and saved at: {output_path}")
=======
from PIL import Image

def encode_image(image_path, message, output_path):
    # Open the image
    img = Image.open(image_path)
    # Convert the message into binary
    message_bin = ''.join(format(ord(char), '08b') for char in message)
    # Get the pixels of the image
    pixels = img.load()
    # Initialize the message index
    message_index = 0
    # Loop through every pixel in the image
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # Get the RGB values of the pixel
            r, g, b = pixels[i, j]
            # Modify the least significant bit of each color
            if message_index < len(message_bin):
                r = r & ~1 | int(message_bin[message_index])
                message_index += 1
            if message_index < len(message_bin):
                g = g & ~1 | int(message_bin[message_index])
                message_index += 1
            if message_index < len(message_bin):
                b = b & ~1 | int(message_bin[message_index])
                message_index += 1
            # Update the pixel with the new values
            pixels[i, j] = (r, g, b)
            if message_index == len(message_bin):
                break
    # Save the image with the hidden message
    img.save(output_path)
    print(f"Message encoded in image saved to {output_path}")

# Example usage
if __name__ == "__main__":
    encode_image("input_image.png", "This is a secret message", "encoded_image.png")
>>>>>>> 9ed376891358988e38195fd293b5f88eda231e9e
