# Napt�r alkalmaz�s
N�v: Moln�r Patrik
Neptun K�d: RQ8RD0

## R�vid Le�r�s
A prgoram egy napt�rat val�s�t meg ahol tudunk l�ptetni az �vek �s h�napok k�z�tt.
Ha r�kattintunk egy adott napra akkor tudunk hozz�adni/menteni esem�nyeket, azokat meg tudjuk n�zni a megfelel� gomb megnyom�s�val. 
A ment�s gombra kattint�s ut�n tudjuk a naphoz tartoz� esem�nyt menteni az "esemenyek.txt" f�jlba.
A t�rl�s is lehets�ges ha az adott naphoz nem szeretn�nk tov�bb esem�nyeket t�rolni.

## Modulok
- `tkinter`: Ez a modul lehet�v� teszi grafikus felhaszn�l�i fel�letek (GUI) l�trehoz�s�t �s kezel�s�t. A programban a tkinter modult haszn�ljuk az ablak �s gombok l�trehoz�s�hoz.
- `scrolledtext`: A scrolledtext modul egy olyan kiterjeszt�se a tkinter-nek, amely lehet�v� teszi g�rgethet� sz�vegdobozok l�trehoz�s�t. Ezt haszn�ljuk az esem�nyek megjelen�t�s�re a megtekint�s gomb haszn�latakor.
- `tkcalendar`: A tkcalendar modul egy napt�r widgetet k�n�l, amelyet a programban haszn�lnak a d�tumok kiv�laszt�s�ra.
- `os`: Ez a modul l�nyeg�ben az oper�ci�s rendszer specifikus m�veleteket v�grehajt�s�hoz sz�ks�ges �s lehet�v� teszi a program �s az OP-rendszer k�z�tti kommunik�ci�t. Ebben az esetben a f�jlm�veleteket v�gz�nk ennek a seg�ts�g�vel.


## F�ggv�nyek
- `save_events()`: Ezzel a f�ggv�nnyel el lehet menteni az adott napi esem�nyt  egy "esemenyek.txt" nev� f�jlba. Az esem�nyek a d�tummal egy�tt ker�lnek
- `delete_events()`: Ez azt szolg�lja, hogy az adott napon �llva az �sszes esem�nyt kit�rli.
- `delete_all_events()`: Ez a f�ggv�ny t�rli az �sszes esem�nyt a f�jlb�l.
- `load_events()`: Az alkalmaz�s inicializ�l�sakor h�v�dik meg, amikor a napt�r oszt�ly p�ld�nyos�t�s�val l�trej�n az ablak. Ellen�rzi, hogy az `esemenyek.txt` f�jl l�tezik-e, ha nem akkor l�trej�n. Majd beolvassa a a f�jlt, hogy ki tudjuk list�zni az esem�nyeket az adott naphoz.
- `view_event()`: Ez a f�ggv�ny megjelen�ti az adott napon tal�lhat� esem�nyek list�j�t egy k�l�n felugr� ablakban.
 a f�jlba, �s mindig hozz�f�zik az �j esem�nyeket a m�r megl�v�kh�z.
- `list_all_events()`: Ez list�zza az �sszes esem�nyt a f�jlb�l.

- `show_info_with_timeout(title, message, timeout)`: Ezzel a f�ggv�nnyel lehet inform�ci�s �zeneteket megjelen�teni egy p�rbesz�dablakban. Az �zenetes ablak id�tartama, ami megjelenik, a f�ggv�ny param�tereinek megfelel�en �ll�that� be. Ebben az esetben 2,5 mp-ig l�tsz�dik, majd elt�nik(destroy seg�ts�g�vel).
- `show_warning_with_timeout(title, message, timeout)`: Ez a f�gv�ny l�nyeg�ben ugyanaz mint a `show_info_timeout`, csak ebben az esetben a warning-okat vagy error-okat lehet beall�tani.


### A k�d v�g�n tal�lhat� k�dr�szlet a f�program bel�p�si pontjak�nt van jelen. Teh�t l�nyeg�ben az alkalmaz�s fut�s�t ind�tja �s a f� ablakot megjelen�ti a k�perny�n.

## A program haszn�lata
Futtassa a `beadando.py` f�jlt, egy adott napon �llva lehet menteni egy esem�nyt �s azt megtekinteni megfelel� gombok megnyom�s�val. A mentett elemeket az `esemyek.txt` f�jlba menti �s meg lehet tekinteni az el�z�leg hozz�adott esem�nyeket d�tummal list�zva.