from itertools import cycle


def crypto_iter(fn, text: str, key: str) -> str:
    # check arguments
    if text == '' or not key.isalpha():
        return ''
    # encrypt or decrypt
    result = ''
    for ch, k in zip(text, cycle(key.upper())):
        if ch.isalpha():
            tmp_ch = chr(fn(ord(ch.upper()), ord(k)) % 26 + ord('A'))
            result += tmp_ch if ch.isupper() else tmp_ch.lower()
        else:
            result += ch

    return result


def encrypt(key: str, text: str) -> str:
    return crypto_iter(lambda ch, k: ch + k - 2 * ord('A'), text, key)


def decrypt(key: str, text: str) -> str:
    return crypto_iter(lambda ch, k: ch - k + 26, text, key)
