
def extended_euclidean(a,b):
    # output: (d, X, Y) such that d = gcd(a,b) = aX + bY
    assert a >= b > 0
    # b divides a
    if a % b == 0:
        return b, 0, 1
    # Compute q,r with a = qb + r and 0 < r < b
    q = a // b
    r = a - q*b
    # Recurse
    d, X, Y = extended_euclidean(b, r)
    return d, Y, X - q*Y

if __name__ == '__main__':
    # Finding the invers of 14 mod 47 using the extended euclidean algorithm
    # Find X, Y such that 47X + 14Y = gcd(47,14) = 1
    a = 47
    b = 14
    d, X, Y = extended_euclidean(a, b)
    print(f"({a})*({X}) + ({b})*({Y}) = {d}")