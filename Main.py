def caesar_cipher_encrypt(text, shift):
    # Initialize an empty string to store the encrypted text
    encrypted_text = ""
    # Loop through each character in the input text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the base ASCII value depending on whether the letter is lowercase or uppercase
            if char.islower():
                shift_base = ord('a')
            else:
                shift_base = ord('A')
            # Shift the character and wrap around the alphabet
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    # Decryption is just encryption with a negative shift
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    # Ask the user if they want to encrypt or decrypt a message
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ")
    # Get the message from the user
    message = input("Enter your message: ")
    # Get the shift value from the user
    shift = int(input("Enter the shift value: "))
    
    # Check if the user chose to encrypt
    if choice.lower() == 'e':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    # Check if the user chose to decrypt
    elif choice.lower() == 'd':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)
    else:
        # If the user entered an invalid choice
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
