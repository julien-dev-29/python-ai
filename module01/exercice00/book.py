from recipe import Recipe

class Book:

    def __init__(self, name: str, recipes_list: list, last_update: str, creation_date: str):
        """ Initializes the book class with the given parameters"""
        self.name = name
        self.recipes_list = recipes_list
        self.last_update = last_update
        self.creation_date = creation_date

    def get_recipe_by_name(self, name: str):
        """ Prints a recipe with the name `name` and returns the instance"""
        for recipe in self.recipes_list:
            if recipe.name == name:
                print(recipe)
                return recipe
        print(f"Recipe '{name}' not found.")
        return None

    def get_recipes_by_types(self, recipe_type: str):
        """ Get all recipe names for a given recipe_type """
        recipes_of_type = [recipe.name for recipe in self.recipes_list if recipe.recipe_type == recipe_type]
        if recipes_of_type:
            print(f"Recipes of type '{recipe_type}': {', '.join(recipes_of_type)}")
        else:
            print(f"No recipes found for type '{recipe_type}'.")

    def add_recipe(self, recipe):
        """ Add a recipe to the book and update last_update """
        if isinstance(recipe, Recipe):
            self.recipes_list.append(recipe)
            self.last_update = "now"  # You can replace "now" with the actual current date/time if needed
            print(f"Recipe '{recipe.name}' added to the book.")
        else:
            print("Invalid recipe. Please provide an instance of the Recipe class.")