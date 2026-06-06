def caesar_cipher(text,shift,mode):
    result = ""
    if mode.lower() == "decrypt":
        shift =- shift
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result +=char
    return result
print("===Caesar Cipher Program===")
message = input("Enter the message:")
shift = int(input("Enter shift value:"))
choice = input("Type 'encrypt' to Encrypt or 'decrypt' to Decrypt:")
output = caesar_cipher(message, shift, choice)
print("\nResult:", output)                            