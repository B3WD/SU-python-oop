# from pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        repeats = [owned_pokemon for owned_pokemon in self.pokemon if pokemon.name == owned_pokemon.name]
        if not repeats:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon:
            if pokemon_name == pokemon.name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        info = ""
        info += f"Pokemon Trainer {self.name}\n"
        info += f"Pokemon count {len(self.pokemon)}\n"
        for pokemon in self.pokemon:
            info += f"- {pokemon.pokemon_details()}\n"

        return info


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("xdddddddd"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())