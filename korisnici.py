import korisniciIO
import knjige
import akcije
import racuni

korisnici = korisniciIO.ucitaj_korisnike()

def korisnik_login(username, password):
    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == username and korisnik['lozinka'] == password:
            if korisnik['tip_korisnika'] == "Administrator":
                return "Administrator", korisnik
            elif korisnik['tip_korisnika'] == "Menadzer":
                return "Menadzer", korisnik
            elif korisnik['tip_korisnika'] == "Prodavac":
                return "Prodavac", korisnik
    return False

def menadzer(menadzer):
    print("Ulogovao se menazder")
    izbor = '0'
    while izbor.upper() != 'X':
        izbor = menadzer_meni()
        if izbor == '1':
            knjige.prikaz_svih_knjiga()
        elif izbor == '2':
            knjige.pretraga_svih_knjiga()
        elif izbor == '3':
            akcije.prikaz_svih_akcija()
        elif izbor == '4':
            akcije.pretraga_svih_akcija()
        elif izbor == '5':
            registracija()
        elif izbor == '6':
            prikaz_svih_korisnika()
        elif izbor == '7':
            akcije.dodavanje_akcije()
        elif izbor == '8':
            racuni.izvestaji()



def menadzer_meni_ispis():
    print("\nIzaberite opciju:")
    print("1 - Prikaz svih knjiga")
    print("2 - Pretraga knjiga")
    print("3 - Prikaz svih akcija")
    print("4 - Pretraga akcija")
    print("5 - Registracija")
    print("6 - Prikaz svih korisnika")
    print("7 - Dodavanje akcijske ponude")
    print("8 - Kreiranje izvestaja")
    print("X - Povratak nazad")

def menadzer_meni():
    menadzer_meni_ispis()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', 'X'):
        print("\nUneli ste pogresnu komandu!\n")
        menadzer_meni_ispis()
        command = input(">> ")
    return command

def administrator(administrator):
    print("Ulogovao se administrator")
    izbor = '0'
    while izbor.upper() != 'X':
        izbor = administrator_meni()
        if izbor == '1':
            knjige.prikaz_svih_knjiga(True)
        elif izbor == '2':
            knjige.pretraga_svih_knjiga(True)
        elif izbor == '3':
            akcije.prikaz_svih_akcija(True)
        elif izbor == '4':
            akcije.pretraga_svih_akcija(True)
        elif izbor == '5':
            registracija()
        elif izbor == '6':
            prikaz_svih_korisnika()
        elif izbor == '7':
            knjige.dodavanje_knjige()
        elif izbor == '8':
            knjige.izmena_knjige()
        elif izbor == '9':
            knjige.brisanje()

def administrator_meni_ispis():
    print("\nIzaberite opciju:")
    print("1 - Prikaz svih knjiga")
    print("2 - Pretraga knjiga")
    print("3 - Prikaz svih akcija")
    print("4 - Pretraga akcija")
    print("5 - Registracija")
    print("6 - Prikaz svih korisnika")
    print("7 - Dodavanje knjige")
    print("8 - Izmena knjige")
    print("9 - Logicko brisanje knjige")
    print("X - Povratak unazad")

def administrator_meni():
    administrator_meni_ispis()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'):
        print("\nUneli ste pogresnu komandu!\n")
        administrator_meni_ispis()
        command = input(">> ")
    return command

def prodavac(prodavac):
    print("Ulogovao se prodavac")
    izbor = '0'
    while izbor.upper() != 'X':
        izbor = prodavac_meni()
        if izbor == '1':
            knjige.prikaz_svih_knjiga()
        elif izbor == '2':
            knjige.pretraga_svih_knjiga()
        elif izbor == '3':
            akcije.prikaz_svih_akcija()
        elif izbor == '4':
            akcije.pretraga_svih_akcija()
        elif izbor == '5':
            racuni.prodaja_knjiga(prodavac)
        elif izbor == '6':
            knjige.dodavanje_knjige()
        elif izbor == '7':
            knjige.izmena_knjige()
        elif izbor == '8':
            knjige.brisanje()

def prodavac_meni_ispis():
    print("\nIzaberite opciju:")
    print("1 - Prikaz svih knjiga")
    print("2 - Pretraga knjiga")
    print("3 - Prikaz svih akcija")
    print("4 - Pretraga akcija")
    print("5 - Prodaja knjiga")
    print("6 - Dodavanje knjige")
    print("7 - Izmena knjige")
    print("8 - Logicko brisanje knjige")
    print("X - Povratak unazad")

def prodavac_meni():
    prodavac_meni_ispis()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', 'X'):
        print("\nUneli ste pogresnu komandu!\n")
        prodavac_meni_ispis()
        command = input(">> ")
    return command


def registracija():
    print("Izaberite opciju:")
    print("1 - Registracija prodavaca")
    print("2 - Registracija menadzera")
    print("X - Povratak na pocetak")
    opet = input(">> ")
    if opet.upper() == 'X':
        return
    while opet.upper() not in ('1', '2', 'X'):
        print("Izaberite opciju:")
        print("1 - Registracija prodavaca")
        print("2 - Registracija menadzera")
        print("X - Povratak na pocetak")
        opet = input(">> ")
    if opet == '1':
        tip = 'Prodavac'
    elif opet == '2':
        tip = 'Menadzer'
    else:
        return
    lista_imena = []
    for korisnik in korisnici:
        lista_imena.append(korisnik['korisnicko_ime'])
    korisnik = {}
    korisnik['korisnicko_ime'] = input("Uneti korisnicko ime:\n>> ")
    while korisnik['korisnicko_ime'] in lista_imena:
        print("\nKorisnicko ime vec postoji, pokusajte ponovo!\n")
        korisnik['korisnicko_ime'] = input("Uneti korisnicko ime:\n>> ")
    korisnik['lozinka'] = input("Uneti lozinku:\n>> ")
    korisnik['ime'] = input("Uneti ime:\n>> ")
    korisnik['prezime'] = input("Uneti prezime:\n>> ")
    korisnik['tip_korisnika'] = tip
    korisnici.append(korisnik)
    korisniciIO.sacuvaj_korisnike(korisnici)

def prikaz_svih_korisnika():
    izbor = prikaz_svih_korisnika_meni()
    if izbor == '1':
        sortirani_korisnici = sorted(korisnici, key=lambda k: k['ime'])
    elif izbor == '2':
        sortirani_korisnici = sorted(korisnici, key=lambda k: k['prezime'])
    elif izbor == '3':
        sortirani_korisnici = sorted(korisnici, key=lambda k: k['tip_korisnika'])
    print(format_header_korisnik())
    for korisnik in sortirani_korisnici:
        print(format_korisnik(korisnik))


def prikaz_svih_korisnika_meni_ispis():
    print("\nIzaberite opciju:")
    print("1 - Sortiranje po imenu")
    print("2 - Sortiranje po prezimenu")
    print("3 - Sortiranje po tipu korisnika")


def prikaz_svih_korisnika_meni():
    prikaz_svih_korisnika_meni_ispis()
    command = input(">> ")
    while command not in ('1', '2', '3'):
        print("\nUneli ste pogresnu komandu!\n")
        prikaz_svih_korisnika_meni_ispis()
        command = input(">> ")
    return command

def format_header_korisnik():
    return "Korisnicko ime   |Ime            |Prezime                    |Tip korisnika      \n" \
           "-----------------+---------------+---------------------------+--------------------"

def format_korisnik(korisnik):
    return "{0:17}|{1:15}|{2:27}|{3:20}".format(korisnik['korisnicko_ime'], korisnik['ime'], korisnik['prezime'], korisnik['tip_korisnika'])
