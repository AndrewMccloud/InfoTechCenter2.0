import random

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calls the value of gasLevelGauge Function
gasLevelIndidactor = gasLevelGauge()

# Create If-ELIF-ELSE statements the Comparative Operator == Equal To in order to display gas level messages
def gasLevelAlert():
    if gasLevelIndidactor == "Empty":
        print("   WARNING YOU ARE ON EMPTY\nCalling Emergency Contact")
    elif gasLevelIndidactor == "Low":
        print("      WARNInG\nYour gas tank is low on gas\nThe closest gasoline station is ")
    elif gasLevelIndidactor == "Quarter Tank":
        print("You have a quarter tank of gas left\nLook for a gas station to stop at")
    elif gasLevelIndidactor == "Half Tank":
        print("You have a Half tank of gas left\nYou have 126 miles to empty")
    elif gasLevelIndidactor == "Three Quarter Tank":
        print("You have Three quarter tank of gas left\nYou have 210 miles to empty")
    else:
     print("You have Full of gas left\nYou have 310 miles to empty")

# Call Functions Here
gasLevelAlert()

