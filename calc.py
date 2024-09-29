
# More advanced calculator
# user enters both numbers and choice of operator
num_1 = float(input("enter first number: "))
op = input("enter an operator: ")
num_2 = float(input("enter a second number: "))

if op == "+":
    print(num_1 + num_2)
elif op == "-":
    print(num_1 - num_2)
elif op == "*":
    print(num_1 * num_2)
elif op == "/":
    print(num_1 / num_2)
else:
    print("invalid")
