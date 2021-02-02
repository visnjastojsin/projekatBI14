import json

def ucitaj_akcije():
    with open("akcijske_ponude.json", encoding="UTF8") as datoteka:
        return json.load(datoteka)

def sacuvaj_akcije(akcije):
    with open("akcijske_ponude.json", "w", encoding="UTF8") as datoteka:
        json.dump(akcije, datoteka, indent=10)