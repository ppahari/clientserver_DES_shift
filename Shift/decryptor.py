alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def decrypt(r, cipher):
    """
    Decrypts ciphertext to plaintext
    :param r: Shift Index
    :param cipher: Ciphertext to be decrypted
    :return: Plaintext
    """
    res = ''

    for letter in cipher:
        try:
            decrypt_index = (alphas.index(letter) - r) % 52
            res += alphas[decrypt_index]
        except ValueError :
            res += letter
    return res
