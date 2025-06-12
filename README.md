# Faktorijel Usporedba: Rekurzija vs. Memoizacija

Ovaj Python program omogućuje korisniku unos broja i uspoređuje vrijeme izvođenja algoritma za izračun faktorijela pomoću:

- **Klasične rekurzije**
- **Memoizirane rekurzije (dinamičko programiranje)**

Rezultati, uključujući sve faktorijele od 0 do unesenog broja i vrijeme izvođenja, spremaju se u tekstualnu datoteku `Faktorijeli_usporedba.txt` u istom direktoriju gdje se izvršava skripta.

## Sadržaj

- [Značajke](#značajke)
- [Kako koristiti](#kako-koristiti)
- [Primjeri izlaza](#primjeri-izlaza)
- [Tehnički detalji](#tehnički-detalji)
- [Napomene](#napomene)

## Značajke

- Interaktivan unos broja s provjerom ispravnosti (nema negativnih brojeva)
- Računanje faktorijela dvama metodama
- Precizno mjerenje vremena izvođenja
- Automatsko spremanje rezultata u `.txt` datoteku
- Ispis rezultata u terminal i u datoteku

## Kako koristiti

1. Kloniraj repozitorij:
   ```bash
   git clone https://github.com/tvoje_korisnicko_ime/ime_repozitorija.git
   cd ime_repozitorija
   ```

2. Pokreni program:
   ```bash
   python ime_datoteke.py
   ```

3. Unesi broj za koji želiš izračunati sve faktorijele do tog broja (npr. 10).

4. Rezultati i usporedba izvođenja bit će prikazani u terminalu i zapisani u datoteku `Faktorijeli_usporedba.txt`.

## Primjeri izlaza

```
Uneseni broj: 5

Ispis svih faktorijela od 0 do 5 (bez spremanja u memoriju):
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
Operacija je trajala 0.00012 sekundi.

Ispis svih faktorijela od 0 do 5 (sa spremanjem u memoriju):
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
Operacija je trajala 0.00004 sekundi.

Datoteka je spremljena u direktorij: /tvoj/put
```

## Tehnički detalji

- Jezik: Python 3
- Modul(i): `time`, `os`
- Tehnike: rekurzija, memoizacija (korištenjem rječnika kao cache)
- Način pohrane: `with open(..., "w")` za automatsko zatvaranje datoteke

## Napomene

- Za veće ulazne brojeve (npr. >1000) može doći do `RecursionError`, jer Python ima ograničenje na dubinu rekurzije.
- Moguće je dodatno proširiti program uporabom iterativne metode ili ugrađene `math.factorial()` funkcije za usporedbu.
- Zakomentirani dijelovi s brojem pokušaja mogu se aktivirati radi zaštite od beskonačnog unosa.

---

✅ Slobodno koristi, mijenjaj i proširuj projekt za potrebe učenja rekurzije, optimizacije i performansi!