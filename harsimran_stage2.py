# Stage 2: Calculator with Result Check

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = None

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2

else:
    print("Invalid operator.")

# Check and display result
if result is not None:
    print("Result =", result)

    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")