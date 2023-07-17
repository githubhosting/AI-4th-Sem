# Knowledge Base
food_data = {
    "apple": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14},
    "banana": {"calories": 96, "protein": 1.2, "fat": 0.2, "carbs": 23},
    "orange": {"calories": 47, "protein": 0.9, "fat": 0.1, "carbs": 12},
    "peanuts": {"calories": 567, "protein": 25, "fat": 49, "carbs": 16},
    "egg": {"calories": 155, "protein": 13, "fat": 11, "carbs": 1.1},
    "milk": {"calories": 42, "protein": 3.4, "fat": 1, "carbs": 5},
    "bread": {"calories": 74, "protein": 3.1, "fat": 0.7, "carbs": 13},
    "rice": {"calories": 130, "protein": 2.7, "fat": 0.3, "carbs": 28},
    "chicken": {"calories": 239, "protein": 27, "fat": 14, "carbs": 0},
}

allergens = {
    "namratha": ["peanuts", "shellfish", "apple"],
    "shravan": ["egg", "milk"],
}

preferences = {
    "nams": ["apple", "banana"],
    "shravu": ["chicken", "egg"],
}


def calculate_total_calories(meal):
    total_calories = 0
    for food in meal:
        if food in food_data:
            total_calories += food_data[food]["calories"]
    return total_calories


def suggest_alternatives(user_name, meal):
    alternatives = []
    allergens_list = allergens.get(user_name, [])
    preferences_list = preferences.get(user_name, [])

    for food in meal:
        if food in allergens_list:
            for item in food_data:
                if item not in allergens_list and item not in meal:
                    alternatives.append(item)

        if food not in food_data and food not in preferences_list:
            for item in food_data:
                if item in preferences_list and item not in meal:
                    alternatives.append(item)

    return alternatives


def ask_user_input():
    user_name = input("Enter your Name: ")

    meal = []
    while True:
        food = input(
            "Enter a food item for the meal (type 'done' when finished): ")
        if food.lower() == "done":
            break
        meal.append(food.lower())

    return user_name, meal


def main():
    user_name, meal = ask_user_input()

    total_calories = calculate_total_calories(meal)
    print(f"Total calories in the meal: {total_calories}")

    alternative_foods = suggest_alternatives(user_name, meal)
    if alternative_foods:
        print("Suggested alternative foods:")
        for food in alternative_foods:
            print(food)
    else:
        print("No alternative suggestions based on your preferences/allergies.")


if __name__ == "__main__":
    main()
