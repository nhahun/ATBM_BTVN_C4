def mod_inverse(e, phi):
    """Tìm nghịch đảo modular của e mod phi bằng Extended Euclidean Algorithm"""
    def egcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = egcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception("Không tồn tại nghịch đảo modular")
    return x % phi


p = 17
q = 23
e = 5
n = p * q            
phi = (p - 1) * (q - 1)

d = mod_inverse(e, phi)

print(f"n = {n}, phi = {phi}, e = {e}, d = {d}")

def char_to_num(ch):
    return ord(ch) - ord('A')

def num_to_char(num):
    return chr(num + ord('A'))

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

plaintext = "TRANTHANHNHA"


nums = [char_to_num(ch) for ch in plaintext]


ciphertext = [encrypt(m, e, n) for m in nums]

print("Plaintext:", plaintext)
print("Mã số:", nums)
print("Ciphertext:", ciphertext)


decrypted_nums = [decrypt(c, d, n) for c in ciphertext]
decrypted_text = ''.join(num_to_char(m) for m in decrypted_nums)

print("Giải mã:", decrypted_text)
