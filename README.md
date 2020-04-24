# Python Haladó (megoldások)

## Feladat 1

Készíts egy PostIt osztályt, amelynek van 3 tagváltozója:

- `hatterSzin`
- `szoveg` ami rajta van
- `szovegSzin`
  Készíts pár példa objektumot:
- sárga posztit kék szöveggel: "Első ötlet"
- rózsaszínű posztit fekete szöveggel: "Hurrá!"
- zöld posztit barna szöveggel: "Szuper!"

# Megoldás:

```py
class PostIt:
    def __init__(self, hatterSzin, szoveg, szovegSzin):
        self._hatterSzin = hatterSzin
        self._szoveg = szoveg
        self._szovegSzin = szovegSzin

sárga = PostIt('sárga', 'Első ötlet', 'kék')
rózsaszín = PostIt('rózsaszín', 'Hurrá!', 'fekete')
zöld = PostIt('zöld', 'Szuper!', 'barna')
```
