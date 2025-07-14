spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 4,
}
print(create_spicy_food(spicy_foods, new_food))
