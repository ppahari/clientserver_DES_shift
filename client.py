# Client Module:

#  -> Creates Socket -> Establish Socket connection to server using port and ip
#  -> Sends the choice of encryption to server
#  -> If Des, performs Des encryption -> extracts hexstrings from the file and encrypts them, sends them to server
#  -> If Shift, generates key, ask for input text, encrypt them, and send it to server for decryption

# Importing necessary library
import random  # Import Random Module for random number generation
import socket  # Import socket module
import time    # Import Time Module, here we use for sleep function
from Ask.ask_choice import *  # Import Ask Choice module to execute the script sent by server
from Des.desEngine import *
from FileParser.fileExtractor import extract_file
from Shift.encryptor import encrypt  # import encryptor.py module to apply "encrypt" function to create ciphertext
from Shift.gen import generate    # Import gen.py module , it has "generate" function to generate K'=(a.k+b) % 52

s = socket.socket()         # Create a socket object
port = 1234                # Reserve a port for your service.

connected = False
# Try to connect to  server
while not connected:
    try:
        # Give your required IP of server host here, for now we used local host 127.0.0.1
        s.connect(('127.0.0.1', port))
        connected=True
    except Exception as e:
        pass

# Display 'Connection Established' Acknowledgment
print s.recv(1024)

while 1:
    a= s.recv(1024)   # Client Receives the execution command for the choice of encryption
    exec(a)           # Client executes the command received from server
    s.send(resp)      # Client responses to server

    if resp == '1':   # Shift Cipher
        print '\n\n ********************** SHIFT CIPHER *********************************\n\n'
        # Infinite Loop
        while True:
            # Generates Random Number 1 <= K <= 1000,000
            ranNum=random.randint(1,1000000)
            # Generates Shift Number K'= (a.k+b)%52 where a=250 and b= 479
            r= generate(ranNum)
            # Checks if generated shift number (K') is 0, if its 0 continues the loop else breaks the loop
            if r != 0:
                break

        print "\nClient Generated Random Number ( K ) = ",ranNum
        print "\nClient Generated Shift Number (K') = ", r

        print "\nStatus: Sending Random Number To Server..."

        time.sleep(3)
        # Sends Random Number (K) to server
        s.send(str(ranNum)) #Convers inteeger ranNum to string to send to socket
        # Receives Acknowledgement Form Server
        print s.recv(1024)

        time.sleep(3)

        # Asking for input of plaintext
        plaintext=raw_input('\nEnter your text to be encrypted:\n')

        # Printing Input Plaintext
        print "\n----------Plain Text----------\n"
        print plaintext
        print "-------------------------------"

        print "\nStatus: Generating Ciphertext...\n"
        time.sleep(3)

        # Generating Ciphertext from input plaintext
        ciphertext = encrypt(r,plaintext)

        print "\n----------CipherText----------\n"

        # Displaying Ciphertext
        print ciphertext
        print "-------------------------------"

        print "\nStatus: Sending CipherText To Server..."
        time.sleep(2)
        # Sending Ciphertext to Server
        s.send(ciphertext)

        # Receive Acknowledgment
        print s.recv(1024)
        print '\n************************************************************\n'
    else:
        y = []
        print '\n\n**************** DES ENCRYPTION ****************************\n\n'
        while 1:
            file = raw_input("Enter The file Name:  ")
            hexstr = extract_file(file)
            if hexstr:
                break
            else:
                print "Invalid File Path"
        while 1:
            # Hardcoding shared key here
            key = 'C30950FA36CF58CF'
            # key = raw_input("Enter the key to encrypt:  ") # If you want to input key, activate this command
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
        print "\nStatus: Generating Ciphertext...\n"
        time.sleep(3)
        print '----Plaintext----' + ':' + '---Ciphertext---\n'
        # Encrypts the plain text block by block
        for i in range(0, len(hexstr)):
            y.append(des_encrypt(hexstr[i], key))
            print hexstr[i] + ' : ' + y[i]
        print "\nStatus: Sending Ciphertext to Server...\n"
        # Sends the number of blocks of cipher to server
        s.send(str(len(y)))
        # Sends the cipher blocks to server
        for i in range(0, len(y)):
            s.send(y[i])
            print 'Sent Cipher Block: %d' % i
            # Wait to send another frame until acknowledgment is received
            while int(s.recv(256)) != i:
                pass
        print s.recv(1024)
        print '\n************************************************************\n'

    print '\nStatus: Waiting...\n'
    end = s.recv(1024)   # Client Receives the execution command for the choice of quit or continue
    exec(end)           # Client executes the command received from client
    s.send(end_resp)      # Client sends the response to client's command

    if end_resp != 'y':
        break

s.close
print "\nStatus: Connection Terminated! "

