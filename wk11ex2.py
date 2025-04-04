print("CALCULATOR APPLICATION")
num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))

result = 0
loop = True

while loop:
    print("Select an operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    menuOption = input("Enter your choice (1-4): ")
    
    if menuOption == "1":
        result = num1 + num2
        break
    elif menuOption == "2":
        result = num1 - num2
        break
    elif menuOption == "3":
        result = num1 * num2
        break
    elif menuOption == "4":
        result = num1 / num2
        break
    else:
        print("Invalid Value, Enter a number between (1 - 4)")

print(f"The result of division is: {result:.2f}")
print(f"Here is the result: {result:.2f}")


        
    
