def main():
    # Ask the user for a time
    time_input = input("What time is it? ").strip()

    # Convert to decimal hours
    hours = convert(time_input)

    # Check which meal it is and print with "time"
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")
    # If it's not a meal time, do nothing


def convert(time):
    # Find the colon in the string
    colon_index = time.find(":")

    # Get hours and minutes as integers
    hours = int(time[:colon_index])
    minutes = int(time[colon_index + 1:])

    # Convert to decimal hours
    return hours + minutes / 60


if __name__ == "__main__":
    main()
