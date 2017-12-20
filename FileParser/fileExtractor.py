import os.path


def extract_file(file):
    """
    :param file: File name with correct path from which 16 Hex String needs to parsed
    :return: returns list of 16 Hex String
    """
    # Checks if file exists
    status = os.path.exists(file)
    if status:
        # #Opens file
        f = open (file,'r')
        b = []
        hexstrings = []
        # Read each line in loop
        for line in f:
            # Splits the strings into list seperated by spaces
            a = line.split(' ')
            for i in range(0, len(a)):
                b.append(a[i][0:16])
        f.close()

        # Checks if the parsed file is hex strings or not, if not ignores them and returns only hexstrings of length 16
        for i in range(0,len(b)):

            try:
                int(b[i],16)
                flag = True
            except ValueError:
                flag = False
            if len(b[i]) == 16 and flag:
                hexstrings.append(b[i])
        return hexstrings
    else:
        return status
