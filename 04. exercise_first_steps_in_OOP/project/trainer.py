from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):

        try:
            searched_pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
            self.pokemons.remove(searched_pokemon)
            return f"You have released {pokemon_name}"

        except StopIteration:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"

        for p in self.pokemons:
            result += f"- {p.pokemon_details()}\n"

        return result
