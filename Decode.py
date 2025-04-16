from PIL import Image

def decode_image(image_path):
    # Open the image
    img = Image.open(image_path)
    # Get the pixels of the image
    pixels = img.load()
    # Initialize the binary message
    message_bin = ''
    # Loop through every pixel in the image
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # Get the RGB values of the pixel
            r, g, b = pixels[i, j]
            # Extract the least significant bit of each color
            message_bin += str(r & 1)
            message_bin += str(g & 1)
            message_bin += str(b & 1)
            # Check if we've reached the end of the message (end of file indicator)
            if len(message_bin) >= 8 * 100:  # Arbitrary size limit (e.g., 100 characters)
                break
    # Convert the binary message into text
    message = ''.join(chr(int(message_bin[i:i+8], 2)) for i in range(0, len(message_bin), 8))
    print("Decoded message:", message)

# Example usage
if __name__ == "__main__":
    decode_image("encoded_image.png")
