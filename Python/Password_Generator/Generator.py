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

print("1:I want my password to only contain letters and numbers")
print("2:I want my password to contain only numbers")
print("3I want my password to contain letters, numbers and symbols")
Complexity_Password=input("Please choose the complexity of your password:")
Complexity_Password=Complexity_Password.strip().lower()

while True:
    if Complexity_Password=="1" or Complexity_Password=="2" or Complexity_Password=="3":
        break
    else:
        print("Please enter a valid option (choose 1,2 or 3)")