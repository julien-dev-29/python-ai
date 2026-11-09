cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "avocado", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def printAllRecipesName():
    for key in cookbook.keys():
        print(f"{key}")

def printRecipeDetails(name: str):
    print()