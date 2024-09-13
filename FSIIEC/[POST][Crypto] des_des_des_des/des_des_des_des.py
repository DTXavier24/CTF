from Crypto.Cipher import DES
import random
from Crypto.Util.Padding import pad, unpad

a = b""
b = b""
c = b""
d = b""
FLAG = b"IIECTF{REDACTED}"

def generateKey():
	global a, b, c, d
	a = (str(random.randint(0, 2048)).zfill(4)*3)[:8].encode()
	b = (str(random.randint(0, 2048)).zfill(4)*3)[:8].encode()
	c = (str(random.randint(0, 2048)).zfill(4)*3)[:8].encode()
	d = (str(random.randint(0, 2048)).zfill(4)*3)[:8].encode()

def encrypt(plaintext, a, b, c, d):
	c1 = DES.new(a, mode=DES.MODE_ECB)
	ct = c1.encrypt(pad(plaintext, 8))
	c2 = DES.new(b, mode=DES.MODE_ECB)
	ct = c2.encrypt(ct)
	c3 = DES.new(c, mode=DES.MODE_ECB)
	ct = c3.encrypt(ct)
	c4 = DES.new(d, mode=DES.MODE_ECB)
	ct = c4.encrypt(ct)
	return ct.hex()

generateKey()

print("enc_flag =", encrypt(FLAG, a, b, c, d))
plain = "pl@1ntxt"
print("enc =", encrypt(plain.encode(), a, b, c, d))
'''
enc_flag = 1b15e71f37951e9950123c599921985e410be6aeb076cf5ebeac6810cce9bc06fcf07d6e4f33a1aa3c94dd00945dc96e
enc = cf5fca567b2713cd288489671866baae
'''
