import random
import string

characters = string.ascii_letters + string.digits + "!@£$%^*"

print("============================")
print("  Username and Password sim    ")
print("=============================")

Username = "User" + str(random.randint(100, 999))
Password = "ExamplePassword1"

print("Current username:", Username)
print("Current password: *********")
reset = input("Reset password Y/N? :")

if reset == "Y":
	confirmation = input("Password will reset to default, continue Y/N? :")
	if confirmation == "Y":
		print("Resetting Password")
		Password = "".join(random.choice(characters) for _ in range(12))
		print("New Password:", Password)
	elif confirmation == "N": 
		print("Cancelling request")