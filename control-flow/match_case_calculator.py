num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

result = ""

match operation:
    case "+":
        result = num1 + num2
    case "-":  
        result = num1 - num2
    case "*":  
        result = num1 * num2
        
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "cannot divide by zero"
    case _:
        result = ("Invalid operation")

print("The result is: ", result)
         
