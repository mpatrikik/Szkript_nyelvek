# Naptár alkalmazás
Név: Molnár Patrik
Neptun Kód: RQ8RD0

## Rövid Leírás
A prgoram egy naptárat valósít meg ahol tudunk léptetni az évek és hónapok között.
Ha rákattintunk egy adott napra akkor tudunk hozzáadni eseményeket, azokat meg tudjuk nézni a megfelelõ gomb megnyomásával. 
A mentés gombra kattintás után tudjuk a naphoz tartozó eseményt menteni az "esemenyek.txt" fájlba.

## Modulok
- `tkinter`: Ez a modul lehetõvé teszi grafikus felhasználói felületek (GUI) létrehozását és kezelését. A programban a tkinter modult használjuk az ablak és gombok létrehozásához.
- `scrolledtext`: A scrolledtext modul egy olyan kiterjesztése a tkinter-nek, amely lehetõvé teszi görgethetõ szövegdobozok létrehozását. Ezt használjuk az események megjelenítésére a megtekintés gomb használatakor.
- `tkcalendar`: A tkcalendar modul egy naptár widgetet kínál, amelyet a programban használnak a dátumok kiválasztására.
- `events_module`: Az events_module egy saját modul, amelyek az események kezeléséhez szükségesek. A modul tartalmazza az események hozzáadását, lekérdezését és kezelését.


## Függvények
- `add_event()`: Ezzel a függvénnyel hozzá lehet adni egy eseményt a naptárhoz a kiválasztott dátumhoz. Az esemény leírása a szövegdobozban található.
- `view_event()`: Ez a függvény megjeleníti az adott napon található események listáját egy külön felugró ablakban.
- `save_events()`: Ezzel a függvénnyel el lehet menteni az adott napi eseményt  egy "esemenyek.txt" nevû fájlba. Az események a dátummal együtt kerülnek a fájlba, és mindig hozzáfûzik az új eseményeket a már meglévõkhöz.
- `show_info_with_timeout(title, message, timeout)`: Ezzel a függvénnyel lehet információs üzeneteket megjeleníteni egy párbeszédablakban. Az üzenetes ablak idõtartama, ami megjelenik, a függvény paramétereinek megfelelõen állítható be. Ebben az esetben 2,5 mp-ig látszódik, majd eltûnik(destroy segítségével).
- `show_warning_with_timeout(title, message, timeout)`: Ez a fügvény lényegében ugyanaz mint a `show_info_timeout`, csak ebben az esetben a warning-okat vagy error-okat lehet beallítani.


### A kód végén található kódrészlet a fõprogram belépési pontjaként van jelen. Tehát lényegében az alkalmazás futását indítja és a fõ ablakot megjeleníti a képernyõn.

## `events_module-py`:
- Az `EventManager` nevû osztály egy egyszerû eseménykezelõt valósít meg:
- Ez tehát arra szolgál, hogy eseményeket tároljon és kezeljen a dátumok alapján. Az `add_event()` metódussal új eseményeket lehet hozzáadni a rendszerhez, és a `get_events()` metódussal pedig lekérdezhetõk az események egy adott dátumhoz.

## A program használata
Futtassa a `beadando.py` fájlt, egy adott napon állva lehet hozzáadni eseményt, azt megtekinteni és menteni a megfelelõ gombok megnyomásával. A mentett elemeket az `esemyek.txt` fájlba menti és meg lehet tekinteni az elõzõleg hozzáadott eseményeket dátummal listázva.