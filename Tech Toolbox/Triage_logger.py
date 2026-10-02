print("===============================")
print("         TRIAGE LOGGER         ")
print("===============================")

Log = input(" Please enter your related issue:")

print("You entered:", Log)

if "Password" in Log:
    print("Low_impact")
elif "WI-FI" in Log:
    print("Medium_impact")
elif "Crash" in Log:
    print("High_impact")
elif "Bluescreen" in Log:
    print("Emergency")
    
if Log="Low_impact"
	print("Thank you, we will resolve this as soon as possible")