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
        "ingredients": ["avocado", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def printCookbook():
    print("\nList of Cookbook recipes:")

    if not cookbook:
        print("The cookbook is empty!")
        return

    for name, recipe in cookbook.items():
        print(f"\nRecipe: {name}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Meal: {recipe['meal']}")
        print(f"Preparation time: {recipe['prep_time']} minutes")

def printHeader():
    print("---------------------------------------------------------")
    print("XXXXXXX                                                  ")
    print("X        XXXXX  XXXXX  X   X  XXXXX   XXXXX  XXXXX  X   X")
    print("X        X   X  X   X  XXX    X  X    X   X  X   X  XXX  ")
    print("X        X   X  X   X  X  X   X    X  X   X  X   X  X  X ")
    print("XXXXXXX  XXXXX  XXXXX  X   X  XXXXX   XXXXX  XXXXX  X   X")
    print("---------------------------------------------------------")
    print("")

def printAllRecipesName():
    print("\nAvailable recipes:")

    if not cookbook:
        print("No recipes available.")
        return
    for name in cookbook:
        print(f"- {name}")

def printRecipeDetails():
    name = input("\nEnter a recipe name: ").strip()
    recipe = cookbook.get(name)
    if recipe == None:
        print("This recipe does not exist.")
        return
    print("\n---------------------------------------------------------")
    print(f"Recipe for {name}")
    print("---------------------------------------------------------")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Meal: {recipe['meal']}")
    print(f"Preparation time: {recipe['prep_time']} minutes")

def deleteRecipe():
    name = input("\nEnter the recipe name to delete: ").strip()

    if name not in cookbook:
        print("This recipe doesn't exist!")
        return

    confirmation = input(
        f"Are you sure you want to delete {name}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        del cookbook[name]
        print(f"{name} has been deleted successfully!")
    else:
        print("Deletion cancelled.")

def addRecipe():
    print("\n----> Enter a name:")
    name = input().strip()

    if not name:
        print("Recipe name cannot be empty!")
        return

    if name in cookbook:
        print("This recipe already exists!")
        return

    print("----> Enter ingredients separated by spaces:")
    ingredients = input().strip().split()

    if not ingredients:
        print("You must enter at least one ingredient!")
        return
    print("----> Enter meal type:")
    meal = input().strip()

    if not meal:
        print("Meal type cannot be empty!")
        return

    print("----> Enter preparation time in minutes:")

    try:
        prep_time = int(input())

        if prep_time <= 0:
            print("Preparation time must be positive!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return
    
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }

    print(f"\nRecipe '{name}' added successfully!")

def printMenu():
    print("\nList of available options:")
    print("     1: Add a recipe")
    print("     2: Delete a recipe")
    print("     3: Print a recipe")
    print("     4: Print the cookbook")
    print("     5: List recipe names")
    print("     6: Quit")

def getOptionFromInput():
    option = input("\nPlease select an option: ").strip()
    if option == "1":
        addRecipe()

    elif option == "2":
        deleteRecipe()

    elif option == "3":
        printRecipeDetails()

    elif option == "4":
        printCookbook()

    elif option == "5":
        printAllRecipesName()

    elif option == "6":
        print("Cookbook closed. Goodbye !")
        return False

    else:
        print("\nSorry, this option does not exist.")

    return True

# Main program
printHeader()

while True:
    printMenu()
    if not getOptionFromInput():
        break