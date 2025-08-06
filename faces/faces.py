#faces.py

# Define a function to convert text emoticons into emoji
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

# Define the main function that handles user input and output
def main():
    user_input = input("Enter your message: ")
    print(convert(user_input))

main()
