from sympy import randprime

from ElGamalPrivateKey import ElGamalPrivateKey
from ElGamalPublicKey import ElGamalPublicKey
from typing import Tuple

def egcd(a, b):
    """Extended Euclidean Algorithm to find gcd and coefficients."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m."""
    gcd, x, _ = egcd(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return x % m


def find_prime(bits: int = 256) -> int:
    """Generate a prime number of specified bit length."""
    return randprime(2**(bits - 1), 2**bits)

def find_generator(p: int) -> int:
    """Find a generator for the multiplicative group of integers modulo p."""
    # For simplicity, we can use 2 as a generator for prime p > 2
    if p > 2:
        return 2
    raise ValueError("Prime must be greater than 2 to find a generator.")

def generate_keys(bits: int = 256) -> Tuple[ElGamalPublicKey, ElGamalPrivateKey]:
    """Generate ElGamal public and private keys."""
    p = find_prime(bits)
    g = find_generator(p)
    x = randprime(1, p - 1)  # Private key
    y = pow(g, x, p)          # Public key
    return ElGamalPublicKey(p, g, y), ElGamalPrivateKey(p, x)  # Return public and private keys as objects