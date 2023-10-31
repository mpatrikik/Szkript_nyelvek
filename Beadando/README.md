# Napt�r alkalmaz�s
N�v: Moln�r Patrik
Neptun K�d: RQ8RD0

## R�vid Le�r�s
A prgoram egy napt�rat val�s�t meg ahol tudunk l�ptetni az �vek �s h�napok k�z�tt.
Ha r�kattintunk egy adott napra akkor tudunk hozz�adni esem�nyeket, azokat meg tudjuk n�zni a megfelel� gomb megnyom�s�val. 
A ment�s gombra kattint�s ut�n tudjuk a naphoz tartoz� esem�nyt menteni az "esemenyek.txt" f�jlba.

## Modulok
- `tkinter`: Ez a modul lehet�v� teszi grafikus felhaszn�l�i fel�letek (GUI) l�trehoz�s�t �s kezel�s�t. A programban a tkinter modult haszn�ljuk az ablak �s gombok l�trehoz�s�hoz.
- `scrolledtext`: A scrolledtext modul egy olyan kiterjeszt�se a tkinter-nek, amely lehet�v� teszi g�rgethet� sz�vegdobozok l�trehoz�s�t. Ezt haszn�ljuk az esem�nyek megjelen�t�s�re a megtekint�s gomb haszn�latakor.
- `tkcalendar`: A tkcalendar modul egy napt�r widgetet k�n�l, amelyet a programban haszn�lnak a d�tumok kiv�laszt�s�ra.
- `events_module`: Az events_module egy saj�t modul, amelyek az esem�nyek kezel�s�hez sz�ks�gesek. A modul tartalmazza az esem�nyek hozz�ad�s�t, lek�rdez�s�t �s kezel�s�t.


## F�ggv�nyek
- `add_event()`: Ezzel a f�ggv�nnyel hozz� lehet adni egy esem�nyt a napt�rhoz a kiv�lasztott d�tumhoz. Az esem�ny le�r�sa a sz�vegdobozban tal�lhat�.
- `view_event()`: Ez a f�ggv�ny megjelen�ti az adott napon tal�lhat� esem�nyek list�j�t egy k�l�n felugr� ablakban.
- `save_events()`: Ezzel a f�ggv�nnyel el lehet menteni az adott napi esem�nyt  egy "esemenyek.txt" nev� f�jlba. Az esem�nyek a d�tummal egy�tt ker�lnek a f�jlba, �s mindig hozz�f�zik az �j esem�nyeket a m�r megl�v�kh�z.
- `show_info_with_timeout(title, message, timeout)`: Ezzel a f�ggv�nnyel lehet inform�ci�s �zeneteket megjelen�teni egy p�rbesz�dablakban. Az �zenetes ablak id�tartama, ami megjelenik, a f�ggv�ny param�tereinek megfelel�en �ll�that� be. Ebben az esetben 2,5 mp-ig l�tsz�dik, majd elt�nik(destroy seg�ts�g�vel).
- `show_warning_with_timeout(title, message, timeout)`: Ez a f�gv�ny l�nyeg�ben ugyanaz mint a `show_info_timeout`, csak ebben az esetben a warning-okat vagy error-okat lehet beall�tani.


### A k�d v�g�n tal�lhat� k�dr�szlet a f�program bel�p�si pontjak�nt van jelen. Teh�t l�nyeg�ben az alkalmaz�s fut�s�t ind�tja �s a f� ablakot megjelen�ti a k�perny�n.

## `events_module-py`:
- Az `EventManager` nev� oszt�ly egy egyszer� esem�nykezel�t val�s�t meg:
- Ez teh�t arra szolg�l, hogy esem�nyeket t�roljon �s kezeljen a d�tumok alapj�n. Az `add_event()` met�dussal �j esem�nyeket lehet hozz�adni a rendszerhez, �s a `get_events()` met�dussal pedig lek�rdezhet�k az esem�nyek egy adott d�tumhoz.

## A program haszn�lata
Futtassa a `beadando.py` f�jlt, egy adott napon �llva lehet hozz�adni esem�nyt, azt megtekinteni �s menteni a megfelel� gombok megnyom�s�val. A mentett elemeket az `esemyek.txt` f�jlba menti �s meg lehet tekinteni az el�z�leg hozz�adott esem�nyeket d�tummal list�zva.