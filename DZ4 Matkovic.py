
import time
import os

def kontrolirani_unos():
    uneseni_broj = int(input("Unesi broj čiji faktorijel želiš izračunati: "))
    # broj_max_pokusaja = 5 #osiguranje od beskonačne petlje

    while uneseni_broj < 0:
        uneseni_broj = int(input("Molim unesi broj veći od 0: "))
        # broj_max_pokusaja -= 1
        # if broj_max_pokusaja == 0:
        #     print("Previše pokušaja. Program se zatvara.")
        #     break
    return uneseni_broj

def faktorijel(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorijel(n - 1)

def memo_faktorijel(n, memo):
    if n in memo:  # Ako je već izračunat, uzmi iz memorije
        return memo[n]
    if n == 0 or n == 1:  # 0! = 1, 1! = 1
        return 1

    rezultat = n * memo_faktorijel(n - 1, memo)
    memo[n] = rezultat  
    return rezultat

def main():
    uneseni_broj = kontrolirani_unos()

    # Otvaranje datoteke i spremanje u direktorij gdje je skripta. Datoteka se automatski zatvara
    with open("Faktorijeli_usporedba.txt", "w") as datoteka:
        datoteka.write(f"Uneseni broj: {uneseni_broj}\n\n")

        # Računanje i ispis faktorijela bez memoizacije
        pocetno_vrijeme1 = time.time()
        datoteka.write(f"Ispis svih faktorijela od 0 do {uneseni_broj} (bez spremanja u memoriju):\n")
        print(f"Ispis svih faktorijela od 0 do {uneseni_broj} (bez spremanja u memoriju):")

        for i in range(uneseni_broj + 1):  # Uzimanje u obzir i uneseni broj
            faktorijel_rezultat = faktorijel(i)  # Poziv funkcije za računanje faktorijela
            redak = f"{i}! = {faktorijel_rezultat}\n"
            print(redak, end="")
            datoteka.write(redak)

        zavrsno_vrijeme1 = time.time()
        trajanje1 = zavrsno_vrijeme1 - pocetno_vrijeme1
        trajanje1_zaokruzeno = f"{trajanje1:.5f}"
        print(f"Operacija je trajala {trajanje1_zaokruzeno} sekundi.")
        datoteka.write(f"Operacija je trajala {trajanje1_zaokruzeno} sekundi.\n\n")

        # Računanje i ispis faktorijela s memoizacijom
        memo = {}
        pocetno_vrijeme2 = time.time()

        datoteka.write(f"\nIspis svih faktorijela od 0 do {uneseni_broj} (sa spremanjem u memoriju):\n")
        print(f"\nIspis svih faktorijela od 0 do {uneseni_broj} (sa spremanjem u memoriju):")

        for i in range(uneseni_broj + 1):
            faktorijel_rezultat = memo_faktorijel(i, memo)  # Poziv funkcije za memoizaciju
            redak = f"{i}! = {faktorijel_rezultat}\n"
            print(redak, end="")
            datoteka.write(redak)

        zavrsno_vrijeme2 = time.time()
        trajanje2 = zavrsno_vrijeme2 - pocetno_vrijeme2
        trajanje2_zaokruzeno = f"{trajanje2:.5f}"

        print(f"Operacija je trajala {trajanje2_zaokruzeno} sekundi.")
        datoteka.write(f"Operacija je trajala {trajanje2_zaokruzeno} sekundi.\n")

    # Direktorij/putanja ispisana, nisam koristio bez korištenja personalizirane
    print(f"\nDatoteka je spremljena u direktorij: {os.getcwd()}\n")

if __name__ == "__main__":
    main()
