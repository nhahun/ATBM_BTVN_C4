def caesar_encrypt(plaintext: str, k: int) -> str:
    result = []
    k = k % 26  
    for ch in plaintext:
        if 'A' <= ch <= 'Z':  
            x = ord(ch) - ord('A')
            c = (x + k) % 26
            result.append(chr(c + ord('A')))
        elif 'a' <= ch <= 'z':  
            x = ord(ch) - ord('a')
            c = (x + k) % 26
            result.append(chr(c + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)

P = "TRANTHANHNHA"
k = 19
cipher = caesar_encrypt(P, k)
print("Plaintext:", P)
print("Shift k =", k)
print("Ciphertext:", cipher)
