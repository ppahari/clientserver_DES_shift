def ask():
    """
    Ask for choice of Encryption
    :return: Choice
    """
    while 1:
        ip = raw_input("\n\nEnter your Choice of Encryption 1- Shift Cipher 2 - Des encryption : ")
        if ip in ('1' , '2'):
            return ip
            break
        else:
            print 'Invalid Entry! Try Again\n'

def ask_termination():
    """
    Ask whether to terminate the connection or not
    :return: y or any key pressed
    """
    while 1:
        ip = raw_input("\nPress Y to continue or any key to terminate the connection : ")
        if ip in ('y', 'Y'):
            ip = 'y'
            return ip
            break
        else:
            return ip