from book import Book
from recipe import Recipe

book = Book("My Recipe Book", [], "2024-06-01", "2024-06-01")
recipe1 = Recipe("Pasta", 2, 30, ["pasta", "tomato sauce", "cheese"], "Delicious pasta with tomato sauce and cheese.", "lunch")
recipe2 = Recipe("Salad", 1, 10, ["lettuce", "tomatoes", "cucumber", "olive oil"], "Fresh and healthy salad.", "starter")
recipe3 = Recipe("Chocolate Cake", 3, 60, ["flour", "sugar", "cocoa powder", "eggs", "butter"], "Rich and moist chocolate cake.", "dessert")
recipe4 = Recipe("Grilled Chicken", 2, 45, ["chicken breast", "olive oil", "herbs"], "Juicy grilled chicken with herbs.", "lunch")
recipe5 = Recipe("Fruit Smoothie", 1, 5, ["banana", "strawberries", "yogurt", "honey"], "Refreshing fruit smoothie.", "starter")
recipe6 = Recipe("Beef Stew", 3, 120, ["beef", "potatoes", "carrots", "onions", "broth"], "Hearty beef stew with vegetables.", "lunch")

book.add_recipe(recipe1)
book.add_recipe(recipe2)
book.add_recipe(recipe3)
book.add_recipe(recipe4)
book.add_recipe(recipe5)
book.add_recipe(recipe6)

book.get_recipe_by_name("Pasta")
book.get_recipes_by_types("lunch")