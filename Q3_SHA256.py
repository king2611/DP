import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sha256(data):
    binary_text = "".join(format(ord(i), '08b') for i in data)
    binary_data = binary_text + '1'
    
    while (len(binary_data) % 512) != 448:
        binary_data += '0'

    binary_data += format(len(binary_text), '064b')

    H = [
        int(math.modf(math.sqrt(2))[0] * (2 ** 32)),
        int(math.modf(math.sqrt(3))[0] * (2 ** 32)),
        int(math.modf(math.sqrt(5))[0] * (2 ** 32)),
        int(math.modf(math.sqrt(7))[0] * (2 ** 32)),
        int(math.modf(math.sqrt(11))[0] * (2 ** 32)),
        int(math.modf(math.sqrt(13))[0] * (2 ** 32)),
        int(math.modf(math.sqrt(17))[0] * (2 ** 32)),
        int(math.modf(math.sqrt(19))[0] * (2 ** 32)),
    ]

    K = []
    count = 0
    i = 2
    while count < 64:
        if is_prime(i):
            K.append(int(math.modf(i ** (1/3))[0] * (2 ** 32)))
            count += 1
        i += 1

    chunks = [binary_data[i:i + 512] for i in range(0, len(binary_data), 512)]
    
    for chunk in chunks:
        # Create a message schedule array of 64 32-bit words
        M = [int(chunk[i:i + 32], 2) for i in range(0, 512, 32)]
        for i in range(16, 64):
            s0 = (right_rotate(M[i-15], 7) ^ right_rotate(M[i-15], 18) ^ (M[i-15] >> 3)) & 0xffffffff
            s1 = (right_rotate(M[i-2], 17) ^ right_rotate(M[i-2], 19) ^ (M[i-2] >> 10)) & 0xffffffff
            M.append((M[i-16] + s0 + M[i-7] + s1) & 0xffffffff)

        # Initialize working variables with current hash values
        a, b, c, d, e, f, g, h = H

        # Main compression loop
        for i in range(64):
            S1 = (right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)) & 0xffffffff
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + K[i] + M[i]) & 0xffffffff
            S0 = (right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)) & 0xffffffff
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xffffffff

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xffffffff

        # Add the compressed chunk to the current hash value
        H[0] = (H[0] + a) & 0xffffffff
        H[1] = (H[1] + b) & 0xffffffff
        H[2] = (H[2] + c) & 0xffffffff
        H[3] = (H[3] + d) & 0xffffffff
        H[4] = (H[4] + e) & 0xffffffff
        H[5] = (H[5] + f) & 0xffffffff
        H[6] = (H[6] + g) & 0xffffffff
        H[7] = (H[7] + h) & 0xffffffff

    # Produce final hash (concatenate the hash values into a single hex string)
    return ''.join(f'{x:08x}' for x in H)

def right_rotate(value, shift):
    return (value >> shift) | (value << (32 - shift)) & 0xffffffff

data = "hey"
hashed_value = sha256(data)
print(f"SHA-256 hashed value: {hashed_value}")
