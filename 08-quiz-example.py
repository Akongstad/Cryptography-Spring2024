# Counter example for proposed elgamal based encryption scheme
import random

q = 37861 # large prime
p = 2 * q + 1
g = 2
x = 12
h = pow(g, x)
m0 = 0
m1 = 123

# Encryption
r = random.randint(1, q-1)
c1 = pow(g, r)
c2 = (pow(h, r) + m0) % p
print(f"c2: {c2}")

r_p = random.randint(1, q-1)
c1_prime = pow(g, r_p)
c2_prime = (pow(h, r_p) + m1) % p
print(f"c2_prime: {c2_prime}")

# Decryption
m_decrypted = (c2 - pow(c1, x)) % p
m_decrypted_prime = (c2_prime - pow(c1_prime, x)) % p

print("Decrypted message:", m_decrypted)
print("Decrypted message prime:", m_decrypted_prime)

# Attack. Distingues m0, from m1 without x
