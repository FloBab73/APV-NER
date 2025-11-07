from ChatClient import extract_entities
from DatabaseConnection import DatabaseConnection
from FileReader import read_entries_from_file

if __name__ == '__main__':
    entries = read_entries_from_file()
    db = DatabaseConnection()
    for entry in entries:
        entity_query = extract_entities(entry.text)
        entity_query = entity_query.replace("```", "").replace("\n", " ")
        db.insert_data(entity_query)