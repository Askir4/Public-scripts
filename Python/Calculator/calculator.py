#Since this is an educational project for my self, I followed tutorials (both written and on YouTube) to create this tool.
#Since I am a beginner basically every bit is commented as some kind of documentation for me.(How does is work?:)
#Simple Password Generator
#DO NOT USE FOR PRODUCTION
#This is for educational purposes only
print("\n###Calculator###\n")

while True:
    print("\nPlease select an operation:\n")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")
    operation=input("Please enter your choice: ")
    operation=operation.strip()
    
    if operation in ["1","2","3","4","5"]: #If users input is in given options break the loop
        break
    else:
        print("Invalid input. Please try again.") #If users input is not in given options print error message

while True:
    print("\nPlease enter your numbers\n")
    number1=float(input("Please enter your first number:"))
    if number1.isfloat():
        break
    else:
        print("Invalid input. Please try again.")
    number2=float(input("Please enter your first number"))
    if number2.isfloat():
        break
    else:
        print("Invalid input. Please try again.")


