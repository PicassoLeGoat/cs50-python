# Prompt the user for an expression
user_input = input("Enter an expression: ").strip()

# Split the input into first number, operator, and second number
first_number, operator, second_number = user_input.split(" ")

# Convert strings to integers
first_number = int(first_number)
second_number = int(second_number)

# Perform the calculation
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
else:
    result = 0

# Print result formatted with one decimal place
print(f"{result:.1f}")
