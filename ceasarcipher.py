alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt \n")
text = input("Type your message: \n").lower()
shift = int(input("Type your shift number 1-26 \n"))


def encrypt(text,shift):
    #modify the alphabet with the shift
    slice1 = alphabet[:shift]
    slice2 = alphabet[shift:]
    slice2.extend(slice1)

    encrypted_text = ""

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_char = slice2[index]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text,shift):
    #modify the alphabet with the shift
    slice1 = alphabet[:shift]
    slice2 = alphabet[shift:]
    slice2.extend(slice1)

   
    encrypted_text = ""

    for char in text:
        if char in slice2:
            index = slice2.index(char)
            encrypted_char = alphabet[index]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text
        



if direction == "decode":
    decrypted = decrypt(text,shift)
    print(decrypted)
elif direction == "encode":    
    encrypted = encrypt(text,shift)
    print(encrypted)

