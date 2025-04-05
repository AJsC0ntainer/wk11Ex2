#Program Title
print("CALCULATOR APPLICATION")
#Prompt user for number 1
num1 = float(input("What is the first number? "))
#Prompt user for number 2
num2 = float(input("What is the second number? "))
#Variable to store the result
result = 0
#Variable to keep the loop until break
loop = True
#While loop
while loop:
    #Menu options
    print("Select an operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    menuOption = input("Enter your choice (1-4): ")
    #Conditional for executing option 1
    if menuOption == "1":
        #Formula
        result = num1 + num2
        #Breaks the loop
        break
    #Conditional for executing option 2
    elif menuOption == "2":
        #Formula
        result = num1 - num2
        #Breaks the loop
        break
    #Conditional for executing option 3
    elif menuOption == "3":
        #Formula
        result = num1 * num2
        #Breaks the loop
        break
    #Conditional for executing option 4
    elif menuOption == "4":
        #Formula
        result = num1 / num2
        #Breaks the loop
        break
    else:
        #Error message for invalid menu option
        print("Invalid Value, Enter a number between (1 - 4)")
#Display result
print(f"The result of division is: {result:.2f}")
#Display Result
print(f"Here is the result: {result:.2f}")

#Pushed to Wk11ex2 GitHun repo.