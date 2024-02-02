# https://cryptopals.com/sets/1/challenges/4

def best_plaintext(ciphertext):
    # Create a dictionary to store potential plaintexts
    plaintexts = {}

    # Brute force: XOR each ascii character with the ciphertext
    for i in range(126):
        key = chr(i)
        try:
            decoded_msg = bytes.fromhex(ciphertext).decode()
        except:
            # If decoding fails, assume invalid ciphertext and continue
            continue
        # XOR the key with each byte character in the decoded message
        dec = [chr(i ^ ord(c)) for c in decoded_msg]
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
    candidates = {}
    # Read in ciphertexts from file
    for line in open('data/04_data.txt', 'r').readlines():
        # Strip any trailing whitespace and store the ciphertext and its potential plaintext in the dictionary
        candidates[line.strip()] = best_plaintext(line.strip())

    # Sort the candidates by score in descending order
    sorted_candidates = sorted(candidates.items(), key=lambda x: x[1][0], reverse=True)
    print("Top 3 candidates:")
    for i in range(3):
        print("score=", sorted_candidates[i][1][0], "key=", sorted_candidates[i][1][1], "plaintext=",
              sorted_candidates[i][1][2])
