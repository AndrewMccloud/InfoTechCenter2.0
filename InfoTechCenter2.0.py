import random

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
    # print(currentGasLevel)
    return currentGasLevel

# Create If-ELIF-ELSE statements using Comparative Operators to display gas level messages
def gasLevelAlert():
    if gasLevelGauge() == "Empty":
        print("        WARNIG\nYou have run out of gas\nCalling Emergency Contact")




gasLevelGauge()
gasLevelAlert()

