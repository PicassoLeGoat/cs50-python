text = input("Input: ")

print("Output: ", end="")

for c in text:
    if c not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print(c, end="")

print()
