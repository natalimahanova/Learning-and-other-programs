def caesar_cipher(text, shift, language='english', direction='encrypt'):
    if language == 'english':
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num_letters = 26
    elif language == 'russian':
        alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        num_letters = 32
    else:
        return "Unsupported language. Please choose 'english' or 'russian'."
    
    if direction == 'decrypt':
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    result = ''
    for char in text:
        if char.upper() in alphabet:
            is_upper = char.isupper()
            index = alphabet.find(char.upper())
            shifted_char = shifted_alphabet[index]
            if is_upper:
                result += shifted_char.upper()
            else:
                result += shifted_char.lower()
        else:
            result += char
    
    return result

direction = input("Enter 'encrypt' for encryption or 'decrypt' for decryption: ")
language = input("Enter 'english' for English alphabet or 'russian' for Russian alphabet: ")
shift = int(input("Enter the shift value (positive integer): "))
text = input("Enter the text to encrypt/decrypt: ")

result = caesar_cipher(text, shift, language, direction)
print("Result:", result)
