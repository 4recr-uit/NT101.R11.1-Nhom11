import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

#ham dao bit tai vi tri thu x
def flip_bit(data, byte_index, bit_index):
    data_array = bytearray(data)
    data_array[byte_index] ^= (1 << bit_index)
    return bytes(data_array)

# dem so khoi bi hong
def analyze_corruption(original_pt, decrypted_pt, mode_name):
    block_size = AES.block_size
    total_blocks = len(original_pt) // block_size
    corrupted_blocks = 0
    corrupted_indices = []

    for i in range(total_blocks):
        org_block = original_pt[i*block_size : (i+1)*block_size]
        dec_block = decrypted_pt[i*block_size : (i+1)*block_size]
        if org_block != dec_block:
            corrupted_blocks += 1
            corrupted_indices.append(i)

    print(f"== {mode_name} ==")
    print(f"tổng số block: {total_blocks}")
    print(f"số block bị lệch: {corrupted_blocks}")
    if corrupted_blocks > 0:
        print(f"các block bị lệch: {corrupted_indices}")
    print()

def run_test(mode_name, mode, iv):

    key = os.urandom(16)
    plaintext = os.urandom(1000)

    padded_pt = pad(plaintext, AES.block_size)

    if mode == AES.MODE_CFB:
        cipher_enc = AES.new(key, mode, iv=iv, segment_size=128)
    elif mode == AES.MODE_ECB:
        cipher_enc = AES.new(key, mode)
    else:
        cipher_enc = AES.new(key, mode, iv=iv)

    ciphertext = cipher_enc.encrypt(padded_pt)
    corrupted_ct = flip_bit(ciphertext, 26, 0)

    if mode == AES.MODE_CFB:
        cipher_dec = AES.new(key, mode, iv=iv, segment_size=128)
    elif mode == AES.MODE_ECB:
        cipher_dec = AES.new(key, mode)
    else:
        cipher_dec = AES.new(key, mode, iv=iv)

    decrypted_padded = cipher_dec.decrypt(corrupted_ct)
    analyze_corruption(padded_pt, decrypted_padded, mode_name)

if __name__ == "__main__":
    iv = os.urandom(16)
    print("== bài 2.4: lan truyền lỗi ==")
    run_test("ECB", AES.MODE_ECB, iv)
    run_test("CBC", AES.MODE_CBC, iv)
    run_test("CFB", AES.MODE_CFB, iv)
    run_test("OFB", AES.MODE_OFB, iv)
