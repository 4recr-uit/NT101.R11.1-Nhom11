from dependencies import install_dependencies
install_dependencies(["pycryptodome"])

from Crypto.Cipher import AES

key = b'1234567890123456'
plaintext = b"UIT_LAB_UIT_LAB_UIT_LAB_UIT_LAB_"
iv = b'0123456789abcdef'

print(f"plaintext: {plaintext.decode('utf-8')}\n")
print(f"plaintext (hex): {plaintext.hex()}")

def print_and_compare(mode_name, ciphertext):
    hex_str = ciphertext.hex()
    block1 = hex_str[:32]
    block2 = hex_str[32:]

    print(f"== {mode_name} ==")
    print(f"block 1 (16 byte): {block1}")
    print(f"block 2 (16 byte): {block2}")
    print(f"giống nhau: {block1 == block2}\n")
    return block1, block2

cipher_ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = cipher_ecb.encrypt(plaintext)
print_and_compare("aes-ecb", ct_ecb)

cipher_cbc = AES.new(key, AES.MODE_CBC, iv=iv)
ct_cbc = cipher_cbc.encrypt(plaintext)
print_and_compare("aes-cbc", ct_cbc)

cipher_cfb = AES.new(key, AES.MODE_CFB, iv=iv)
ct_cfb = cipher_cfb.encrypt(plaintext)
print_and_compare("aes-cfb", ct_cfb)

cipher_ofb = AES.new(key, AES.MODE_OFB, iv=iv)
ct_ofb = cipher_ofb.encrypt(plaintext)
print_and_compare("aes-ofb", ct_ofb)

cipher_ctr = AES.new(key, AES.MODE_CTR, nonce=b'12345678')
ct_ctr = cipher_ctr.encrypt(plaintext)
print_and_compare("aes-ctr", ct_ctr)
