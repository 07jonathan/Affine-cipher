def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plaintext, a, b):
    # Check if 'a' and the alphabet size are coprime
    m = 26
    if gcd(a, m) != 1:
        raise ValueError("'a' must be coprime with 26.")

    # Encryption
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')
            y = (a * x + b) % m
            encrypted_char = chr(y + ord('a'))
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    # Check if 'a' and the alphabet size are coprime
    m = 26
    if gcd(a, m) != 1:
        raise ValueError("'a' must be coprime with 26.")

    # Decryption
    plaintext = ''
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        raise ValueError("Multiplicative inverse of 'a' mod 26 does not exist.")

    for char in ciphertext:
        if char.isalpha():
            y = ord(char.lower()) - ord('a')
            x = (a_inv * (y - b)) % m
            decrypted_char = chr(x + ord('a'))
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = "Hello, World!"
a = 5
b = 8

encrypted = affine_encrypt(plaintext, a, b)
decrypted = affine_decrypt(encrypted, a, b)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
