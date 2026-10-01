import socket
import subprocess

print("=========================================")
print("      NETWORK TROUBLESHOOTER             ")
print("=========================================")

#Find user's computer name and IPV4 Address

computer_name = socket.gethostname()
computer_ip = socket.gethostbyname(computer_name)
print("[  SYSTEM INFORMATION  ]")

print("Computer name :", computer_name)
print("Local IPv4 :", computer_ip)

#Testing connection
print("[  CONNECTION CHECK  ]")

print("Testing connection...")
    
connection = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)
    
if connection.returncode == 0:
    print("Internet connection: Successful")
else:
    print("Internet connection: Failed")
    
#Get website or IP address from user

while True:
    print("[  IP Address/ Website Diagnosis  ]")
    hostname = input(" Please enter a website or IP address: ")

    print("You entered:", hostname)

    try:
        ip_address = socket.gethostbyname(hostname)
        print("[  WEBSITE INFORMATION  ]")

        print("IP address:", ip_address)
        print("Testing connection...")
        result = subprocess.run(["ping", "-n", "1", hostname],capture_output=True,text=True)
        if result.returncode == 0:
            print("Connection successful!")
            ping_result = result.stdout.split("Maximum =")
            maximum_ping = ping_result[1].split(",")
            print("Ping:", maximum_ping[0])
    
        else:
            print("Connection failed.")

    except socket.gaierror:
        print("DNS LOOKUP FAILED")
        print("COULD NOT FIND VALID ADDRESS.")

    choice = input("Test another address? (Y/N): ")
    if choice.lower() == "n":
        print("Thank you for using this tool!")
        break
