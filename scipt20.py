feet_inches = input("Enter feet and inches : ")

def parse(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inches = float(part[1])
    return {'feet' : feet, 'inches' :inches}

def convert (feet, inches):
    meters = feet * 0.3048 + inches * 0.0244
    return meters

    #return f"{feet} feet and {inches} is euql to {meters}"

parsed = parse(feet_inches)
result= convert(parsed['feet'], parsed['inches'])



print(f"{parsed['feet'] }feet and {parsed['inches']} is equal to {result}")
if result < 1:
    print ("small")
else:
    print("good")