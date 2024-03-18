# https://cryptopals.com/sets/1/challenges/5
import numpy as np
plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

# XOR each byte of the plaintext with the corresponding byte of the key. Repeat the key if necessary.
# ord() returns the Unicode code point for a one-character string.
# ord('A') = 65. chr(65) = 'A'.
ciphertext = ""
for i in range(len(plaintext)):
    ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))

if __name__ == '__main__':
    assert ciphertext.encode().hex() == ('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a'
                                         '282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
