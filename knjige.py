import knjigeIO

knjige = knjigeIO.ucitaj_knjige()

def prikaz_svih_knjiga(administrator = False):
    izbor = prikaz_svih_knjiga_meni()
    if izbor == '1':
        sortirane_knjige = sorted(knjige, key=lambda k: k['naslov'])
    elif izbor == '2':
        sortirane_knjige = sorted(knjige, key=lambda k: k['kategorija'])
    elif izbor == '3':
        sortirane_knjige = sorted(knjige, key=lambda k: k['autor'])
    elif izbor == '4':
        sortirane_knjige = sorted(knjige, key=lambda k: k['izdavac'])
    elif izbor == '5':
        sortirane_knjige = sorted(knjige, key=lambda k: k['cena'])
    print(format_header_knjige())
    for knjiga in sortirane_knjige:
        if knjiga['brisanje'] == False or administrator:
            print(format_knjiga(knjiga))

def prikaz_svih_knjiga_meni_ispis():
    print("\nIzaberite opciju:")
    print("1 - Sortiranje po naslovu kjnige")
    print("2 - Sortiranje po kategoriji")
    print("3 - Sortiranje po autoru")
    print("4 - Sortiranje po izdavacu")
    print("5 - Sortiranje po ceni")

def prikaz_svih_knjiga_meni():
    prikaz_svih_knjiga_meni_ispis()
    command = input(">> ")
    while command not in ('1', '2', '3', '4', '5'):
        print("\nUneli ste pogresnu komandu!\n")
        prikaz_svih_knjiga_meni_ispis()
        command = input(">> ")
    return command

def pretraga_svih_knjiga(administrator = False):
    izbor = pretraga_svih_knjiga_meni()
    if izbor == '1':
        sifra = input("Uneti zeljenu sifru:\n>> ")
        sortirane_knjige = pretraga_po_sifri(sifra, "sifra")
    elif izbor == '2':
        sifra = input("Uneti zeljeni naslov:\n>> ")
        sortirane_knjige = pretraga_po_sifri(sifra, "naslov")
    elif izbor == '3':
        sifra = input("Uneti zeljenog autora:\n>> ")
        sortirane_knjige = pretraga_po_sifri(sifra, "autor")
    elif izbor == '4':
        sifra = input("Uneti zeljenu kategoriju:\n>> ")
        sortirane_knjige = pretraga_po_sifri(sifra, "kategorija")
    elif izbor == '5':
        sifra = input("Uneti zeljenog izdavaca:\n>> ")
        sortirane_knjige = pretraga_po_sifri(sifra, "izdavac")
    elif izbor == '6':
        sortirane_knjige = []
        mincena = eval(input("Unesite minimalnu cenu:\n>> "))
        maxcena = eval(input("Unesite maksimalnu cenu:\n>> "))
        for knjiga in knjige:
            if mincena <= knjiga["cena"] <= maxcena:
                sortirane_knjige.append(knjiga)
        sortirane_knjige = sorted(sortirane_knjige, key=lambda k: k['cena'])
    print(format_header_knjige())
    for knjiga in sortirane_knjige:
        if knjiga['brisanje'] == False or administrator:
            print(format_knjiga(knjiga))

def pretraga_po_sifri(sifra, kljuc):
    lista = []
    for knjiga in knjige:
        if sifra.lower() in knjiga[kljuc][:len(sifra)].lower():
            lista.append(knjiga)
    return lista

def pretraga_svih_knjiga_meni_ispis():
    print("\nIzaberite opciju:")
    print("1 - Pretraga po sifri")
    print("2 - Pretraga po naslovu")
    print("3 - Pretraga po autoru")
    print("4 - Pretraga po kategoriji")
    print("5 - Pretraga po izdavacu")
    print("6 - Pretraga po opsegu cene")

def pretraga_svih_knjiga_meni():
    pretraga_svih_knjiga_meni_ispis()
    command = input(">> ")
    while command not in ('1', '2', '3', '4', '5', '6'):
        print("\nUneli ste pogresnu komandu!\n")
        pretraga_svih_knjiga_meni_ispis()
        command = input(">> ")
    return command

def format_header_knjige():
    return "Sifra   |Naslov                                 |Autor                      |ISBN               |Izdavac               |Godina   |Cena    |Kategorija      \n" \
           "--------+---------------------------------------+---------------------------+-------------------+----------------------+---------+--------+----------------"

def format_knjiga(knjiga):
    return "{0:8}|{1:39}|{2:27}|{3:19}|{4:22}|{5:9}|{6:8}|{7:16}".format(knjiga['sifra'], knjiga['naslov'], knjiga['autor'], knjiga['isbn'], knjiga['izdavac'], knjiga['godina'], knjiga['cena'], knjiga['kategorija'])

def dodavanje_knjige():
    lista = []
    for knjiga in knjige:
        lista.append(knjiga['sifra'])
    knjiga = {}
    knjiga['sifra'] = input("Uneti sifru knjige:\n>> ")
    while knjiga['sifra'] in lista:
        print("\nSifra vec postoji, pokusajte ponovo!\n")
        knjiga['sifra'] = input("Uneti sifru knjige:\n>> ")
    lista.clear()
    knjiga['naslov'] = input("Uneti naslov knjige:\n>> ")
    knjiga['autor'] = input("Uneti autora knjige:\n>> ")
    knjiga['isbn'] = input("Uneti isbn knjige:\n>> ")
    knjiga['izdavac'] = input("Uneti izdavaca knjige:\n>> ")
    knjiga['godina'] = int(input("Uneti godinu izdanja knjige:\n>> "))
    knjiga['cena'] = float(input("Uneti cenu knjige:\n>> "))
    knjiga['kategorija'] = input("Uneti kategoriju knjige:\n>> ")
    knjiga['brisanje'] = False
    knjige.append(knjiga)
    knjigeIO.sacuvaj_knjige(knjige)

def izmena_knjige():
    sifra = input("Uneti sifru zeljene knjige:\n>> ")
    postoji = False
    for knjiga in knjige:
        if knjiga['sifra'] == sifra:
            postoji = True
            naziv = input("Uneti naslov knjige:\n>> ")
            if naziv != "":
                knjiga['naslov'] = naziv
            autor = input("Uneti autora knjige:\n>> ")
            if autor != "":
                knjiga['autor'] = autor
            isbn = input("Uneti isbn knjige:\n>> ")
            if isbn != "":
                knjiga['isbn'] = isbn
            izdavac = input("Uneti izdavaca knjige:\n>> ")
            if izdavac != "":
                knjiga['izdavac'] = izdavac
            godina = input("Uneti godinu izdanja knjige:\n>> ")
            if godina != "":
                knjiga['godina'] = int(godina)
            cena = input("Uneti cenu knjige:\n>> ")
            if cena != "":
                knjiga['cena'] = float(cena)
            kategorija = input("Uneti kategoriju knjige:\n>> ")
            if kategorija != "":
                knjiga['kategorija'] = kategorija
            knjigeIO.sacuvaj_knjige(knjige)
            break
    if not postoji:
        print("Ne postoji knjiga sa ovom sifrom!")

def brisanje():
    sifra = input("Uneti sifru zeljene knjige za brisanje:\n>> ")
    postoji = False
    for knjiga in knjige:
        if knjiga['sifra'] == sifra:
            postoji = True
            knjiga['brisnje'] = True
            knjigeIO.sacuvaj_knjige(knjige)
            break
    if not postoji:
        print("Ne postoji knjiga sa ovom sifrom!")

