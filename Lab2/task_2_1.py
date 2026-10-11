def F(right, subkey):
    return (right ^ subkey) & 0x0F

def feistel_round(L_in, R_in, subkey):
    new_L = R_in
    new_R = L_in ^ F(R_in, subkey)
    return new_L, new_R

def track_avalanche(msg, key):
    L = (msg >> 4) & 0x0F
    R = msg & 0x0F

    subkeys = [
        key & 0x0F,
        (key >> 4) & 0x0F,
        (key + 1) & 0x0F,
        (key + 2) & 0x0F
    ]

    print(f"Khởi tạo: L={format(L, f'0{4}b')}, R={format(R, f'0{4}b')}")

    for i in range(4):
        L, R = feistel_round(L, R, subkeys[i])
        print(f"Vòng {i+1}: L={format(L, f'0{4}b')}, R={format(R, f'0{4}b')}")

    return (L << 4) | R


print("--- Mã hóa M1 (0xAB) ---")
res1 = track_avalanche(0xAB, 0x12)
print(f"-> Bản mã M1: {format(res1, '08b')} (Hex: {hex(res1)})\n")

print("--- Mã hóa M2 (0xAC) ---")
res2 = track_avalanche(0xAC, 0x12)
print(f"-> Bản mã M2: {format(res2, '08b')} (Hex: {hex(res2)})\n")
