import datetime

from openai import OpenAI

PROMPT = """Erstelle eine Cypher-Query für Neo4j, die die übergebenen Informationen in den Graphen einfügt.
    Achte dabei besonders darauf, dass die bereitgestellte Query ohne Nachbearbeitung ausgeführt werden kann 
    Extrahiere dabei – sofern vorhanden – folgende Entitäten und Relationen:
    Personen (optional mit Rolle)
    Organisationen
    Events (optional mit Zeitpunkt)
    Orte
    Regeln:
    Personen oder Organisationen können an Events teilnehmen oder sie veranstalten.
    Events finden an einem Ort statt.
    Wenn eine Kategorie nicht vorhanden oder nicht ableitbar ist, lasse sie weg.
    Verwende ausschließlich die vorgegebenen Labels und Relationen.
    Gehe davon aus, dass alle Entitäten bereits existieren und nutze daher MERGE, nicht CREATE.
    Gib ausschließlich die fertige Cypher-Query als Plaintext aus – ohne Markdown, Kommentare oder Erklärungen."""

def extract_entities(text):
    f = open("api-key.txt")
    api_key = f.read()

    message = PROMPT + text

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    starttime = datetime.datetime.now()
    response = client.responses.create(
        model="gpt-4o-mini",
        input=message
    )
    endtime = datetime.datetime.now()
    print(endtime - starttime)
    text = response.output[0].content[0].text
    print(text)
    return text
