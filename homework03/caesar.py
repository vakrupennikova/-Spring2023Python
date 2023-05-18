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
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    caes = alp[shift: 26] + alp[:shift] \
        + alp[26 + shift: 52] + alp[26: 26 + shift] \
        + alp[52 + shift: 85] + alp[52: 52 + shift] \
        + alp[85 + shift:] + alp[85: 85 + shift]
    alp += ' ,-'
    caes += ' ,-'
    alp_in_caes = str.maketrans(alp, caes)
    ciphertext = plaintext.translate(alp_in_caes)

    return ciphertext


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

    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    caes = alp[shift: 26] + alp[:shift] \
        + alp[26 + shift: 52] + alp[26: 26 + shift] \
        + alp[52 + shift: 85] + alp[52: 52 + shift] \
        + alp[85 + shift:] + alp[85: 85 + shift]
    alp += ' ,-'
    caes += ' ,-'
    caes_in_alp = str.maketrans(caes, alp)
    plaintext = ciphertext.translate(caes_in_alp)
    return plaintext


def caesar_breaker(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    >>> d = {"python", "java", "ruby"}
    >>> caesar_breaker("python", d)
    0
    >>> caesar_breaker("sbwkrq", d)
    3
    """
    best_shift = 0
    plaintext = ''
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    while plaintext not in dictionary:
        caes = alp[best_shift: 26] + alp[:best_shift] \
            + alp[26 + best_shift: 52] + alp[26: 26 + best_shift] \
            + alp[52 + best_shift: 85] + alp[52: 52 + best_shift] \
            + alp[85 + best_shift:] + alp[85: 85 + best_shift]
        caes_in_alp = str.maketrans(caes, alp)
        plaintext = ciphertext.translate(caes_in_alp)
        best_shift += 1
    return best_shift - 1
