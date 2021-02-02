import json

def ucitaj_knjige():
    with open("knjige.json", encoding="UTF8") as datoteka:
        return json.load(datoteka)

def sacuvaj_knjige(knjige):
    with open("knjige.json", "w", encoding="UTF8") as datoteka:
        json.dump(knjige, datoteka, indent=10)