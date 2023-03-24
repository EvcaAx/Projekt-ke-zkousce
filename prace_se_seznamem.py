from pojistenec import Pojistenec
pojistenci: list[Pojistenec] = [Pojistenec(jmeno='Karel', prijmeni='Heřmánek', vek='78', telefon='569158741'),
Pojistenec(jmeno='Alžběta', prijmeni='Nováková', vek='36', telefon='547854123'),
Pojistenec(jmeno='Jiřina', prijmeni='Kabíčková', vek='58', telefon='541258919')]
class OperaceSeSeznamem:

    def vyber_cinnosti(self):
        volba = input("Zvolte operaci: \n 1 - Zadání nového pojištěnce\n 2 - Vypsat všechny pojištěnce\n 3 - Vyhledat pojištěnce\n 4 - Vymazat pojištěnce\n 5 - Konec\n")
        print()
        if volba == "1":
            OperaceSeSeznamem.pridani_pojistence(self)
        elif volba == "2":
            OperaceSeSeznamem.vypsat_pojistence(self)
        elif volba == "3":
            OperaceSeSeznamem.tisk_vyhledaneho_pojistence(self)
        elif volba == "4":
            OperaceSeSeznamem.vymazat_pojistence(self)
        elif volba == "5":
            OperaceSeSeznamem.ukonceni(self)
        else:
            print("Neplatná volba!!\n")
            OperaceSeSeznamem.vyber_cinnosti(self)


    def pridani_pojistence(self):
        pokracovat = True
        while pokracovat:
            jmeno = input("Zadejte jméno:\n").strip().lower().capitalize()
            prijmeni = input("Zadejte příjmení:\n").strip().lower().capitalize()
            vek = ""
            while not vek.isdigit():
                vek = input("Zadejte věk: \n")
                if not vek.isdigit():
                    print("Věk musí být zadán jako celé číslo!")
            telefon = input("Zadejte telefon: \n")
            pojistenci.append(Pojistenec(jmeno, prijmeni, vek, telefon))
            print(f"Osoba {jmeno} {prijmeni} byla úspěšně přídána.\n")
            if OperaceSeSeznamem.dalsi_pojistenec_dotaz(self):
                pokracovat = True
            else:
                pokracovat = False


    def dalsi_pojistenec_dotaz(self):
        nezadano = True
        while nezadano:
            odpoved = input("Chcete zadat dalšího pojištěnce? a/n\n")
            if (odpoved == "a" or odpoved == "A"):
                return True
            elif (odpoved == "n" or odpoved == "N"):
                return False
            else:
                pass


    def vypsat_pojistence(self):
        for i in pojistenci:
            print(i)
        return True


    def vyhledat_pojistence(self):
        hledany_jmeno = input("Zadejte jméno pojištěného:\n ").strip().lower().capitalize()
        hledany_prijmeni = input("Zadejte příjmení: \n ").strip().lower().capitalize()
        print()
        for i in pojistenci:
            if hledany_jmeno == i.jmeno and hledany_prijmeni == i.prijmeni:
               return i


    def tisk_vyhledaneho_pojistence(self):
        p = OperaceSeSeznamem.vyhledat_pojistence(self)
        if p:
            print("Nalezeno:\n", p)
        else:
            print("Nenalezen žádný záznam")

    def vymazat_pojistence(self):
        p = OperaceSeSeznamem.vyhledat_pojistence(self)
        if p:
            print("Nalezený záznam:", p)
            odpoved = False
            while odpoved == False:
                zrusit = input("Opravdu si přejete VYMAZAT tohoto pojištěnce? a/n\n").lower()
                if zrusit == "a":
                    pojistenci.remove(p)
                    print(f"Osoba {p.jmeno} {p.prijmeni} byla úspěšně odstraněna z evidence.")
                    odpoved = True
                elif zrusit == "n":
                    print("Operace zrušena.")
                    odpoved = True
                else:
                    print("Neplatná volba.")
                    odpoved = False
        else:
            print("Záznam nenalezen!")


    def ukonceni(self):
        print("Děkujeme za použití naší aplikace.")
        exit()

    def pokracovani(self):
        print()
        print("Pokračujte stiskem libovolné klávesy....", end=" ")
        input()
        OperaceSeSeznamem.vykresli(self)

    def vykresli(self):
        print()
        print("------------------------------------- \n EVIDENCE POJIŠTĚNÝCH\n--------------------------------------")
        OperaceSeSeznamem.vyber_cinnosti(self)

