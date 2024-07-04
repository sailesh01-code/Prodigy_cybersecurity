from PIL import Image

def swap_pixels(image):
    width, height = image.size
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = pixels[width - i - 1, height - j - 1]
            pixels[width - i - 1, height - j - 1] = (r, g, b)

def apply_operation(image, operation):
    width, height = image.size
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = operation(r), operation(g), operation(b)

def encrypt_image(image_path, operation):
    image = Image.open(image_path)
    apply_operation(image, operation)
    image.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, operation):
    encrypted_image = Image.open(encrypted_image_path)
    apply_operation(encrypted_image, operation)
    encrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    image_path = input("Enter the path to the image: ")
    operation_choice = input("Choose an operation to perform (swap/operation): ").lower()

    if operation_choice == 'swap':
        image = Image.open(image_path)
        swap_pixels(image)
        image.save("encrypted_image.png")
        print("Image encrypted successfully with pixel swapping!")
    elif operation_choice == 'operation':
        operation = lambda x: 255 - x  # Example operation: Inversion
        encrypt_image(image_path, operation)
        decrypt_image("encrypted_image.png", operation)
    else:
        print("Invalid operation choice.")

if __name__ == "__main__":
    main()