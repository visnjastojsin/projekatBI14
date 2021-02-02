import json

def ucitaj_racune():
    with open("racun.json", encoding="UTF8") as datoteka:
        return json.load(datoteka)

def sacuvaj_racune(racun):
    with open("racun.json", "w", encoding="UTF8") as datoteka:
        json.dump(racun, datoteka, indent=4)