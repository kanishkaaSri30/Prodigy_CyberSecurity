from PIL import Image
def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)
    img.save(output_image)
    print("Image encrypted successfully!")
def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)
    img.save(output_image)
    print("Image decrypted successfully!")
def main():
    print("=== Image Encryption Tool ===")
    choice = input("Enter E for Encrypt or D for Decrypt: ").upper()
    input_file = input("Enter input image path: ")
    output_file = input("Enter output image path: ")
    key = int(input("Enter secret key (0-255): "))
    if choice == "E":
        encrypt_image(input_file, output_file, key)
    elif choice == "D":
        decrypt_image(input_file, output_file, key)
    else:
        print("Invalid choice!")
if __name__ == "__main__":
    main()