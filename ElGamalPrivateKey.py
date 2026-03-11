from dataclasses import dataclass

@dataclass(frozen=True)
class ElGamalPrivateKey:
    p: int              # prime modulus
    x: int              # private key, a random integer in the range [1, p-2]