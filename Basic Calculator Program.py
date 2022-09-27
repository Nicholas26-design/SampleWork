# Getting input
name = input("enter name: ")
age = input("enter age: ")
print("Hello " + name + "! You are " + age + " Can you use a calculator?")

# Calculator
Var1 = input("enter a number: ")
Var2 = input("enter another number: ")
Result = float(Var1) + float(Var2)
print(Result)
print("On to the next one")

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
