import json

def ucitaj_korisnike():
    with open("korisnici.json", encoding="UTF8") as datoteka:
        return json.load(datoteka)

def sacuvaj_korisnike(korisnici):
    with open("korisnici.json", "w", encoding="UTF8") as datoteka:
        json.dump(korisnici, datoteka, indent=4)