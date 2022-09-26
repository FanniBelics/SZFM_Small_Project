# Tesztelési jegyzőkönyv

## Manuális tesztek

### Bejelentkező felület
| ID | Név | Leírás | Megfelelés
| ----------- | ----------- | ----------- | ----------- |
| B1 | Eltolódás | A bejelentkezési oldalon a kék terület elmozgatható, ezt a Sign up/in gomb nyomásával érjük el | OK |
| B2 | E-mail formátumú e-maillel regisztrálás | Az e-mail el lesz fogadva | OK |
| B3 | Nem e-mail formátumú e-maillel regisztrálás | Feljön egy üzenet a textbox-ban ami megkér hogy javítsuk ki | OK |
| B4 | E-mail kihagyása regisztrációkor | Nem történik regisztráció, konzolban hiba jelenik meg | OK |
| B5 | Felhasználónév kihagyása regisztrációkor | Nem történik regisztráció, konzolban hiba jelenik meg | OK |
| B6 | Jelszó kihagyása regisztrációkor | Nem történik regisztráció, konzolban hiba jelenik meg | OK |
| B7 | Helyes adatokkal való regisztrálás | Megtörténik a regisztráció, a jelszó titkosítva van az adatbázisban | OK |
| B8 | Belépés regisztrált felhasználóval | Megtörténik a bejelentkezés, megjelenik a játékfelület | OK |
| B9 | Belépés nem regisztrált felhasználóval | Nem történik meg a bejelentkezés | OK |

### Játékfelület
 ID | Név | Leírás | Megfelelés
| ----------- | ----------- | ----------- | ----------- |
| J1 | CSS/JS betöltődés | A játékoldalon megfigyeljük hogy a CSS és JS fájlok betöltődnek, működnek-e | OK |
| J2 | Logout | A Logout gomb megnyomása visszajuttat minket a belépési oldalra | OK |
| J3 | Adatbázis adatok | A bal felső sarokban, láthatóak-e az adatbázisból visszakapott érékek | OK |
| J4 | Admin | Amennyiben a felh. Admin, megjelenik az ADMIN feliratú gomb | OK |
| J5 | Admin oldal | Amennyiben a felh. Admin, a gombra kattintva eljut az admin oldalra | OK |
| J5 | Kockamozgatás | A kockák megjelennek és a mozgathatóak  | OK |
| J6 | Kockamozgatás D&D | A kockákon működik a drag and drop funkció  | OK |
| J7 | Üres kocka | Üres kockát nem lehet a képrészletekkel cserélni  | OK |
| J8 | Megoldhatóság | A puzzle megoldható| OK |
| J9 | Megoldáskép | Az oldalon megjelenik a megoldás képe is, jó kép jelenik meg  | OK |
| J10 | Felcserélhetőség | A nemüres kockák egymással felcserélhetők | OK |
| J11 | Chrome | A játék játszható Google Chrome böngészőben | OK |
| J12 | Nem Admin | Nem admin játékosoknak nem jelenik meg az Admin gomb | OK |
| J13 | Megoldásüzenet |Megoldáskor üzenet pattan fel gombbal kiegészítve | OK |
| J14 | Gomb pontot ad | A gombra kattintva a játékos plusz pontot szerez | OK |
| J15 | Újrakezdés | A pont begyűjtése után a játék újrakezdhető | OK |
| J16 | Egyszeri pont | A pont egyszer gyűjthető be megoldásonként | OK |
| J17 | Hibás megoldás | Amennyiben a puzzle minden darabja a táblán van, de nincs a helyén, nem jelenik meg a pontgyűjtő gomb | OK |




### Admin felület
 ID | Név | Leírás | Megfelelés
| ----------- | ----------- | ----------- | ----------- |
| A1 | Egy felhasználó törlése | A kijelölt felhasználó törlődik a felületről és adatbázisból is | OK |
| A2 | Több felhasználó törlése | A kijelölt felhasználók törlődnek a felületről és adatbázisból is | OK |
| A3 | Nulla felhasználó törlése | Nem történik semmi, csak frissül az oldal | OK |
| A4 | Vissza navigálás | Megjelenik a játékfelület újra | OK |


