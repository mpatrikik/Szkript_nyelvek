# számológép
# bemeneti rész->
def adatkeres(tipus):
    valasz = ""
    if tipus == "sz":
        valasz = input("Kérem a számot: ")
        while not valasz.isnumeric():
            print("!!!Rossz érték!!!")
            valasz = input("\nKérem a számot: ")
        valasz = int(valasz)
    elif tipus == "m":
        valasz = input("Milyen müveletet végezzek el a megadott számmal?(+ - * /): ")
        while valasz not in ["+", "-", "/", "*"]:
            print("!!!Nem jó a megadaott műveleti jel!!!")
            valasz = input("\nMilyen müveletet végezzek el a megadott számmal?(+ - * /): ")
    return valasz


# műveleti rész->
def szamolas():
    eredmeny = 0
    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    elif muvelet == "/":
        eredmeny = szam1 / szam2
    return eredmeny

# itt van a program indítás->
print("Számológép")

szam1 = adatkeres("sz")

muvelet = adatkeres("m")

szam2 = adatkeres("sz")

eredmenye = szamolas()


# kiiratas->
print(str(szam1).rjust(50))
print(muvelet, end="")
print(str(szam2).rjust(49))
print("_".rjust(50, "_"))
print(str(eredmenye).rjust(50))