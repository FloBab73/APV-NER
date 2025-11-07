import csv

FILENAME = 'export_chronikstar_50_latest.csv'


def read_entries_from_file():
    entries = []
    with open(FILENAME) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in spamreader:
            entries.append(Entry(row))

    return entries


class Entry:
    def __init__(self, fields):
        self.title = fields[0]
        self.anfang = fields[1]
        self.ende = fields[2]
        self.erfassungsdatum = fields[3]
        self.bemerkung = fields[4]
        self.text = fields[5]
        self.kategorien = fields[6]
        self.quellen = fields[7]
