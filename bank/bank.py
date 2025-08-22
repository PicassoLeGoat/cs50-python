# Prompt the user for a greeting
greeting = input("Greeting: ")

# Clean it up: remove spaces at the start/end and make it lowercase
normalized = greeting.strip().lower()

# Check what the greeting starts with
if normalized.startswith("hello"):
    # Starts with "hello"? No money for you
    print("$0")
elif normalized.startswith("h"):
    # Starts with an "h" but not "hello"? Bank pays $20
    print("$20")
else:
    # Anything else? Bank gives the full $100
    print("$100")
