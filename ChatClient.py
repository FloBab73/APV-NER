import datetime

from openai import OpenAI


def extract_entities(text):
    f = open("api-key.txt")
    api_key = f.read()

    prompt = """Erstelle eine Cypher-Query für Neo4j, um die angegebenen Daten einzufügen.
    Verwende ausschließlich folgende Labels:
    - Person, Event, Ort, Organisation.
    Verwende nur diese Relationen:
    - nimmt_teil, findet_statt, veranstaltet
    Erlaube nur diese Attribute an Knoten oder Relationen:
    - zeitpunkt, role
    Gehe davon aus, dass Entitäten eventuell schon vorhanden sind (verwende also MERGE statt CREATE).
    Die Query soll nur die definierten Strukturen erzeugen oder verknüpfen, keine zusätzlichen Labels, Relationen oder Eigenschaften.
    Gib nur die reine Cypher-Query als Plaintext aus (kein Markdown, keine Erklärung, kein Kommentar)."""
    message = prompt + text

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
