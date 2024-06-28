num1 = input(int("Enter the first number"))
num2 = input(int("Enter the second number"))
operation = input("Choose the operation (+, -, *, /)")

match case:
    case:
      "+"
      results = num1 + num2
      print("The result is: ", result)
    case:
      "-"
      result = num1 - num2
      print("The result is: ", result)
    case:
      "/"
      result = num1 / num2
      print("The result is: ", result)
      if num1/0: print("can't devide by zero")
    case:
      "*"
      result =num1 * num2 
      print("The result is: ", result)
    
