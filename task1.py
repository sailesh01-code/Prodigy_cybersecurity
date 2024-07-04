def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
            else:
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            shifted_index = (alphabet.index(char) + shift * mode) % 26
            result += alphabet[shifted_index]
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Please enter 'encrypt' or 'decrypt'")
            continue
        
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value (a number between 1 and 25): "))
        if shift < 1 or shift > 25:
            print("Shift value must be between 1 and 25")
            continue
        
        if choice == 'encrypt':
            encrypted_text = caesar_cipher(text, shift, 1)
            print("Encrypted message:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, shift, -1)
            print("Decrypted message:", decrypted_text)
        
        another = input("Would you like to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
    