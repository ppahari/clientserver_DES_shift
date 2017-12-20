

------------------------------- Running On Same Computer -------------------------------------------------------------------------------------------------------------

-> Open two Terminal on the same computer , one for client and another for server  

-> Change directory of both terminal to path of 'src'  folder which contains all the python modules 

-> Run Server from terminal using command:  python server.py  

-> Run Client from second terminal using command:  python client.py 

-> Both Client and Server runs as expected

----------------------------------------------------------------------------------------------------------------------------------------------------------------------


--------------------------------Running on Different Computer ---------------------------------------------------------------------------------------------------------
-> Open terminal at both the computer
-> Edit client.py , and change the parameter of IP in function " s.connect(('127.0.0.1', port)) " with the IP of another computer 
   i.e.    " s.connect(('IP of Server Computer',port))  " , then save client.py

-> Run Server from server computer terminal using command:  python server.py

-> Run client.py from another computer as client terminal using command:  python client.py 

-> Both Client and Server Runs as expected

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note: There are sample hex files in sample folder. Give the folder path in the entry as :  for e.g :     sample/hex.txt

----------------------------------------------------------------------------NOTE---------------------------------------------------------------------------------------



All the source code modules are well commented and documented

P.S: Please See the Programming Project Problem Statement

------------------------------------------------------------------------------------------------------------------------------------------------------------------
