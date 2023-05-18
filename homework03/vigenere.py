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
    keyword = keyword.lower()

    i = 0
    while len(keyword) < len(plaintext):
        keyword += keyword[i : i + 1]
        i += 1

    ciphertext = ''

    for j in range(len(plaintext)):
        border = 123
        if plaintext[j].isupper():
            border = 91
        if not plaintext[j].isalpha():
            ciphertext += plaintext[j]
            continue
        if ord(plaintext[j]) + ord(keyword[j]) % 97 < border:
            letter = chr(ord(plaintext[j]) + ord(keyword[j]) % 97)
        else:
            letter = chr((ord(plaintext[j]) + ord(keyword[j]) % 97) - 26)
        ciphertext += letter
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
    keyword = keyword.lower()

    i = 0
    while len(keyword) < len(ciphertext):
        keyword += keyword[i : i + 1]
        i += 1

    plaintext = ''

    for j in range(len(ciphertext)):
        border = 96
        if ciphertext[j].isupper():
            border = 64
        if not ciphertext[j].isalpha():
            plaintext += ciphertext[j]
            continue
        if ord(ciphertext[j]) - ord(keyword[j]) % 97 > border:
            letter = chr(ord(ciphertext[j]) - ord(keyword[j]) % 97)
        else:
            letter = chr((ord(ciphertext[j]) - ord(keyword[j]) % 97) + 26)
        plaintext += letter
    return plaintext