
# This is the module which houses all the units and subunits required to carry out DES encryption

# Initial Permutation Function before the rounds begins
ip = (58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7)

# Inverse Permutation function after the rounds completes
ip_inv = (40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25)


# --------------------Base Converters --------------------------------


def bin2hex(binstr):
    """
    Converts the binary string into hex string
    :param binstr: Input: binary string
    :return: returns the hex string
    """
    length = len(binstr)/4
    try:
        s = hex(int(binstr,2))
        s = s[2:s.index('L')]
    except ValueError:
        s = hex(int(binstr,2))
        s= s[2:]
    while len(s)!=length:
        s = '0'+s
    return s


def hex2bin(hexstr):
    """
    Convert hex string to binary string
    :param hexstr: Input: Hex String
    :return: Returns binary string
    """
    length = len(hexstr)*4
    binstr = bin(int(hexstr, 16))[2:]
    while len(binstr) < length:
        binstr = '0' + binstr
    return binstr
# ---------------------------------------------------------------------

# ---------------------------Permutation Function ------------------------


def permutate(binstr, perm_table):
    """
    This functions permutes the given binary string according to the given permutation table
    :param binstr: Input: Binary String
    :param perm_table: Input : Permutation Table
    :return: permuted binary string
    """
    perm = [binstr[i-1] for i in perm_table]
    perm = ''.join(perm)
    return perm
# --------------------------------------------------------------------------


# --------------------------Splitter function -------------------------------


def split_func(block,n):
    """
    Splits the given string into n size
    :param block: Input String
    :param n: Size
    :return: n size of string into lists
    """
    return [block[i:i+n] for i in range(0, len(block), n)]


def display(binstr,n):
    """
    Used for better visibility of long strings whose purpose to display the seperated string into n chunks
    This function is used just for testing purpose
    :param binstr:  string
    :param n: n size
    :return: n size of string as lists
    """
    a = [binstr[i:i+n] for i in range(0,len(binstr),n)]
    print '  '.join(a)
# -------------------------------------------------------------------------

# --------------------------------Binary string XOR function --------------------


def binxor(binstr1, binstr2):
    """
    Performs XOR Operation between two binary strings
    :param binstr1: Binary String 1
    :param binstr2: Binary String 2
    :return: Result of XOR between Binary String 1 and Binary String 2
    """
    result = [str(int(i) ^ int(j)) for i,j in zip(binstr1,binstr2)]
    return ''.join(result)


# -----------------------------------------------------------------------------

def sbox(binstr):
    """
    Carries out Substitution between 8 Sboxes
    :param binstr: Takes Binary String of 48 bit length as input
    :return: returns 32bit length of concatenated eight 4bit chunks of binary string with overall length of 32 bit size
    """

    # Houses 8 Sboxes
    sbox = [
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
         ],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
         ],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
         ],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
         ],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
         ],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
         ],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
         ],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
         ]
    ]
    output = []
    # Splits the binary string of 48 bit length into 6 bit chunks
    s = split_func(binstr,6)
    # Performs the substitution with 8 sboxes
    for i in range(8):
        row = int(s[i][0]+s[i][5], 2)
        column = int(s[i][1:5], 2)
        val = sbox[i][row][column]
        b = str(bin(val)[2:])
        while len(b)!=4:
            b='0'+b
        output.append(b)
    # print output
    return ''.join(output)


# --------------------------------------------------------------------------------------------------------------------


# -----------------------------Mangler Function------------------------------------------------------------------------

def mangler(r,key):
    """
    Performs the mangler function of DES
    :param r: 32 bit length right chunks of 64 bit initially permuted binary string
    :param key: 48 bit length of each round key
    :return: 32 bit binary string
    """
    # Expansion Function
    exp = [32, 1, 2, 3, 4, 5,
           4, 5, 6, 7, 8, 9,
           8, 9, 10, 11, 12, 13,
           12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29,
           28, 29, 30, 31, 32, 1]

    # Permutation Function after sbox substitutions
    perm = [16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25]

    # Expand the 32 bit binary string to 48 bit binary string using expansion function
    exp_r = permutate(r, exp)
    # display(exp_r,6)
    # Performs XOR operation between 48 bit expanded right chunk binary string and 48 bit binary string key
    r_xor_key = binxor(exp_r,key)
    # display(r_xor_key,6)
    # Performs the substitution function with 8 sboxes
    sbox_op = sbox(r_xor_key)
    # display(sbox_op,4)
    # Final permuation of mangler function for each round
    final_permutation = permutate(sbox_op,perm)
    # display(final_permutkeyation,4)
    return  final_permutation

# -------------------------------------------------------------------------------------------------------------------


# ---------------------Key Generator -------------------------------------------------------------------------------


def shifter(bitstr, n):
    """
    Takes the
    :param bitstr: Input : Binary string
    :param n: n is shift position
    :return: returns the shifted result of binary string
    """
    return bitstr[n:]+bitstr[:n]


def keygen(key):
    """
    Generates 48 bit binary key string for each round
    :param key: Input: 16 digit hex string
    :return: returns 48 bits binary key string
    """
    PC1 = (57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4)

    PC2 = (14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32)

    # Lists No of shift rotate for each round
    no_shift = [0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    # Convert the input 8 byte hexstring to binary string
    bin_key = hex2bin(key)
    # Initialises the original hexstring
    k = [bin_key]
    # Permutes the binary string with PC1 functions and generate only 56 bits, ignoring the eighth bit of each byte
    pc1_key = permutate(bin_key,PC1)
    # Split the 56 binary string into two half of each length of 28 bit binary string
    c,d = split_func(pc1_key,28)
    # Performs the shift operation for each rounf
    for i in range(1,17):
        c = shifter(c,no_shift[i]); d = shifter(d,no_shift[i])
        temp = c+d
        # print " %d : C0/D0 56-bit : " % i
        # display(temp)
        k.append(permutate(temp,PC2))
        # print '%d : (Key 48-bit)' % i
        # display(k[i])
    return k  # Returns the list of key calculated for each round

# ---------------------------------------------------------------------------------------------------------------------

# -------------------------DES Encryption function -------------------------------------------------------------


def des_encrypt(input,key):
    """
    It carries out the encryption function
    :param input: Plaintext- 16 digit hex string
    :param key: 16 digit hex string as key
    :return: returns the 16 digit hex string as encrypted ciphertext
    """
    # Converts the plain text hex string to binary string
    b = hex2bin(input)
    # Performs the initial permutation
    b_ip = permutate(b, ip)
    # Splits the binary string into two chunks - left as l and right as r - of size 32
    l, r = split_func(b_ip, 32)
    # Generates list of key for each round
    k = keygen(key)
    # Carries out 16 round operations for encryption
    for i in range(1, 17):
        # Saves temp variable for swapping the chunks
        temp = r
        # Performs the mangler function with right chunk as r and k[i] as key for the respective round i
        f = mangler(r, k[i])
        # Performs the xor operation between the result of mangler function and left chunk and is saved as right chunk
        r = binxor(f, l)
        # Swaps with right chunk which was saved as temp variable
        l = temp
    # In the end after 16 round right chunks is placed as left chunk and left as right chunk and concatenated together
    op = r+l
    # Carries out the inverse permutation function
    op_ip_inv = permutate(op, ip_inv)
    # display(op_ip_inv,8)
    # Converts the final encrypted binary string into hex digit as ciphertext
    y = bin2hex(op_ip_inv)
    # Returns the hex string y as ciphertext
    return y

# ------------------------------------------------------------------------------------------------------------------


def des_decrypt(input, key):
    """
    It carries out the decryption function
    :param input: Ciphertext- 16 digit hex string
    :param key: 16 digit hex string as key
    :return: returns the 16 digit hex string as decrypted plaintext
    """
    # Converts the Ciphertext hex string to binary string
    b = hex2bin(input)
    # Performs the initial permutation
    b_ip = permutate(b, ip)
    # Splits the binary string into two chunks - left as l and right as r - of size 32
    l,r = split_func(b_ip, 32)
    # Generates list of key for each round
    k = keygen(key)
    # Carries out 16 round operations for decryption - uses reverse key schedule
    for i in range(1, 17):
        # Saves temp variable for swapping the chunks
        temp = r
        # Performs the mangler function with right chunk as r and reverse key k[17-i] as key for the respective round i
        f = mangler(r, k[17-i])
        # Performs the xor operation between the result of mangler function and left chunk and is saved as right chunk
        r= binxor(f, l)
        # Swaps with right chunk which was saved as temp variable
        l = temp
    # In the end after 16 round right chunks is placed as left chunk and left as right chunk and concatenated together
    op = r+l
    # Carries out the inverse permutation function
    op_ip_inv = permutate(op, ip_inv)
    # display(op_ip_inv,8)
    # Converts the final decrypted binary string into hex digit as plaintext
    x = bin2hex(op_ip_inv)
    # Returns the hex string x as plaintext
    return x

# --------------------------------------------------------------------------------------------------------------------