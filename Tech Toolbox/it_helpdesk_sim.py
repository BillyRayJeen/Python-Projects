import sys

print("=============================")
print("    IT HELPDESK SIMULATOR     ")
print("=============================")
print("Welcome to the helpdesk simulator!")
print("")
print("This simulator will help you understand and tackle real life helpdesk issues that may occur.")
print("")
print("Are you ready to get started? (Y/N?)")

answer = input("Please enter Y/N: ").lower()

	if answer in ("y", "yes"):
        print("Starting simulator...")
    
    elif answer in ("n", "no"):
        print("Exiting application, goodbye!")
        sys.exit(0)

print("===============================")
print("      IT HELPDESK SYSTEM       ")
print("===============================")

print("1. Create new ticket")
print("2. View all tickets")
print("3. Update ticket")
print("4. Search tickets")
print("5. Exit")
print("")

choice = input("Please select an option")
	if choice == "1":
		print("You selected: Create new ticket")
	elif choice == "2":
    	print("You selected: View all tickets")
	elif choice == "3":
    	print("You selected: Update ticket")
	elif choice == "4":
    	print("You selected: Search tickets")
	elif choice == "5":
		print("You selected: Exit. Thank you for using the IT Helpdesk Simulator!")	sys.exit(0)