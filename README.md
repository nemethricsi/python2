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

### Megoldás:

```python
class PostIt:
    def __init__(self, hatterSzin, szoveg, szovegSzin):
        self._hatterSzin = hatterSzin
        self._szoveg = szoveg
        self._szovegSzin = szovegSzin

sárga = PostIt('sárga', 'Első ötlet', 'kék')
rózsaszín = PostIt('rózsaszín', 'Hurrá!', 'fekete')
zöld = PostIt('zöld', 'Szuper!', 'barna')
```

## Feladat 2

- Készíts egy `Allat` osztályt
- Minden állatnak van éhsége, ami egy szám
- Minden állatnak van szomja, ami egy szám
- Amikor egy állat létrejön 50-es az éhsége és 50-es a szomja
- Minden állat tud csinálni dolgokat:
  - eszik() az éhsége csökken eggyel
  - iszik() a szomja csökken eggyel
  - jatszik() az éhsége és szomja növekszik eggyel

### Megoldás:

```py
class Allat:
    _ehseg = 50
    _szomj = 50

    def eszik(self):
        self._ehseg -= 1
    def iszik(self):
        self._szomj -= 1
    def jatszik(self):
        self._ehseg += 1
        self._szomj += 1

    def lekerEhseg(self):
        print(self._ehseg)

teknos = Allat()
teknos.lekerEhseg() # 50
teknos.eszik()
teknos.lekerEhseg() # 49
```

## Feladat 3

Másold magadhoz az elkészített Pokemon osztályt:

```python
class Pokemon:
    def __init__(self,  nev, tipus, ellenfel):
        self.nev = nev
        self.tipus = tipus
        self.ellenfel = ellenfel

    def hatasos_ellene(self, masik):
        return self.ellenfel == masik.tipus
```

Illetve használd ezen programot, benne kommentként láthatod a feladatot:

```python
def initialize_pokemons():
    pokemon = []
    pokemon.append(Pokemon("Balbasaur", "fű", "víz"))
    pokemon.append(Pokemon("Pikatchu", "elektromos", "víz"))
    pokemon.append(Pokemon("Charizard", "tűz", "fű"))
    pokemon.append(Pokemon("Balbasaur", "víz", "tűz"))
    pokemon.append(Pokemon("Kingler", "víz", "tűz"))
    return pokemon

ash_pokemonjai = initialize_pokemons()

# Minden pokémonnak van neve és típusa.
# Bizonyos tipusok hatásosak más típusokkal szemben, pl. víz hatásos tűz ellen.

# Ash-nek van néhány pokémonja.
# Felbukkant egy vad pokémon!

vad_pokemon = Pokemon("Oddish", "fű", "víz")

# Melyik pokémonját válassza Ash a küzdelemhez?

print("..., téged választalak!")
```

A class és a program kódja két különböző file-ban legyen.

### Megoldás:

```py
# Pokemon.py

class Pokemon:
    def __init__(self,  nev, tipus, ellenfel):
        self.nev = nev
        self.tipus = tipus
        self.ellenfel = ellenfel

    def hatasos_ellene(self, masik):
        return self.ellenfel == masik.tipus
```

```py
# megoldas.py

from Pokemon import Pokemon

def initialize_pokemons():
    pokemon = []
    pokemon.append(Pokemon("Balbasaur", "fű", "víz"))
    pokemon.append(Pokemon("Pikatchu", "elektromos", "víz"))
    pokemon.append(Pokemon("Charizard", "tűz", "fű"))
    pokemon.append(Pokemon("Balbasaur", "víz", "tűz"))
    pokemon.append(Pokemon("Kingler", "víz", "tűz"))
    return pokemon

ash_pokemonjai = initialize_pokemons()

vad_pokemon = Pokemon("Oddish", "fű", "víz")

for i, pokemon in enumerate(ash_pokemonjai):
    if ash_pokemonjai[i].hatasos_ellene(vad_pokemon):
        nev = ash_pokemonjai[i].nev

print(nev + ", téged választalak!") # Charizard, téged választalak!
```

## Feladat 4

Másold magadhoz az elkészített Thing és Fleet osztályt:

```python
class Thing:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return ("[x] " if self.completed else "[ ] ") + self.name
```

```python
class Fleet(object):
    def __init__(self):
        self.things = []

    def add(self, thing):
        self.things.append(thing)

    def __str__(self):
        result = ""
        for i in range(0, len(self.things)):
            result += str(i+1) + ". " + self.things[i].__str__() + "\n"
        return result
```

Illetve használd ezen programot, benne kommentként láthatod a feladatot:

```python
from fleet import Fleet
from thing import Thing

fleet = Fleet()

# Töltsd fel a fleet példányt olyan módon, hogy a következő legyen a kimenet:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)
```

A class és a program kódja két különböző file-ban legyen.

### Megoldás:

```py
# fleet.py

class Fleet(object):
    def __init__(self):
        self.things = []

    def add(self, thing):
        self.things.append(thing)

    def __str__(self):
        result = ""
        for i in range(0, len(self.things)):
            result += str(i+1) + ". " + self.things[i].__str__() + "\n"
        return result
```

```py
class Thing:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return ("[x] " if self.completed else "[ ] ") + self.name
```

```py
# megoldas.py

from fleet import Fleet
from thing import Thing

fleet = Fleet()

get_milk = Thing('Get milk')
fleet.add(get_milk)

remove_the_obstacles = Thing('Remove the obstacles')
fleet.add(remove_the_obstacles)

stand_up = Thing('Stand up')
stand_up.complete()
fleet.add(stand_up)

eat_lunch = Thing('Eat lunch')
eat_lunch.complete()
fleet.add(eat_lunch)

print(fleet)
```

## Feladat 5
