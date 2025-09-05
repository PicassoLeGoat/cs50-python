#take user input
user_input = input("Enter text to slow down: ")

#split the input with spaces and joing with "..."
words = user_input.split(" ")
output = "...".join(words)

#remove any white spaces
output = output.strip()

print(output)
