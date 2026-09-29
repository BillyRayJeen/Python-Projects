import socket

print("=========================================")
print("			NETWORK TROUBLESHOOTER")
print("=========================================")

hostname = input("Enter a website or IP adress: ")
print("You entered:", hostname)
try:
	ip_adress = socket.gethostbyname(hostname)
    print("IP adress:", ip_adress)
except socket.gaierror:
	print("Could not resolve the hostname.")