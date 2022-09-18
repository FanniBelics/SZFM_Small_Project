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

## Adatbázis terv

## Implementációs terv

## Tesztterv

## Telepítési terv

## Karbantartási terv