from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.db = database

    def getPokemonByName(self, name: str):
        pokemons = self._database.collection.find({"name": name})
        writeAJson(pokemons, "pokemonByName")

    def getFireWeaknessPokemons(self):
        pokemons = self._database.collection.find({"weaknesses": "Fire"})
        writeAJson(pokemons, "fireWeaknessPokemons")

    def getPokemonsByType(self, types: list):
        pokemons = self._database.collection.find({"type": {"$in": types}})
        writeAJson(pokemons, "pokemons_by_type")

    def getFirePokemons(self):
        pokemons = self._database.collection.find({"type": "Fire"})
        writeAJson(pokemons, "firePokemons")

    def good_defense_types(self):
        pokemons = self.db.collection.find({"weaknesses": {"$size": 1}})
        print(pokemons)
        writeAJson(pokemons, "Good_Defense_Types_Pokemons")
        return pokemons