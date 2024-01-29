# https://cryptopals.com/sets/1/challenges/4

def best_plaintext(ciphertext):
    dict = {}

    # Brute force: for all ascii characters, XOR with ciphertext
    for i in range(256):
        key = chr(i)
        try:
            decoded_msg = bytes.fromhex(ciphertext).decode() # What if we cannot decode?
        except:
            continue
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

    return max_score, max_key, ''.join(max_plaintext)

if __name__ == '__main__':
    candidates = {}
    for line in open('data/04_data.txt', 'r').readlines():
        candidates[line.strip()] = best_plaintext(line.strip())

    # Sort by score
    sorted_candidates = sorted(candidates.items(), key=lambda x: x[1][0], reverse=True)
    print("Top 5 candidates:")
    for i in range(5):
        print("score=", sorted_candidates[i][1][0], "key=", sorted_candidates[i][1][1], "plaintext=", sorted_candidates[i][1][2])