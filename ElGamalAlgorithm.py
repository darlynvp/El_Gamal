from random import random
from typing import Tuple
from ElGamalPrivateKey import ElGamalPrivateKey
from ElGamalPublicKey import ElGamalPublicKey
import KeyGeneration


def encrypt(plaintext: int, public_key: ElGamalPublicKey) -> Tuple[int, int]:
    """
    Encrypts a plaintext message using the ElGamal encryption algorithm.

    :param plaintext: The message to be encrypted, represented as an integer.
    :param public_key: The recipient's public key, which includes the prime modulus (p), generator (g), and public key (y).
    :return: A tuple containing the ciphertext components (c1, c2).
    """
    p = public_key.p
    g = public_key.g
    y = public_key.y

    # Step 1: Choose a random integer k in the range [1, p-2]
    k = random.randint(1, p - 2)

    # Step 2: Compute c1 = g^k mod p
    c1 = pow(g, k, p)

    # Step 3: Compute c2 = (y^k * plaintext) mod p
    c2 = (pow(y, k, p) * plaintext) % p

    return c1, c2

def decrypt(ciphertext: Tuple[int, int], private_key: ElGamalPrivateKey) -> int:
    """
    Decrypts a ciphertext message using the ElGamal decryption algorithm.

    :param ciphertext: A tuple containing the ciphertext components (c1, c2).
    :param private_key: The recipient's private key, which includes the prime modulus (p) and private key (x).
    :return: The decrypted plaintext message as an integer.
    """
    c1, c2 = ciphertext
    p = private_key.p
    x = private_key.x

    # Step 1: Compute s = c1^x mod p
    s = pow(c1, x, p)

    # Step 2: Compute the modular inverse of s modulo p
    s_inv = KeyGeneration.mod_inverse(s, p)

    # Step 3: Compute plaintext = (c2 * s_inv) mod p
    plaintext = (c2 * s_inv) % p

    return plaintext


def main():
    # Generate keys
    public_key, private_key = KeyGeneration.generate_keys()

    # Example plaintext message (as an integer)
    plaintext = 12345

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, public_key)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_plaintext = decrypt(ciphertext, private_key)
    print(f"Decrypted plaintext: {decrypted_plaintext}")

if __name__ == "__main__":
    main()