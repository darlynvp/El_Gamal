from typing import Tuple
from sympy import randprime
import KeyGeneration

def encrypt(plaintext, q, h, g):
    """
    Encrypts a plaintext message using the ElGamal encryption algorithm.

    :param plaintext: The message to be encrypted.
    :param q: The prime modulus.
    :param h: The recipient's public key.
    :param g: The generator.
    :return: A tuple containing the ciphertext components (c2, p).
    """
    # Convert plaintext to bytes for encryption
    msg_bytes = plaintext.encode('utf-8')

    k = KeyGeneration.generate_keys(q)      # ephemeral private key for sender (per message)
    s = KeyGeneration.mod_exp(h, k, q)      # shared secret = h^k mod q
    p = KeyGeneration.mod_exp(g, k, q)      # ephemeral public key = g^k mod q (aka ciphertext c1)

    # Encrypt the message using the shared secret: c2 = (s * msg_bytes) mod q
    c2 = [(b * s) % q for b in msg_bytes]

    return c2, p

def decrypt(ciphertext, p, x, q):
    """
    Decrypts a ciphertext message using the ElGamal decryption algorithm.

    :param ciphertext: A tuple containing the ciphertext components (c2, p).
    :param p: The prime modulus.
    :param x: The recipient's private key.
    :param q: The prime modulus.
    :return: The decrypted plaintext message as an integer.
    """
    # Receiver recomputes the shared secret: s = p^x mod q
    s = KeyGeneration.mod_exp(p, x, q)
    s_inv = KeyGeneration.mod_inverse(s, q)  # Compute the modular inverse of s

    # Decrypt the message: plaintext = (c2 * s_inv) mod q
    decrypted_bytes = bytes([(c * s_inv) % q for c in ciphertext])
    plaintext = decrypted_bytes.decode('utf-8')

    return plaintext

def main():
    msg = str(input("Enter a message to encrypt: "))

    # Generate a prime modulus q
    q = randprime(2**255, 2**256)  # Using a large prime for better security

    # Pick g in [2, q-2]
    g = KeyGeneration.generate_keys(q)

    # Receiver's private key
    priv_key = KeyGeneration.generate_keys(q)

    # Receiver's public key: h = g^x mod q
    h = KeyGeneration.mod_exp(g, priv_key, q)

    print(f"Public parameters: \nq (random prime)={q}, \ng (generator)={g}, \nh (public key)={h}")

    encrypted, p = encrypt(msg, q, h, g)
    print(f"Ciphertext: {encrypted}")
    print(f"Ephemeral Public Key (p): {p}")

    decrypted = decrypt(encrypted, p, priv_key, q)
    print(f"Decrypted message: {decrypted}")


if __name__ == "__main__":
    main()