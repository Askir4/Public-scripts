#Simple Password Generator
#DO NOT USE FOR REAL PASSWORDS
#This is for educational purposes only
print("\n##Password Generator##\n")
#Ask user to enter the length of the password
#Define user input is Length_Password
while True: 
    Length_Password=input("Please enter the length of the password: ")
    Length_Password=Length_Password.strip()
    if Length_Password.isnumeric and Length_Password.isdigit() and Length_Password !="0":
        break
    else:
        print ("Please enter a number greater than 0.")

print("1:I want my password to only contain letters and numbers")
print("2:I want my password to contain only numbers")
print("3I want my password to contain letters, numbers and symbols")


while True:
    #Ask user to enter the complexity of the password
    #Define user input is Complexity_Password
    Complexity_Password=input("Please choose the complexity of your password:")
    Complexity_Password=Complexity_Password.strip().lower()
    if Complexity_Password in ["1","2","3"]:
        break
    else:
        print("\n Please enter a valid option (choose 1,2 or 3)\n")