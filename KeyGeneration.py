import secrets

def gcd(a, b):
    """Euclidean Algorithm to find gcd."""
    while b:
        a, b = b, a % b
    return a

# Modular Exponentiation: a^b mod m
def mod_exp(a, b, m):
    """Find the modular exponentiation of a under modulo m."""
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % m
        y = (y * y) % m
        b = b // 2
    
    return x % m

def mod_inverse(x, q):
    """Find the modular inverse of x under modulo q using Fermat's Little Theorem."""
    return mod_exp(x, q - 2, q)

def generate_keys(q):
    """
    Generate random key in [2, q-2].
    Uses secrets module for secure random number generation.
    :param q: The prime modulus.
    :return: A random key in the range [2, q-2].
    """
    if q <= 4:
        raise ValueError("q must be greater than 4 to generate a valid key.")

    key = secrets.randbelow(q - 3) + 2      # produces values 2, 3, ..., q-2
    return key