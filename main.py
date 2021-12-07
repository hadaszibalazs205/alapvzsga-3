'''
Nyitvatartás.
Egy bolt pontban reggel nyolc órakor nyit, és pontban délután tizenhat órakor zár be – azaz 8:00‑kor már nyitva van és 16:00-kor már nincs nyitva.
A program kérjen be egy egész órát jelző számot a felhasználótól, majd írja ki, hogy a megadott időpontban nyitva van-e a bolt! 
Amennyiben igen, akkor azt is írja ki, hogy mennyi idő van még zárásig, azaz hány egész óra áll rendelkezésre odaérni a boltba! 
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Hány óra van most? 8
A bolt nyitva van.
Ennyi órád van még odaérni: 8
-----
Hány óra van most? 7
A bolt zárva van.
-----
Hány óra van most? 17
A bolt zárva van.
-----
Hány óra van most? 16
A bolt zárva van.
-----
Hány óra van most? 12
A bolt nyitva van.
Ennyi órád van még odaérni: 4
'''



zaras = 16

ora = int(input("Hány óra van most? "))

if ora >= 8 and ora < zaras:
    print(f"A bolt nyitva van.\n Ennyi órád van még odaérni: {zaras - ora}")
if ora < 8 or ora >= 16:
    print("A bolt zárva van")