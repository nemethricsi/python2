from sharpie import Sharpie
from sharpieSet import SharpieSet

tolltarto = SharpieSet()
print(tolltarto.sharpies)

# példányosítunk 2 filcet:
sarga = Sharpie('sárga', 4.5)
kek = Sharpie('kék', 2)

# hozzáadjuk a tolltartohoz
tolltarto.add(sarga)
tolltarto.add(kek)
print(tolltarto.sharpies)

# a sárgát használjuk 100-szor, kiürül
for _ in range(100):
    sarga.use()

print('hasznalhato filcek: ' + str(tolltarto.count_usable()))

tolltarto.remove_trash()

# már csak a kék van a tolltartóban:
for sharpie in tolltarto.sharpies:
    print(sharpie.szin)
