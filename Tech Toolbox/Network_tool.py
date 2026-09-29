import socket

print("=========================================")
print("			NETWORK TROUBLESHOOTER")
print("=========================================")

hostname = input(" Please enter a website or IP address: ")

print("You entered:", hostname)

try:
	ip_address = socket.gethostbyname(hostname)
	print("IP address:", ip_address)

except socket.gaierror:
  print("DNS Lookup failed")
  print("Could not find valid address.")
	
