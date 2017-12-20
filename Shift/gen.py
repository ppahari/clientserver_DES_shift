def generate(ranNum):
    """
    Generates K'= ((a*K)+b) % 52 where a=250 and b=479 and K is random Number from random.randint function
    :param ranNum: Random Numbers
    :return: ((a*ranNum) + b)% 52
    """
    a = 250
    b = 479
    r = ((a * ranNum)+b) % 52
    return r