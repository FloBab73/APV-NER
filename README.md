# APV - Named Entity Recognition

## Neo4j in Docker starten
- Docker installieren
- `docker run --publish=7474:7474 --publish=7687:7687 --env NEO4J_AUTH=neo4j/Marchivum --volume ~/ws/APV-neo4j/data:/data neo4j`
- Grafische Oberfläche unter http://localhost:7474/browser/
- Anmelden mit `neo4j` und `Marchivum`
- Genaue [Anleitung](https://neo4j.com/docs/operations-manual/current/docker/introduction/) zum nachlesen

## API Anbindung
- Chronikstar-Datei in den Ordner legen
- im Ordner eine Datei `api-key.txt` mit dem api key anlegen
- DATEI NICHT PUSHEN!

