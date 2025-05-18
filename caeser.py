alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def ceaser(original_text, shift_amount,encode_or_decode):
    cipher_text = ""

    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1 #multiplying by -1 will make the shift_amount neg so same code can be used for both encode and decode
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)