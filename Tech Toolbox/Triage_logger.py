import random as Gen

print("===============================")
print("         TRIAGE LOGGER         ")
print("===============================")
User = input("Please enter your name: ")
Log = input(" Please enter your related issue, try limit this to as short as possible :").lower()

print("You entered:", Log)

Error_description = input ("Please explain in further detail, what is the current issue with your device and when and what task you were doing when the issue occured :")
print("You entered:", Error_description)

low_impact_keywords = ["password", "printer", "keyboard", "mouse"]
medium_impact_keywords = ["wi-fi", "wifi", "internet", "slow", "email"]
high_impact_keywords = ["crash", "not responding", "data loss"]
emergency_keywords = ["bluescreen", "server down", "security breach"]

if any(keyword in Log for keyword in low_impact_keywords):
    print("Low_impact")
    impact = ("low_impact")
elif any(keyword in Log for keyword in medium_impact_keywords):
    print("Medium_impact")
    impact = ("medium_impact")
elif any(keyword in Log for keyword in high_impact_keywords):
    print("High_impact")
    impact = ("high_impact")
elif any(keyword in Log for keyword in emergency_impact_keywords):
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
    
ticket_id = random.randint(1000,9999)

print("===============================")        
print("[         YOUR REPORT         ]")
print("===============================")

print("[User]", User_name)
print("[Ticket ID", ticket_id)   
print("[Issue]",Log)
print("[Description]",Error_description)
