from dataclasses import dataclass


@dataclass(frozen=True)
class ElGamalPublicKey:
    p: int              # prime modulus
    g: int              # generator
    y: int              # public key = g^x mod p, where x is the private key