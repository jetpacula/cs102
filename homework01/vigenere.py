def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    ciphertext = ""

    for i in range(len(plaintext)):
        if keyword[i % len(keyword)].isupper():
            shift = ord(keyword[(i % len(keyword))]) - 65
        else:
            shift = ord(keyword[(i % len(keyword))]) - 97
        if plaintext[i].isupper():
            ciphertext += chr(((ord(plaintext[i]) + shift - 65) % 26) + 65)
        elif plaintext[i].islower():
            ciphertext += chr(((ord(plaintext[i]) + shift - 97) % 26) + 97)
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if keyword[i % len(keyword)].isupper():
            shift = ord(keyword[(i % len(keyword))]) - 65
        else:
            shift = ord(keyword[(i % len(keyword))]) - 97
        if ciphertext[i].isupper():
            plaintext += chr(((ord(ciphertext[i]) - shift - 65) % 26) + 65)
        elif ciphertext[i].islower():
            plaintext += chr(((ord(ciphertext[i]) - shift - 97) % 26) + 97)
        else:
            plaintext += ciphertext[i]
    return plaintext
