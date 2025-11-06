def read_entries_from_file():
    f = open("export_chronikstar-full.csv")
    text = f.read()
    rows = text.split("\n")
    entries = []
    for row in rows[:1]:
        entries.append(Entry(row))
    return entries


class Entry:
    def __init__(self, text):
        fields = text.split(",")
        self.title = fields[0]
        self.anfang = fields[1]
        self.ende = fields[2]
        self.erfassungsdatum = fields[3]
        self.bemerkung = fields[4]
        self.text = fields[5]
        self.kategorien = fields[6]
        self.quellen = fields[7]
