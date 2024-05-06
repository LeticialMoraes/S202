from database import Database
from GameDatabase import GameDatabase

db = Database("bolt://44.200.4.98:7687", "neo4j", "radians-leaks-towns")
db.drop_all()

game_db = GameDatabase(db)

# Criar jogadores
game_db.create_player("João")
game_db.create_player("Maria")
game_db.create_player("José")

print("Jogadores:")
players = game_db.get_players()
for player in players:
        print(player)

game_db.create_match("Vitória do João")
game_db.create_match("Vitória do Maria")
game_db.create_match("Vitória do José")

print("\nPartidas:")
matches = game_db.get_matches()
for match in matches:
    print(match)

game_db.add_player_to_match("João", "Vitória do João")
game_db.add_player_to_match("Maria", "Vitória do Maria")
game_db.add_player_to_match("José", "Vitória do José")


game_db.delete_player("José")

db.close()