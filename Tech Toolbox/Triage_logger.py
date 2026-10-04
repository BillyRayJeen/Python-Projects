print("===============================")
print("         TRIAGE LOGGER         ")
print("===============================")

Log = input(" Please enter your related issue, try limit this to as short as possible :")

print("You entered:", Log)

Error_description = input ("Please explain in further detail, what is the current issue with your device and when and what task you were doing when the issue occured :")
print("You entered:", Error_description)

if "Password" in Log:
    print("Low_impact")
    impact = ("low_impact")
elif "WI-FI" in Log:
    print("Medium_impact")
    impact = ("medium_impact")
elif "Crash" in Log:
    print("High_impact")
    impact = ("high_impact")
elif "Bluescreen" in Log:
    print("Emergency")
    impact = ("emergency")
    
if impact == "low_impact":
	print("Thank you, we will resolve this as soon as possible!")

elif impact == "medium_impact":
    print("Thank you, we will resolve this as soon as possible!")

elif impact == "high_impact":
    print("We have notified an engineer, they will be with you shortly")

elif impact == "emergency":
    print("This is our top priority and we will resolve this as quickly as possible")

print("===============================")        
print("[         YOUR REPORT         ]")
print("===============================")    

print(Log)
print(Error_description)

