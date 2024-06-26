num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
choose_the_operation = input("Choose the operation (+, -, *, /)")


match case:

        case "+":
            result = num1 + num2
            print("The result is: " , result)
        case "-":
            result = num1 - num2
            print("The result is: " , result)
        case "*":
            result = num1 * num2
            print("The result is: " , result)
        case "/":
            if num2 != 0:
            result = num1 / num2
            print("The result is: " , result)
        else:
            print("Error: Division by zero is not allowed")
        case_:
            print("please enter an invalid operation (+, *, -, /))

            
        



