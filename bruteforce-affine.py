import string

# Function to compute the modular inverse of a
def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

# Function to decrypt a single character using a given pair of keys (a, b)
def decrypt_char(c, a_inv, b, m):
    if c in string.ascii_lowercase:
        y = string.ascii_lowercase.index(c)
        x = (a_inv * (y - b)) % m
        return string.ascii_lowercase[x]
    else:
        return c

# Function to decrypt the entire message using a given pair of keys (a, b)
def decrypt_affine_cipher(ciphertext, a, b, m):
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    return ''.join(decrypt_char(c, a_inv, b, m) for c in ciphertext)

# Brute force attack on Affine Cipher
def brute_force_affine(ciphertext, m=26):
    possible_messages = []
    for a in range(1, m):
        if mod_inverse(a, m) is not None:  # a must be coprime with m
            for b in range(m):
                decrypted_message = decrypt_affine_cipher(ciphertext, a, b, m)
                possible_messages.append((a, b, decrypted_message))
    return possible_messages

# Example ciphertext
ciphertext = "ymnx nx f xywnsl"

# Perform brute force attack
possible_messages = brute_force_affine(ciphertext)

# Print possible decrypted messages
for a, b, message in possible_messages:
    print(f"a={a}, b={b}: {message}")
