expression = input("Expression: ").split()

x = float(expression[0])
y = float(expression[2])
operation = expression[1]

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "/":
    print(x / y)
elif operation == "*":
    print(x * y) 
else:
    print("What?")