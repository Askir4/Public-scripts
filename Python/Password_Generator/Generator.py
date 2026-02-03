#Simple Password Generator
#DO NOT USE FOR REAL PASSWORDS
#This is for educational purposes only
print("##Password Generator##")

while True: 
    Length_Password=input("Please enter the length of the password: ")
    Length_Password=Length_Password.strip()
    if Length_Password.isnumeric and Length_Password.isdigit() and Length_Password !="0":
        break
    else:
        print ("Please enter a number greater than 0.")