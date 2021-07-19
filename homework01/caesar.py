import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """

    return "".join(
        [
            chr(((ord(i) + shift - 65) % 26) + 65)
            if i.isupper()
            else chr(((ord(i) + shift - 97) % 26) + 97)
            if i.islower()
            else i
            for i in plaintext
        ]
    )


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE

    return "".join(
        [
            chr(((ord(i) - shift - 65) % 26) + 65)
            if i.isupper()
            else chr(((ord(i) - shift - 97) % 26) + 97)
            if i.islower()
            else i
            for i in ciphertext
        ]
    )


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
