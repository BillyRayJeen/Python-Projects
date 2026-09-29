import socket

print("=========================================")
print("			NETWORK TROUBLESHOOTER")
print("=========================================")

hostname = input(" Please enter a website or IP adress: ")

print("You entered:", hostname)

try:
	ip_adress = socket.gethostbyname(hostname)
	print("IP adress:", ip_adress)

except socket.gaierror:
	print("Could not find valid adress.")
	
