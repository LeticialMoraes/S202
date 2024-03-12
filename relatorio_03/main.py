from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

Pokedex.getPokemonByName("Charizard")
Pokedex.getPokemonsByType(["Grass", "Poison"])
Pokedex.getFirePokemons()
Pokedex.getFireWeaknessPokemons()
