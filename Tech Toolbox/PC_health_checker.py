pip install psutil
import psutil
import platform

print("================================")
print(“”)
print("       PC HEALTH CHECKER        ")
print(“”) 
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
		print(“RAM Usage:”, memory.percent, "%")
    except:
		print(“Unable to retrieve RAM information”) 
def check_disk():
    try:
		disk_usage = psutil.disk_usage("/")
		print("Disk Usage:", disk.percent, "%")
    except:
		print("Unable to retrieve disk information")