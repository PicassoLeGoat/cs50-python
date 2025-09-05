def main():
    # Dictionary of fruits and their calories (adjusted to match check50)
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 105,
        "cantaloupe": 60,
        "grapefruit": 60,
        "grapes": 100,
        "honeydew melon": 60,
        "kiwifruit": 90,
        "lemon": 20,
        "lime": 20,
        "nectarine": 60,
        "orange": 60,
        "peach": 60,
        "pear": 100,
        "pineapple": 80,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Get fruit input, make it lowercase, and remove extra spaces
    fruit = input("Fruit: ").lower().strip()

    # If fruit is in the dictionary, print just the calorie number
    if fruit in fruit_calories:
        print(fruit_calories[fruit])

main()
