## Rendszerterv

## A rendszer célja
A klasszikus kirakós játék egyaránt gyermekek és felnőttek kedvence, egyszerű és szórakoztató játék.
A rendszerünk célja, hogy egy ingyenes, digitalizált megoldást hozzon a játékhoz, mely ugyanúgy érdekelhet, és kihívást jelenthet majd minden korosztály számára. Fontos, hogy nem szeretnénk, hogy elveszítse a játék fő érdekességeit,
ne legyen túl bonyolult, elvégre gyerekek, vagy akár idősek is játszhatják.
A kulcs összehangolni a digitalizációt az egyszerűséggel, és nem utolsó sorban, mindez ingyenes.
Egyéb célja a szép kinézet, letisztultság és egyszerűség.
Szeretnénk, ha az ember nem csak a játékban lelné örömét, hanem a játék kinézete is jó érzéssel töltené el.
A felhasználó a puzzle nehézségének megfelelően pontszámot kap, melyeknek összege az előrehaladását jelzi.
A játék webes felületen lesz elérhető, reszponzív megoldásokkal, így mobilról és tabletről is játszhatóvá szeretnénk tenni.

## Üzleti folyamatok modellje

## Követelmények
Felhasználók adatainak, előrehaladásának adatbázisban való tárolása.
Webes környezetben, reszponzívan megjelenő működés.
GDPR-nak való megfelelés.
Felnőtt tartalmak kizárása.

## Funkcionális terv
    - Szerepkörök: 
        - Admin
        - Felhasználó
    - ADMIN:
        - Hozzáfér a felhasználók listájához, tudja őket menedzselni, adataikat módosítani, és törölni.
        - Jogosult új felhasználó felvételére
        - Jogosult mindenre amire a "Felhasználó" szerepkör is
    - FELHASZNÁLÓ:
        - Tud regisztrálni
        - Meg tudja változtatni a jelszavát
        - Eléri a játékfelületet
        - Látja a pontszámait
        - Látja a nehézségi szinteket
        - Tud nehézségi szintet választani
        - Tudja használni a játékfelületet

## Fizikai környezet
Az alkalmazás webes felületre készül, mely reszponzív, tehát mobil eszközökön is jól használható.
Van tűzfal a hálózaton és minden portot is engedélyez.
Nincsenek megvásárolt komponenseink.
- Fejlesztői eszközök:
    - Visual Studio Code
    - Visual Studio Code Live Server Extension
    - SQLite
    - HTML5
    - Javascript (Pixi JS)
    - CSS

## Architekturális terv
Backend:
A rendszerhez szükség van egy adatbázis szerverre.
Ebben az esetben egy SQLite adatbázist fogunk használni.
Ez fogja tárolni a felhasználók belépési adatait, teljesített szintjeit 
és a képeket.
Ebből az datbázisból Java alapú rendszerrel fogjuk kiszedni az adatokat és 
felvinni rá.

Web kliens:
A web alkalmazás Javascript segítségével készül el.
A felületen való navigálás lesz a feladata.
A bevitt adatokat a Java backend fogja ellenőrizni.


## Adatbázis terv

## Implementációs terv
A webes felület főként HTML, CSS és Javascriptet fog használni.
A Javascript lesz felelős a képek betöltéséert és a UI felület kattintható gombjaiért.
A backend Javában fog iródni, ez felelős a követelmények betartatáséert és
az adatbázissal való kommunikációért.
Az adatbázis pedig egy SQLite lesz.
A frontend használni fogja a backend funkcióit, amik kommunikálnak az adatbázissal.
Ezáltal képes lesz adatokat felvinni és lekérni az adatbázisból.

## Tesztterv

## Telepítési terv
A szoftver webes felületéhez csak egy ajánlott böngésző telepítése
szükséges (Google Chrome, Firefox, Opera, Safari),külön szoftver
nem kell hozzá.
A webszerverre közvetlenül az internetről
kapcsolódnak rá a kliensek.
Mobilon vagy tableten ugyanez a követelmény.

## Karbantartási terv