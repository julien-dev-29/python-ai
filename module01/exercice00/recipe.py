class Recipe:

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: str):
        """ Initializes the recipe class with the given parameters"""
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        

    def __str__(self):
        """ Returns the string to print with the recipe info"""
        return f"Recipe: {self.name}\nCooking Level: {self.cooking_lvl}\nCooking Time: {self.cooking_time} minutes\nIngredients: {', '.join(self.ingredients)}\nDescription: {self.description}\nRecipe Type: {self.recipe_type}"