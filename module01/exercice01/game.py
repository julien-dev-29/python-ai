class GotCharacter:

    def __init__(self, first_name: str, is_alive: bool):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """ A class representing a character from House Stark in Game of Thrones."""
    
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"

    def print_house_words(self):
        print(f"{self.house_words}")

    def die(self):
        self.is_alive = False