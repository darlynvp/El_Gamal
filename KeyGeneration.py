import secrets

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find gcd and coefficients.
    :param a: First integer.
    :param b: Second integer.
    :return: A tuple (gcd, x, y) such that ax + by = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
    return gcd, x, y

# Modular Exponentiation: a^b mod m
def mod_exp(a, b, m):
    """
    Compute (a^b) mod m using exponentiation by squaring.
    :param a: The base.
    :param b: The exponent.
    :param m: The modulus.
    :return: The result of (a^b) mod m."""
    a = a % m
    result = 1

    while b > 0:
        if b % 2 == 1:  # If b is odd, multiply a with result
            result = (result * a) % m
        a = (a * a) % m  # Square a
        b = b >> 1      # Divide b by 2 (shift exponent right)
        
    return result


# Modular Inverse: x^-1 mod q
def mod_inverse(x, q):
    """
    Compute modular inverse of x modulo q using Extended Euclidean Algorithm.
    :param x: The number for which to find the inverse.
    :param q: The prime modulus.
    :return: The modular inverse of x under modulo q.
    """
    g, inv, _ = extended_gcd(x, q)

    if g != 1:
        raise ValueError(f"No modular inverse for {x} under modulo {q} since gcd is {g}.")
    
    return inv % q

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