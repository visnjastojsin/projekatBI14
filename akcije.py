import akcijeIO
import datetime
import knjige

akcije = akcijeIO.ucitaj_akcije()

def prikaz_svih_akcija(administrator = False):
    izbor = prikaz_svih_akcija_meni()
    if izbor == '1':
        sortirane_akcije = sorted(akcije, key=lambda k: k['sifra'])
    elif izbor == '2':
        sortirane_akcije = sorted(akcije, key=lambda k: k['datum_vazenja'])
    date = datetime.datetime.now().date()
    for akcija in sortirane_akcije:
        pisi = True
        if not administrator:
            for knjiga in akcija['artikli']:
                if knjiga['brisanje'] == True:
                    pisi = False
        if pisi:
            print(format_header_akcije())
            print(format_akcija1(akcija))
            for i in range(1, len(akcija['artikli'])):
                print(format_akcija2(akcija, i))
            print()
            print()



def prikaz_svih_akcija_meni_ispis():
    print("\nIzaberite opciju:")
    print("1 - Sortiranje po sifri")
    print("2 - Sortiranje po datumu")


def prikaz_svih_akcija_meni():
    prikaz_svih_akcija_meni_ispis()
    command = input(">> ")
    while command not in ('1', '2'):
        print("\nUneli ste pogresnu komandu!\n")
        prikaz_svih_akcija_meni_ispis()
        command = input(">> ")
    return command

def pretraga_svih_akcija(administrator = False):
    izbor = pretraga_svih_akcija_meni()
    if izbor == '1':
        sifra = input("Uneti zeljenu sifru:\n>> ")
        sortirane_akcije = pretraga_po_sifri(sifra, "sifra")
    elif izbor == '2':
        sifra = input("Uneti zeljeni naslov:\n>> ")
        sortirane_akcije = pretraga_knjiga_u_akciji(sifra, "naslov")
    elif izbor == '3':
        sifra = input("Uneti zeljenog autora:\n>> ")
        sortirane_akcije = pretraga_knjiga_u_akciji(sifra, "autor")
    elif izbor == '4':
        sifra = input("Uneti zeljenu kategoriju:\n>> ")
        sortirane_akcije = pretraga_knjiga_u_akciji(sifra, "kategorija")

    for akcija in sortirane_akcije:
        pisi = True
        if not administrator:
            for knjiga in akcija['artikli']:
                if knjiga['brisanje'] == True:
                    pisi = False
        if pisi:
            print(format_header_akcije())
            print(format_akcija1(akcija))
            for i in range(1, len(akcija['artikli'])):
                print(format_akcija2(akcija, i))
            print()
            print()

def pretraga_po_sifri(sifra, kljuc):
    lista = []
    for akcija in akcije:
        if sifra.lower() in akcija[kljuc][:len(sifra)].lower():
            lista.append(akcija)
    return lista

def pretraga_knjiga_u_akciji(sifra, kljuc):
    lista = []
    for akcija in akcije:
        for knjiga in akcija['artikli']:
            if sifra.lower() in knjiga[kljuc][:len(sifra)].lower():
                lista.append(akcija)
                break
    return lista


def pretraga_svih_akcija_meni_ispis():
    print("\nIzaberite opciju:")
    print("1 - Pretraga po sifri")
    print("2 - Pretraga po naslovu")
    print("3 - Pretraga po autoru")
    print("4 - Pretraga po kategoriji")

def pretraga_svih_akcija_meni():
    pretraga_svih_akcija_meni_ispis()
    command = input(">> ")
    while command not in ('1', '2', '3', '4'):
        print("\nUneli ste pogresnu komandu!\n")
        pretraga_svih_akcija_meni_ispis()
        command = input(">> ")
    return command

def format_header_akcije():
    return "Sifra   |Naslov knjige                          |Nova cena          |Stara cena         |Datum          \n" \
           "--------+---------------------------------------+-------------------+-------------------+---------------"

def format_akcija1(akcija):
    return "{0:8}|{1:39}|{2:19}|{3:19}|{4:15}".format(akcija['sifra'], akcija['artikli'][0]['naslov'], akcija['artikli'][0]['cena'], akcija['artikli'][0]['stara_cena'], akcija['datum_vazenja'])

def format_akcija2(akcija, i):
    return "{0:8}|{1:39}|{2:19}|{3:19}|{4:15}".format("", akcija['artikli'][i]['naslov'], akcija['artikli'][i]['cena'], akcija['artikli'][i]['stara_cena'], "")

def dodavanje_akcije():
    akcija = {}
    akcija['sifra'] = str(len(akcije) + 1)
    akcija['artikli'] = []
    sifra = input("Uneti sifru knjige ili x za kraj: \n>> ")
    while sifra.upper() != 'X':
        ima = False
        for knjiga in knjige.knjige:
            if knjiga['sifra'] == sifra:
                knjiga_akcija = {
                    "sifra": knjiga['sifra'],
                    "naslov": knjiga['naslov'],
                    "autor":knjiga['autor'],
                    "isbn": knjiga['isbn'],
                    "izdavac": knjiga['izdavac'],
                    "godina": knjiga['godina'],
                    "stara_cena": knjiga['cena'],
                    "cena": float(input("Uneti novu cenu knjige: ")),
                    "kategorija": knjiga['kategorija'],
                    "brisanje": knjiga['brisanje']
                }
                akcija['artikli'].append(knjiga_akcija)
                ima = True
                break
        if not ima:
            print("Ne postoji knjiga sa ovom sifrom!\n")
        sifra = input("Uneti sifru knjige ili x za kraj: \n>> ")

    akcija['datum_vazenja'] = input("Uneti datum u obliku gggg-mm-dd:\b>> ")
    akcije.append(akcija)
    akcijeIO.sacuvaj_akcije(akcije)
