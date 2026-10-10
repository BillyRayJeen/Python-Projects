pip install psutil
import psutil
import platform
import socket

print("================================")
print("")
print("       PC HEALTH CHECKER        ")
print("") 
print("================================")

print("==================================")
print("       COMPUTER DETAILS          ")
print("==================================")

print("Computer:",platform.node())
print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Processor:", platform.processor())

def check_cpu():
	try:	
        	cpu_usage = psutil.cpu_percent(interval=1)
		print("CPU Usage:", cpu_usage, "%")
        	if cpu_usage > 90:
                print("WARNING: High CPU Usage")
            elif cpu_usage > 70:
                print("CPU usage elevated")
            else:
                print("CPU usage normal")
	except:
    	print("Unable to retrieve CPU information")

def check_ram():
	try:
    	ram_usage = psutil.virtual_memory()
		print("RAM Usage:", check_ram.percent, "%")
        except:
		print("Unable to retrieve RAM information") 

def check_disk():
    try:
		disk_usage = psutil.disk_usage("/")
		print("Disk Usage:", check_disk.percent, "%")
    except:
		print("Unable to retrieve disk information")

def check_connection():
	try:
        	socket.create_connection(("8.8.8.8",53), timeout=3)
                print("Internet: Connected")
        except OSError:
        	print("Interent: Unavailable")

                
check_cpu():
check_ram():
check_disk():
check_connection():
