from openai import OpenAI


def extract_entities(text):
    f = open("api-key.txt")
    api_key = f.read()

    prompt = """Erstelle eine Query für neo4j mit Cypher, um folgende Daten einzufügen. Beachte dabei, dass die Entitäten potenziell schon vorhanden sind. Gebe nur die Query ohne weitern Text aus.
                Nutze folgende Labels: Person, Event, Ort, Organisation
                Nutze folgende relationen: nimmt teil, findet statt, veranstaltet
                nutze folgende attribute: zeitpunkt, role"""
    message = prompt + text

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=message
    )

    text = response.output[0].content[0].text
    print(text)
    return text


