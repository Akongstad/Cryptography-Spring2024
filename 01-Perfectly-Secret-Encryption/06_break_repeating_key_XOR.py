# https://cryptopals.com/sets/1/challenges/6
import base64

import numpy as np


def distance(s1, s2):
    """Hammer distance between s1 and s2"""
    # XOR each byte of the two strings and count the number of 1s in the result
    # Fill to fit the length of the longer string
    length = max(len(s1), len(s2))
    s1 = s1.ljust(length, b'\x00')
    s2 = s2.ljust(length, b'\x00')

    # 1s will be all bits that are different
    diff = 0
    for i in range(length):
        diff += bin(s1[i] ^ s2[i]).count('1')
    return diff


def best_plaintext(ciphertext):
    # Create a dictionary to store potential plaintexts
    plaintexts = {}
    # Brute force: XOR each ascii character with the ciphertext
    for i in range(126):
        key = chr(i)
        # XOR the key with each byte in the ciphertext
        dec = [chr(i ^ c) for c in ciphertext]
        plaintexts[key] = dec

    # Find the plaintext with the highest score
    # +1 for each character in "etaoin shrdlu"
    max_score = 0
    max_key = chr(0)
    max_plaintext = []

    for key, plaintext in plaintexts.items():
        score = 0
        for c in plaintext:
            if c in "etaoin shrdlu":
                score += 1
        if score > max_score:
            max_score = score
            max_key = key
            max_plaintext = plaintext

    return max_score, max_key, ''.join(max_plaintext)


if __name__ == '__main__':
    str1 = 'this is a test'
    str2 = 'wokka wokka!!!'
    assert distance(str1.encode(), str2.encode()) == 37

    # Read in the base64 encoded ciphertext from the file
    with open('data/06_data.txt', 'r') as file:
        ciphertext = file.read()
    ciphertext = base64.b64decode(ciphertext)

    candidates = {}  # keysize -> normalized_hammer

    for i in range(2, 41):
        # create blocks of size i
        block1 = ciphertext[:i]
        block2 = ciphertext[i:2 * i]
        block3 = ciphertext[2 * i:3 * i]
        block4 = ciphertext[3 * i:4 * i]
        normalized_hammer1 = distance(block1, block2) / i
        normalized_hammer2 = distance(block2, block3) / i
        normalized_hammer3 = distance(block3, block4) / i
        normalized_hammer_avg = (normalized_hammer1 + normalized_hammer2 + normalized_hammer3) / 3
        candidates[i] = normalized_hammer_avg

    print("Top 3 candidates:")
    top_3 = sorted(candidates.items(), key=lambda x: x[1])[:3]
    for i in range(3):
        print("keysize=", top_3[i][0], "normalized_hammer=", top_3[i][1])

    KEYSIZE = max(top_3, key=lambda x: x[1])[0]
    print("KEYSIZE=", KEYSIZE)

    # Break the ciphertext into blocks of KEYSIZE length
    blocks = [ciphertext[i:i + KEYSIZE] for i in range(0, len(ciphertext), KEYSIZE)]
    # Transpose the blocks
    blocks_T = [b"" for _ in range(KEYSIZE)]
    for block in blocks:
        for i in range(KEYSIZE):
            if i < len(block): # Last block will be smaller
                blocks_T[i] += bytes([block[i]]) # append the i-th byte of the block to the i-th block
    assert blocks != blocks_T
    # Assert shape
    assert len(blocks) == len(blocks_T[0])
    assert len(blocks_T) == KEYSIZE
    assert len(blocks[0]) == len(blocks_T)


    # solve each block as if it was single-byte XOR
    # The key that produces the best histogram is the repeating-key XOR key
    key = ""
    for block in blocks_T:
        _, k, _ = best_plaintext(block)
        key += k
    print("key=", key)

    # Decrypt the ciphertext with the key
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ciphertext[i] ^ ord(key[i % KEYSIZE]))
    print("plaintext=", plaintext)
