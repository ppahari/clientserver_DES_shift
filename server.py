# Server Module:

#  -> Creates Socket using socket.socket() and binds to ip and port using s.bind() function
#  -> Listens to clients request using s.client()
#  -> Accepts the client request using s.accept() -> Sends Connection Established Acknowledgment
#  -> Requests for choice of encryption to client
#  -> If Des, receives blocks of cipher from clients, decrypts them to generate plaintext
#  -> If Shift, receives ciphertext from client, decrypts to generate plaintext

# Importing necessary library
import socket  # Socket Library
import time
from Shift.decryptor import decrypt
from Shift.gen import generate
from Des.desEngine import des_decrypt



# Creating a socket object
s=socket.socket()
print "\nStatus: Socket Created!"

# Reserve a port number
port = 1234
s.bind(('',port))
print "Status: Socket binded to port: ", port

# Socket on listening mode
print 'Status: Listening...'
s.listen(5)

# Accepts the request from client
c, addr = s.accept()
print 'Status:Got connected from',addr

# Sends Connection Acknowledgment
c.send('\n*****Acknowledgment :Connection Established*****')

while 1:
    c.send("resp=ask()")
    client_response = c.recv(1024)

    if client_response == '1':    # ----------------------Shift Cipher--------------------------------------
        print " \n\n\n********** Client Choice is Shift Cipher ****************************\n\n\n "
        # Receive RandomNumber K
        ranNum = int(c.recv(1024))  # Convert received string into integer
        print "\nRandom Number received from client (K)= ", ranNum

        # Server Sends Acknowledgment
        c.send('*****Acknowledgment: Server Received Random Number K*****\n ')

        # Server generates shift Number K'
        r = generate(ranNum)
        print ('\nStatus: Generating Shift Number K\' using Random Number K...')
        time.sleep(3)
        print "\nServer Generated Shift Number (K') = ", r

        print "\nStatus: Waiting..."
        time.sleep(3)

        # Receive Ciphertext Received
        ciphertext = c.recv(4096)
        print "\nStatus: CipherText Received!"

        time.sleep(2)

        # Sending Acknowledgment to client
        c.send('\n*****Acknowledgment: CipherText Received by server***** \n')

        print '\nStatus: Now Decrypting the Ciphertext to PlainText... \n'
        time.sleep(3)
        # Decrypts ciphertext into plaintext
        plaintext=decrypt(r,ciphertext)
        print "\nStatus: CipherText Decrypted, Generated Plaintext!"

        # Display CipherText
        print "\n----------CipherText---------\n"
        print ciphertext
        print "-------------------------------"

        # Display Plaintext
        print "\n----------Plain Text---------\n"
        print plaintext
        print "-------------------------------"
        print '\n************************************************************\n'

    else:    # -------------------------- DES Encryption ----------------------------------------------
        cipher = []
        print " \n\n************** Client Choice is DES ************************\n\n "
        print "Status: Waiting...\n"
        # Receives the number of cipher block it 's to receive from client
        length = int(c.recv(1024))
        # Receives Cipher block from client
        for i in range(0, length):
            data = c.recv(256)
            cipher.append(data)
            # Sends acknowledgment to client
            c.send(str(i))
            print 'Received Cipher Block: %d' %i
        time.sleep(2)
        c.send('\n*****Acknowledgment: All blocks of Cipher Received by server***** \n')
        print "\n*****Acknowledgment : Blocks of Cipher Received from client*******\n"
        while 1:
            # Hardcoding key here
            key = 'C30950FA36CF58CF'
            # key = raw_input("Enter the key to decrypt:  ") # If you want to input key, activate this command
            # Checks if key is 16 length hexdigits
            try:
                int(key,16)
                status = True
            except ValueError:
                status = False
            if len(key) == 16 and status:
                break
            else:
                print "Invalid Key"

        print '\nStatus : Generating Plaintext from cipher received from client...\n'
        time.sleep(3)
        print '----Ciphertext---' + ':' + '---PlainText---\n'
        for i in range(0,len(cipher)):
            # Decrypts the cipher received from client
            x = des_decrypt(cipher[i], key)
            print cipher[i] + ' : ' + x
        print '\n************************************************************\n'

    c.send("end_resp=ask_termination()")
    print '\nStatus Waiting...\n'
    client_end_response = c.recv(1024)
    if client_end_response != 'y':
        break

# Close the connection
c.close()
s.close()
print "\nStatus: Connection Terminated!"
