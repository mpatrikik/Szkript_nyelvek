# Jövedelemszámítás
print("Jövedelemszámítás\n")
kor = int(input("Hány éves vagy? "))
if kor > 25:
    gyerek = input("Van 3 gyereked és nő vagy (igen/nem)?")
    if gyerek not in ["igen", "Igen", "IGEN", "I", "i", "yes", "nem", "n", "Nem"]:
        gyerek = input("HIBA \nVan 3 gyereked és nő vagy (igen/nem)?")
brutto = int(input("Mennyi a bruttó jövedelmed: "))
if kor <= 25 or gyerek in ["igen", "Igen", "IGEN", "I", "i", "yes"]:
    if brutto > 500000:
        szja = (brutto - 500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15

print("SZJA:".ljust(25,"_"), str(int(szja)).rjust(10,"_"), "Ft", sep="")
print("Nyudgíj:".ljust(25,"_"), str(int(brutto * 0.1)).rjust(10,"_"), "Ft", sep="")
print("EÜ:".ljust(25,"_"), str(int(brutto * 0.07)).rjust(10,"_"), "Ft", sep="")
print("Munkanélküli segély:".ljust(25,"_"), str(int(brutto * 0.015)).rjust(10,"_"), "Ft", sep="")
print("")
print("Nettó bér:".ljust(25,"_"), str(int(brutto - (brutto * 0.185) - szja)).rjust(10,"_"), "Ft", sep="")