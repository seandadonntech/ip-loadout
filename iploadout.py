from socket import gethostbyname
import os
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("The host name of this computer/machine is" + hostname )
print("Your Computer IP Address is:  " + IPAddr)

we = input("Please enter website address:\n")

# IP lookup from hostname
print(f'The {we} IP Address is {socket.gethostbyname(we)}')
