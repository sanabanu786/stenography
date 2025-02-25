import cv2
import os

def encrypt_image(image_path, secret_message, passcode):
    # Read the image
    img = cv2.imread(image_path)

    # Verify that the image was loaded successfully
    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Create dictionaries for encoding and decoding
    d = {chr(i): i for i in range(255)}

    # Initialize coordinates
    m, n, z = 0, 0, 0
    rows, cols, _ = img.shape

    # Encrypt the message into the image
    for i in range(len(secret_message)):
        img[n, m, z] = d[secret_message[i]]
        n = (n + 1) % rows
        m = (m + 1) % cols
        z = (z + 1) % 3

    # Save the encrypted image
    encrypted_image_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_image_path, img)
    os.system(f"start {encrypted_image_path}")  # Use 'start' to open the image on Windows

    print(f"Encrypted image saved as {encrypted_image_path}")
    return encrypted_image_path, passcode

# Example usage
image_path = "mypic.jpg"
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
encrypt_image(image_path, msg, password)
