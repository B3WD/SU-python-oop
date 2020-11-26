class Pokemon():

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"


class Trainer():

    pokemon = list()

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon):
        if pokemon.name not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon:
            if pokemon_name == pokemon.name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon not caught"

    def trainer_data(self):
        info = ""
        info += f"Pokemon Trainer {self.name}\n"
        info += f"Pokemon count {len(self.pokemon)}\n"
        for pokemon in self.pokemon:
            info += f"- {pokemon.pokemon_details()}\n"

        return info


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())