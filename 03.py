# megoldas.py

from Pokemon import Pokemon

def initialize_pokemons():
    pokemon = []
    pokemon.append(Pokemon("Balbasaur", "fű", "víz"))
    pokemon.append(Pokemon("Pikatchu", "elektromos", "víz"))
    pokemon.append(Pokemon("Charizard", "tűz", "fű"))
    pokemon.append(Pokemon("Balbasaur", "víz", "tűz"))
    pokemon.append(Pokemon("Kingler", "víz", "tűz"))
    return pokemon

ash_pokemonjai = initialize_pokemons()

vad_pokemon = Pokemon("Oddish", "fű", "víz")

for i, pokemon in enumerate(ash_pokemonjai):
    if ash_pokemonjai[i].hatasos_ellene(vad_pokemon):
        nev = ash_pokemonjai[i].nev

print(nev + ", téged választalak!") # Charizard, téged választalak!