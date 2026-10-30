fav_chais = ["Green Tea","Lemon Tea","Green Tea", "Masala Tea", "Ginger Tea", "Vanilla Tea", "Elaichi Tea"]

unique_chai = {chai for chai in fav_chais if len(chai)>10}

print(unique_chai)

recipes = {
    "Masala Tea": ["milk", "ginger", "cardamom"],
    "Lemon Tea": ["milk", "lemon"],
    "Elaichi Tea": ["milk", "cardamom"],
    "Vanilla Tea": ["milk", "vanilla extract"]
}

unique_ingredients = { item for ingr in recipes.values() for item in ingr }
print(unique_ingredients)