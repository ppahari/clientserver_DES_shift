alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encrypt(r, text):
    """ Generates ciphertext from input plaintext
    :param r: Shift Number as K'
    :param text: Input Text
    :return: result as Ciphertext
    """
    res = ''
    for letter in text:
        try:
            encrypt_index = (alphas.index(letter) + r) % 52
            res += alphas[encrypt_index]
        except ValueError:
            res += letter
    return res
