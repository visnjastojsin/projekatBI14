import korisnici


def main():
    prijava_na_sistem()

def login():
    username = input("Uneti korisnicko ime:\n>> ")
    password = input("Uneti lozinku:\n>> ")
    return korisnici.korisnik_login(username, password)

def prijava_na_sistem():
    print("Prijava na sistem")
    korisnik = login()
    print(korisnik)
    pokusaji = 1
    while not korisnik and pokusaji < 3:
        print("Pokusajte ponovo!\n")
        korisnik = login()
        pokusaji += 1
    if pokusaji == 3:
        exit()
    if korisnik[0] == "Administrator":
        korisnici.administrator(korisnik[1])
    if korisnik[0] == "Menadzer":
        korisnici.menadzer(korisnik[1])
    if korisnik[0] == "Prodavac":
        korisnici.prodavac(korisnik[1])













if __name__ == "__main__":
    main()
