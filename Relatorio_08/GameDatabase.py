class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, result):
        query = "CREATE (:Match {result: $result})"
        parameters = {"result": result}
        self.db.execute_query(query, parameters)

    def add_player_to_match(self, player_name, match_result):
        query = """
        MATCH (p:Player {name: $player_name})
        MATCH (m:Match {result: $match_result})
        CREATE (p)-[:PARTICIPATED_IN]->(m)
        """
        parameters = {"player_name": player_name, "match_result": match_result}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.result AS result"
        results = self.db.execute_query(query)
        return [result["result"] for result in results]

    def get_player_matches(self, player_name):
        query = """
        MATCH (p:Player {name: $player_name})-[:PARTICIPATED_IN]->(m:Match)
        RETURN m.result AS result
        """
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [result["result"] for result in results]

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, result):
        query = "MATCH (m:Match {result: $result}) DETACH DELETE m"
        parameters = {"result": result}
        self.db.execute_query(query, parameters)
