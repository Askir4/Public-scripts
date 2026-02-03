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

print("\nThe following options are available:\n")
print("1: I want my password to contain only numbers")
print("2: I want my password to contain only lower letters")
print("3: I want my password to contain only upper letters")
print("4: I want my password to contain lower and upper letters")
print("5: I want my password to contain letters and numbers")
print("6: I want my passwort to contain only symbols")
print("7: I want my password to contain numbers and symbols")
print("8: I want my password to contain letters and symbols")
print("9: I want my password to contain letters, numbers and symbols")

while True:
    #Ask user to enter the complexity of the password
    #Define user input is Complexity_Password
    Complexity_Password=input("\nPlease choose the complexity of your password:")
    Complexity_Password=Complexity_Password.strip()#Remoce white spaces (for example spacebar inputs by user)
    if Complexity_Password in ["1","2","3","4","5","6","7","8","9"]:#Give a list of valid options.by using in operator.
        break
    else:
        print("Please enter a valid option (choose 1,2,3,4,5,6,7,8 or 9)")

length = int(Length_Password) #Convert the length of the password to an integer 
complexity = int(Complexity_Password) #Convert the complexity of the password to an integer
lower_letters = "abcdefghijklmnopqrstuvwxyz" #Define the lower letters
upper_letters = lower_letters.upper() #Define the upper letters by using the upper() method on the lower letters
letters = lower_letters + upper_letters #Define the letters by using the + operator on the lower and upper letters
numbers = "0123456789" #Define the numbers
symbols = "!@#$%^&*()_+[]{}|;:,./<>?" #Define the symbols

all_chars =[] #Empty array to store diferent characters based on the complexity of the password

if complexity ==1:
    all_chars = list(numbers) #Add numbers to the array

elif complexity ==2: #Use else if to check for multiple conditions
    all_chars == list(lower_letters) #Add lower letters to the array

elif complexity ==3:
    all_chars == list(upper_letters) #Add upper letters to the array

elif complexity ==4:
    all_chars == list(letters)   #Add letters to the array 

elif complexity ==5:
    all_chars == list(letters + numbers) #Add letters and numbers to the array

elif complexity ==6:
    all_chars == list(symbols) #Add symbols to the array

elif complexity ==7:
    all_chars == list(numbers + symbols) #Add numbers and symbols to the array

elif complexity ==8:
    all_chars == list(letters + symbols) #Add letters and symbols to the array

elif complexity ==9:
    all_chars == list(letters + numbers + symbols) #Add letters, numbers and symbols to the array



    
