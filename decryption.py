import cv2

def decrypt_image(image_path, original_message_length, passcode):
    # Read the encrypted image
    img = cv2.imread(image_path)

    # Verify that the image was loaded successfully
    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Create dictionaries for encoding and decoding
    c = {i: chr(i) for i in range(255)}

    # Initialize coordinates
    m, n, z = 0, 0, 0
    rows, cols, _ = img.shape

    # Input passcode for decryption
    entered_passcode = input("Enter passcode for Decryption: ")

    if entered_passcode == passcode:
        # Decrypt the message from the image
        message = ""
        for i in range(original_message_length):
            message += c[img[n, m, z]]
            n = (n + 1) % rows
            m = (m + 1) % cols
            z = (z + 1) % 3

        print("Decryption message:", message)
    else:
        print("YOU ARE NOT authorized")

# Example usage
encrypted_image_path = "encryptedImage.jpg"
original_message_length = 14  # Replace with the actual length of the original secret message
decrypt_image(encrypted_image_path, original_message_length, "678")  # Replace "678" with the actual passcode used during encryption
