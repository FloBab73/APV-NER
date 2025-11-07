# NER mit LLM und neo4j

## Ablauf
- Der Chronikstar Auszug wird eingelesen
- Für jeden Eintrag wird mit folgenden Systempromt ein Aufruf gegen die OpenAI API (`gpt-40-mini`) gesendet
  
    
    Erstelle eine Cypher-Query für Neo4j, die die übergebenen Informationen in den Graphen einfügt.
    Extrahiere dabei – sofern vorhanden – folgende Entitäten und Relationen:
    Personen (mit Rolle, wenn vorhanden)
    Organisationen
    Events (mit Zeitpunkt, wenn vorhanden)
    Orte
    Regeln:
    Personen oder Organisationen können an Events teilnehmen oder sie veranstalten.
    Events finden an einem Ort statt.
    Wenn eine Kategorie nicht vorhanden oder nicht ableitbar ist, lasse sie weg.
    Verwende ausschließlich die vorgegebenen Labels und Relationen.
    Gehe davon aus, dass alle Entitäten bereits existieren und nutze daher MERGE, nicht CREATE.
    Gib ausschließlich die fertige Cypher-Query als Plaintext aus – ohne Markdown, Kommentare oder Erklärungen.

- mit der Antwort in Form einer Cypher-Query wird die in Docker gehostete neo4j Datenbank befüllt
- Nach der Ausführung lassen sich mithilfe der grafischen Oberfläche die Ergebnisse betrachten

## Erkenntnisse
- Das LLM macht immer wieder Syntaxfehler in der Cypher Query
- Trotz sehr genauer Beschreibung dichtet die KI doch ab und zu wieder eigene Label dazu
- Besonders schwierig ist es zu erkennen welche Entitäten _nicht_ aufgenommen werden sollen
  - _Beispiele: 7000 Demonstraten, Tischkicker_
- Auch der Umgang mit unbekannten Daten ist schwierig
  - _Es gibt immer mal wieder Nodes mit dem Namen `unbekannt` oder z.B. Events mit der Zeit `NULL`_
- Jede Anfrage dauert mindestens 3-4 Sekunden 