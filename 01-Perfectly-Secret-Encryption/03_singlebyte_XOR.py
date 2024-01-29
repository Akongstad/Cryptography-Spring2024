if __name__ == '__main__':
    # Find plaintext
    enc_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    dict = {}

    # Brute force: for all ascii characters, XOR with ciphertext
    for i in range(256):
        key = chr(i)
        decoded_msg = bytes.fromhex(enc_hex).decode()
        dec = [chr(i ^ ord(c)) for c in decoded_msg]  # XOR the the key with each byte char in the ciphertext
        dict[key] = dec

    # Find the plaintext with the highest score.
    # Method: If c in "etaoin shrdlu", then score += 1. (Most used characters in English language)
    max_score = 0
    max_key = chr(0)
    max_plaintext = []

    for key, plaintext in dict.items():
        score = 0
        for c in plaintext:
            if c in "etaoin shrdlu":
                score += 1
        if score > max_score:
            max_score = score
            max_key = key
            max_plaintext = plaintext

    print("score=" ,max_score,"key=", max_key, "plaintext=", ''.join(max_plaintext))
