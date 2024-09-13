import time
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import itertools

# Generate all possible keys based on the specified pattern
def generate_keys():
    return [(str(i).zfill(4) * 3)[:8].encode() for i in range(2049)]

# Encrypt plaintext using all combinations of keys `a` and `b`
def encrypt_half(plain):
    keys = generate_keys()
    encrypt_dict = {}
    for a, b in itertools.product(keys, repeat=2):
        c1 = DES.new(a, DES.MODE_ECB)
        c2 = DES.new(b, DES.MODE_ECB)
        ct = c1.encrypt(pad(plain, 8))
        ct = c2.encrypt(ct)
        encrypt_dict[ct] = (a, b)
    return encrypt_dict

# Decrypt ciphertext using all combinations of keys `c` and `d` and check against the encryption dictionary
def decrypt_half_and_compare(enc, encrypt_dict):
    keys = generate_keys()
    for c, d in itertools.product(keys, repeat=2):
        c3 = DES.new(c, DES.MODE_ECB)
        c4 = DES.new(d, DES.MODE_ECB)
        try:
            pt = c4.decrypt(enc)
            pt = c3.decrypt(pt)
            if pt in encrypt_dict:
                a, b = encrypt_dict[pt]
                print(f"Found matching keys: a={a}, b={b}, c={c}, d={d}")
                # Now decrypt the flag using the found keys
                decrypted_flag = decrypt_flag(bytes.fromhex(enc_flag), a, b, c, d)
                print("Decrypted FLAG:", decrypted_flag)
                return
        except ValueError:
            # Ignore padding errors or any decryption that fails
            continue

# Function to decrypt the flag using the found keys
def decrypt_flag(ct, a, b, c, d):
    c4 = DES.new(d, DES.MODE_ECB)
    c3 = DES.new(c, DES.MODE_ECB)
    c2 = DES.new(b, DES.MODE_ECB)
    c1 = DES.new(a, DES.MODE_ECB)
    ct = c4.decrypt(ct)
    ct = c3.decrypt(ct)
    ct = c2.decrypt(ct)
    pt = unpad(c1.decrypt(ct), 8)
    return pt

# Example usage with provided data
enc_flag = "1b15e71f37951e9950123c599921985e410be6aeb076cf5ebeac6810cce9bc06fcf07d6e4f33a1aa3c94dd00945dc96e"
enc = bytes.fromhex("cf5fca567b2713cd288489671866baae")
plain = "pl@1ntxt".encode()

# Measure the execution time
start_time = time.time()

# Step 1: Encrypt half and store in dictionary
encrypt_dict = encrypt_half(plain)

# Step 2: Decrypt half and compare with encryption results
decrypt_half_and_compare(enc, encrypt_dict)

end_time = time.time()

# Calculate and print the execution time
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")
