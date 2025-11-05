from neo4j import GraphDatabase

DATABASE = "neo4j"
URI = "neo4j://localhost"
AUTH = ("neo4j", "Marchivum")

class DatabaseConnection:

    def __init__(self):
        self.driver = GraphDatabase.driver(URI, auth=AUTH)

    def insert_data(self, query):
        self.driver.execute_query(query, database_=DATABASE)

    def get_all_entities_with_label(self, label):
        records = self.query_data("MATCH (e:" + label + ") RETURN e")
        return list(records)

    def query_data(self, query):
        records, summary, keys = self.driver.execute_query(query, database_=DATABASE)
        return map(lambda x: x.data(), records)

