#Since this is an educational project for my self, I followed tutorials (both written and on YouTube) to create this tool.
#Since I am a beginner basically every bit is commented as some kind of documentation for me.(How does is work?:)
#Simple Password Generator
#DO NOT USE FOR REAL PASSWORDS
#This is for educational purposes only
print("\n##Password Generator##\n") #Print the title of the tool in a new line by using \n

while True: 
    Length_Password=input("Please enter the length of the password: ")
    Length_Password=Length_Password.strip()#Remoce white spaces (for example spacebar inputs by user)
    if Length_Password.isnumeric and Length_Password.isdigit() and Length_Password !="0": #Check if the input given by the user is a number and not 0.ö
        break #Breaks the current loop if the conditions are true
    else:
        print ("Please enter a number greater than 0.")#inform user that the input is not valid

print("1:I want my password to only contain letters and numbers")
print("2:I want my password to contain only numbers")
print("3I want my password to contain letters, numbers and symbols")


while True:
    #Ask user to enter the complexity of the password
    #Define user input is Complexity_Password
    Complexity_Password=input("Please choose the complexity of your password:")
    Complexity_Password=Complexity_Password.strip()#Remoce white spaces (for example spacebar inputs by user)
    if Complexity_Password in ["1","2","3"]:#Give a list of valid options.by using in operator.
        break
    else:
        print("\n Please enter a valid option (choose 1,2 or 3)\n")