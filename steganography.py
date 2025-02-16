import cv2
import numpy as np
import argparse
from cryptography.fernet import Fernet

# Generate an encryption key
KEY = Fernet.generate_key()
cipher = Fernet(KEY)


def text_to_binary(text):
    """Converts text to binary string."""
    return ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'  # Stop sequence


def binary_to_text(binary_data):
    """Converts binary string back to text."""
    chars = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]
    extracted_text = ""
    for char in chars:
        if char == '11111111':  # Stop sequence found
            break
        extracted_text += chr(int(char, 2))
    return extracted_text


def hide_message(image_path, message, output_path):
    """Hides a secret message inside an image using LSB steganography."""
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Error: Unable to read image!")
        return

    binary_secret = text_to_binary(message)
    data_index = 0
    binary_secret_length = len(binary_secret)

    rows, cols, _ = img.shape

    for row in range(rows):
        for col in range(cols):
            pixel = img[row, col]
            for channel in range(3):  # R, G, B
                if data_index < binary_secret_length:
                    pixel[channel] = (pixel[channel] & ~1) | int(binary_secret[data_index])
                    data_index += 1
                else:
                    break

    # Save image with user-defined output path or default name
    cv2.imwrite(output_path, img)
    print(f"✅ Stego image saved as '{output_path}'")


def extract_message(image_path):
    """Extracts the hidden message from an image."""
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Error: Unable to read image!")
        return

    binary_data = ""
    for row in img:
        for pixel in row:
            for channel in pixel:
                binary_data += str(channel & 1)

    extracted_text = binary_to_text(binary_data)
    print(f"🔍 Extracted Hidden Message: {extracted_text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Secure Data Hiding in Images Using Steganography")

    parser.add_argument("--hide", action="store_true", help="Hide a message inside an image")
    parser.add_argument("--extract", action="store_true", help="Extract a hidden message from an image")
    parser.add_argument("--image", type=str, help="Path to the image file")
    parser.add_argument("--message", type=str, help="Secret message to hide (only used with --hide)")
    parser.add_argument("--o", type=str, default="stego_image.png", help="Output image path (default: stego_image.png)")

    args = parser.parse_args()

    if args.hide:
        if not args.image or not args.message:
            print("❌ Error: --image and --message are required for hiding!")
        else:
            hide_message(args.image, args.message, args.o)

    elif args.extract:
        if not args.image:
            print("❌ Error: --image is required for extraction!")
        else:
            extract_message(args.image)

    else:
        print("❌ Error: Please use --hide or --extract with the required arguments!")
