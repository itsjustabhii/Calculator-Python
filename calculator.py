first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
operator = input("Enter your Operator (+, -, *, /,%): ")

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print("Invalid Operator!")
