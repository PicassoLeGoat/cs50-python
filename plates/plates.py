def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if length is between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if first two characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check if only letters and numbers are used (no spaces or punctuation)
    if not s.isalnum():
        return False

    # Check if numbers are only at the end and first number isn't 0
    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started and char == '0':
                return False
            number_started = True
        elif char.isalpha() and number_started:
            return False

    return True

main()
