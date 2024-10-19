'''
Problem 1: Pokemon Class
Understand:
'''


class Pokemon:
    def __init__(self, name:str, types:list):
        self.name = name
        self.types = types
        self.is_caught = False


    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })

    def catch(self):
        self.is_caught = True

Pkmn_Pikachu = Pokemon('Pikachu', ['Electric'])
print(Pkmn_Pikachu.name)
print(Pkmn_Pikachu.types)
print(Pkmn_Pikachu.is_caught)

#Q2 Create pokemon and use class method
Pkmn_Squirtle = Pokemon('Squirtle', ['Water'])
Pkmn_Squirtle.print_pokemon()


#Q3 Is Caught
Pkmn_Squirtle.is_caught = True
Pkmn_Squirtle.print_pokemon()

#Q4 Catch Pokemon
Pkmn_Pikachu.catch()
Pkmn_Pikachu.print_pokemon()

#Q5 Choose Pokemon

