import socket
import subprocess

print("=========================================")
print("      NETWORK TROUBLESHOOTER")
print("=========================================")

#Finding users Computer name and IPV4 Address

computer_name = socket.gethostname()
computer_ip = socket.gethostbyname(computer_name)
print("Computer name", computer_name)
print("Computer IP:", computer_ip)

#Testing connection

print("Testing connection")
    
connection = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)
    
if connection.returncode == 0:
    print("Internet connection: Successful")
else:
    print("Internet connection: Failed")
    
#Input of website or IP address

hostname = input(" Please enter a website or IP address: ")

print("You entered:", hostname)

try:
    ip_address = socket.gethostbyname(hostname)
    print("IP address:", ip_address)
    print("Testing connection...")
    result = subprocess.run(["ping", "-n", "1", hostname],capture_output=True,text=True)
    if result.returncode == 0:
        print("Connection successful!")
        ping_result = result.stdout.split("Maximum =")
        Maximum = ping_result[1].split(",")
        print("Ping:", Maximum[0])
    
    else:
        print("Connection failed.")

except socket.gaierror:
    print("DNS Lookup failed")
    print("Could not find valid address.")
