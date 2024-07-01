# **Caesar Cipher Encryption and Decryption**

This Python program allows users to encrypt and decrypt text using the Caesar Cipher algorithm. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.


## **Features**
1. Encryption: Encrypt a message by shifting each letter by a specified number of places.

2. Decryption: Decrypt a message by reversing the shift.

3. User Input: The program accepts user input for the message and the shift value.

4. Case Handling: Maintains the case of the original message (uppercase and lowercase letters).

5. Non-Alphabetic Characters: Leaves non-alphabetic characters unchanged.



## **How to Use**
1. Clone the Repository:

   `git clone https://github.com/dhar-un-raj/caesar-cipher.git`

   `cd caesar-cipher`

3. Run the Program:

   `python caesar_cipher.py`

4. Follow the Prompts:

- Choose whether to encrypt or decrypt a message.

- Enter the message you wish to process.

- Enter the shift value (an integer).

## Example
### Encryption
```
Do you want to (e)ncrypt or (d)ecrypt a message? e
Enter your message: Hello World!
Enter the shift value: 3
Encrypted Message: Khoor Zruog!
```
### Decryption
```
Do you want to (e)ncrypt or (d)ecrypt a message? d
Enter your message: Khoor Zruog!
Enter the shift value: 3
Decrypted Message: Hello World!
```

## Code Explanation
### Functions
- `caesar_cipher_encrypt(text, shift)`: Encrypts the given `text` by shifting the letters by the specified `shift` value

- `caesar_cipher_decrypt(text, shift)`: Decrypts the `given text` by reversing the shift applied during encryption.

- `main()`: The main function that interacts with the user, taking inputs and displaying the results.

 ## Algorithm
 - For each character in the input text:
     - If it is an alphabet character, shift it within its case (uppercase or lowercase).
     - If it is not an alphabet character, leave it unchanged.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

---
Footer
