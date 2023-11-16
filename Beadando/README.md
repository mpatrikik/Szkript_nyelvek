# Naptár alkalmazás
Név: Molnár Patrik
Neptun Kód: RQ8RD0

## Rövid Leírás
A prgoram egy naptárat valósít meg ahol tudunk léptetni az évek és hónapok között.
Ha rákattintunk egy adott napra akkor tudunk hozzáadni/menteni eseményeket, azokat meg tudjuk nézni a megfelelõ gomb megnyomásával. 
A mentés gombra kattintás után tudjuk a naphoz tartozó eseményt menteni az "esemenyek.txt" fájlba.
A törlés is lehetséges ha az adott naphoz nem szeretnénk tovább eseményeket tárolni.

## Modulok
- `tkinter`: Ez a modul lehetõvé teszi grafikus felhasználói felületek (GUI) létrehozását és kezelését. A programban a tkinter modult használjuk az ablak és gombok létrehozásához.
- `scrolledtext`: A scrolledtext modul egy olyan kiterjesztése a tkinter-nek, amely lehetõvé teszi görgethetõ szövegdobozok létrehozását. Ezt használjuk az események megjelenítésére a megtekintés gomb használatakor.
- `tkcalendar`: A tkcalendar modul egy naptár widgetet kínál, amelyet a programban használnak a dátumok kiválasztására.
- `os`: Ez a modul lényegében az operációs rendszer specifikus mûveleteket végrehajtásához szükséges és lehetõvé teszi a program és az OP-rendszer közötti kommunikációt. Ebben az esetben a fájlmûveleteket végzünk ennek a segítségével.


## Függvények
- `save_events()`: Ezzel a függvénnyel el lehet menteni az adott napi eseményt  egy "esemenyek.txt" nevû fájlba. Az események a dátummal együtt kerülnek
- `delete_events()`: Ez azt szolgálja, hogy az adott napon állva az összes eseményt kitörli.
- `delete_all_events()`: Ez a függvény törli az összes eseményt a fájlból.
- `load_events()`: Az alkalmazás inicializálásakor hívódik meg, amikor a naptár osztály példányosításával létrejön az ablak. Ellenõrzi, hogy az `esemenyek.txt` fájl létezik-e, ha nem akkor létrejön. Majd beolvassa a a fájlt, hogy ki tudjuk listázni az eseményeket az adott naphoz.
- `view_event()`: Ez a függvény megjeleníti az adott napon található események listáját egy külön felugró ablakban.
 a fájlba, és mindig hozzáfûzik az új eseményeket a már meglévõkhöz.
- `list_all_events()`: Ez listázza az összes eseményt a fájlból.

- `show_info_with_timeout(title, message, timeout)`: Ezzel a függvénnyel lehet információs üzeneteket megjeleníteni egy párbeszédablakban. Az üzenetes ablak idõtartama, ami megjelenik, a függvény paramétereinek megfelelõen állítható be. Ebben az esetben 2,5 mp-ig látszódik, majd eltûnik(destroy segítségével).
- `show_warning_with_timeout(title, message, timeout)`: Ez a fügvény lényegében ugyanaz mint a `show_info_timeout`, csak ebben az esetben a warning-okat vagy error-okat lehet beallítani.


### A kód végén található kódrészlet a fõprogram belépési pontjaként van jelen. Tehát lényegében az alkalmazás futását indítja és a fõ ablakot megjeleníti a képernyõn.

## A program használata
Futtassa a `beadando.py` fájlt, egy adott napon állva lehet menteni egy eseményt és azt megtekinteni megfelelõ gombok megnyomásával. A mentett elemeket az `esemyek.txt` fájlba menti és meg lehet tekinteni az elõzõleg hozzáadott eseményeket dátummal listázva.