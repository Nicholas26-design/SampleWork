"""
Purpose/Goal: to make a calculator. No GUI at this phase.
Reason: practice writing python from scratch and debugging.
Additional benefits include programmatic thinking and problem-solving.

Breakdown:
A calculator receives input from user in the form of:
 a) mathematical operations
 b) numeric inputs
"""

# Most basic way to approach is variable assignment. We need to loop around if they don't enter the correct thing.
# Try except block should do it. break if it's right. Feedback if wrong.
# The below should take care of numeric input

def number_input():
    while True:
        try:
            var_1 = int(input("Enter an integer: "))
            storage = f"Hello. You have entered the number {var_1}."
            print(storage)
            break
        except ValueError:
            print("You made a mistake. Please enter an integer.")


number_input()

# Now I need pretty much the same template, except it is for math signs.

def math_signs():
    valid_operators = ['+', '-', '*', '/', '%', '**', '//']
    # Addition: +
    # Subtraction: -
    # Multiplication: *
    # Division: /
    # Modulus: %
    # Exponentiation: **
    # Floor Division: //
    while True:
        sign_1 = input("Enter a math operator: ")
        if sign_1 in valid_operators:
            storage = f"Hello. You have entered the operator {sign_1}."
            print(storage)
            break
        else:
            print("Invalid operator. Please enter a valid math operator.")

math_signs()