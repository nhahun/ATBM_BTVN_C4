def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += char 
    return ciphertext

# Dữ liệu đầu vào
plaintext = "TRANTHANHNHA"
shift = 19

ciphertext = caesar_encrypt(plaintext, shift)
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
