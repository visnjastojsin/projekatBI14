import knjige
import akcije
import datetime
import racuniIO
korpa = []
racuni = racuniIO.ucitaj_racune()

def prodaja_knjiga(prodavac):
    izbor = '0'
    while izbor.upper() != 'X':
        izbor = prodaja_knjiga_izbor()
        if izbor == '1':
            postoji = False
            sifra = input("Unesite sifru knjige:\n>> ")
            broj = eval(input("Unesite broj knjiga:\n>> "))
            for knjiga in knjige.knjige:
                if knjiga['sifra'] == sifra:
                    korpa.append((knjiga, broj, 'knjiga'))
                    postoji = True
                    break
            if not postoji:
                print("Ne postoji sifra za ovu knjigu!")
        elif izbor == '2':
            postoji = False
            sifra = input("Unesite sifru akcije:\n>> ")
            broj = eval(input("Unesite broj akcija: \n>> "))
            for akcija in akcije.akcije:
                if akcija['sifra'] == sifra and str(datetime.datetime.now().date()) < akcija['datum_vazenja']:
                    korpa.append((akcija, broj, 'akcija'))
                    postoji = True
                    break
            if not postoji:
                print("Ne postoji sifra za ovu akciju!")
        elif izbor == '3':
            suma = 0
            print(format_header_racun())
            for stvar in korpa:
                if stvar[2] == 'knjiga':
                    suma += stvar[0]['cena'] * stvar[1]
                    print(format_racun(stvar[0], stvar[1]))
                if stvar[2] == 'akcija':
                    for knjiga in stvar[0]['artikli']:
                        suma += knjiga['cena'] * stvar[1]
                        print(format_racun(knjiga, stvar[1]))
            print("Ukupna suma je: {0}".format(suma))
        elif izbor == '4':
            racun = {}
            racun['sifra'] = len(racuni) + 1
            racun['prodavac'] = prodavac['korisnicko_ime']
            racun['datum_vreme'] = str(datetime.datetime.now())
            racun['knjige'] = []
            racun['akcije'] = []
            racun['ukupna_cena'] = 0
            for stvar in korpa:
                if stvar[2] == 'knjiga':
                    racun['ukupna_cena'] += stvar[0]['cena'] * stvar[1]
                    racun['knjige'].append((stvar[0], stvar[1]))
                if stvar[2] == 'akcija':
                    for knjiga in stvar[0]['artikli']:
                        racun['ukupna_cena'] += knjiga['cena'] * stvar[1]
                    racun['akcije'].append((stvar[0], stvar[1]))
            racuni.append(racun)
            racuniIO.sacuvaj_racune(racuni)
        elif izbor == 'X':
            return

def prodaja_knjiga_izbor_ispis():
    print("\nIzaberite opciju:")
    print("1 - Unos sifre knjige")
    print("2 - Unos sifre akcije")
    print("3 - Pregled korpe")
    print("4 - Potvrda kupovine")
    print("X - Povratak nazad")

def prodaja_knjiga_izbor():
    prodaja_knjiga_izbor_ispis()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', 'X'):
        print("\nUneli ste pogresnu komandu!\n")
        prodaja_knjiga_izbor_ispis()
        command = input(">> ")
    return command

def format_header_racun():
    return "Sifra   |Naslov                                 |Autor                      |ISBN               |Izdavac               |Godina   |Cena    |Kategorija          |Kom  \n" \
           "--------+---------------------------------------+---------------------------+-------------------+----------------------+---------+--------+--------------------+-----"

def format_racun(knjiga, broj):
    return "{0:8}|{1:39}|{2:27}|{3:19}|{4:22}|{5:9}|{6:8}|{7:20}|{8:5}".format(knjiga['sifra'], knjiga['naslov'], knjiga['autor'], knjiga['isbn'], knjiga['izdavac'], knjiga['godina'], knjiga['cena'], knjiga['kategorija'], broj)

def izvestaji():
    izbor = izvestaji_izbor()
    if izbor == '1':
        izvestaj1()
    elif izbor == '2':
        izvestaj2()
    elif izbor == '3':
        autor = input("Uneti autora:\n>> ")
        izvestaj3(autor, 'autor')
    elif izbor == '4':
        izdavac = input("Uneti izdavaca:\n>> ")
        izvestaj3(izdavac, 'izdavac')
    elif izbor == '5':
        kategorija = input("Uneti kategoriju:\n>> ")
        izvestaj3(kategorija, 'kategorija')

def izvestaji_ispis():
    print("\nIzaberite opciju:")
    print("1 - Ukupna prodaja svih knjiga")
    print("2 - Ukupna prodaja svih akcija")
    print("3 - Ukupna prodaja svih knjiga odabranog autora")
    print("4 - Ukupna prodaja svih knjiga odabranog izdavača")
    print("5 - Ukupna prodaja svih knjiga odabrane kategorije")
    print("X - Povratak nazad")

def izvestaji_izbor():
    izvestaji_ispis()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', 'X'):
        print("\nUneli ste pogresnu komandu!\n")
        izvestaji_ispis()
        command = input(">> ")
    return command

def format_header_zarada():
    return "Sifra   |Naslov                                 |Autor                      |ISBN               |Izdavac               |Godina   |Cena    |Kategorija          |Kom  |Zarada  \n" \
           "--------+---------------------------------------+---------------------------+-------------------+----------------------+---------+--------+--------------------+-----+--------"

def format_zarada(knjiga, broj, zarada):
    return "{0:8}|{1:39}|{2:27}|{3:19}|{4:22}|{5:9}|{6:8}|{7:20}|{8:5}|{9:8}".format(knjiga['sifra'], knjiga['naslov'], knjiga['autor'], knjiga['isbn'], knjiga['izdavac'], knjiga['godina'], knjiga['cena'], knjiga['kategorija'], broj, zarada)

def format_header_akcije_zarada():
    return "Sifra   |Naslov knjige                          |Nova cena          |Stara cena         |Datum          |Kom  |Zarada   \n" \
           "--------+---------------------------------------+-------------------+-------------------+---------------+-----+---------"

def format_akcija1_zarada(akcija, kom, zarada):
    return "{0:8}|{1:39}|{2:19}|{3:19}|{4:15}|{5:5}|{6:9}".format(akcija['sifra'], akcija['artikli'][0]['naslov'], akcija['artikli'][0]['cena'], akcija['artikli'][0]['stara_cena'], akcija['datum_vazenja'], kom, zarada)

def format_akcija2_zarada(akcija, i):
    return "{0:8}|{1:39}|{2:19}|{3:19}|{4:15}|{5:5}|{6:9}".format("", akcija['artikli'][i]['naslov'], akcija['artikli'][i]['cena'], akcija['artikli'][i]['stara_cena'], "", "", "")

def izvestaj1():
    print(format_header_zarada())
    for knjiga in knjige.knjige:
        br = 0
        zarada = 0
        for racun in racuni:
            for knjiga2 in racun['knjige']:
                if knjiga2[0]['sifra'] == knjiga['sifra']:
                    br+=knjiga2[1]
                    zarada += knjiga2[0]['cena'] * knjiga2[1]
            for akcija in racun['akcije']:
                for knjiga2 in akcija[0]['artikli']:
                    if knjiga2['sifra'] == knjiga['sifra']:
                        br += akcija[1]
                        zarada += knjiga2['cena'] * akcija[1]
        print(format_zarada(knjiga, br, zarada))

def izvestaj2():
    for akcija in akcije.akcije:
        print(format_header_akcije_zarada())
        br = 0
        zarada = 0
        for racun in racuni:
            for akcija2 in racun['akcije']:
                if akcija['sifra'] == akcija2[0]['sifra']:
                    br += akcija2[1]
                    for knjiga in akcija2[0]['artikli']:
                        zarada += knjiga['cena'] * akcija2[1]
        print(format_akcija1_zarada(akcija, br, zarada))
        for i in range(1, len(akcija['artikli'])):
            print(format_akcija2_zarada(akcija, i))
        print()
        print()

def izvestaj3(vrednost, tip):
    print(format_header_zarada())
    for knjiga in knjige.knjige:
        if knjiga[tip] == vrednost:
            br = 0
            zarada = 0
            for racun in racuni:
                for knjiga2 in racun['knjige']:
                    if knjiga2[0]['sifra'] == knjiga['sifra']:
                        br += knjiga2[1]
                        zarada += knjiga2[0]['cena'] * knjiga2[1]
                for akcija in racun['akcije']:
                    for knjiga2 in akcija[0]['artikli']:
                        if knjiga2['sifra'] == knjiga['sifra']:
                            br += akcija[1]
                            zarada += knjiga2['cena'] * akcija[1]
            print(format_zarada(knjiga, br, zarada))

