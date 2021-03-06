# Python Haladó (megoldások)

#### [1. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-1) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f1)

#### [2. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-2) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f2)

#### [3. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-3) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f3)

#### [4. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-4) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f4)

#### [5. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-5) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f5)

#### [6. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-6) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f6)

#### [7. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-7) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f7)

#### [8. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-8) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f8)

#### [9. Feladat](https://github.com/nemethricsi/python2/blob/master/README.md#feladat-9) [(megoldás)](https://github.com/nemethricsi/python2/blob/master/README.md#megold%C3%A1s-f9)

## Feladat 1

Készíts egy PostIt osztályt, amelynek van 3 tagváltozója:

- `hatterSzin`
- `szoveg` ami rajta van
- `szovegSzin`
  Készíts pár példa objektumot:
- sárga posztit kék szöveggel: "Első ötlet"
- rózsaszínű posztit fekete szöveggel: "Hurrá!"
- zöld posztit barna szöveggel: "Szuper!"

### Megoldás (F1):

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

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)

## Feladat 2

- Készíts egy `Allat` osztályt
- Minden állatnak van éhsége, ami egy szám
- Minden állatnak van szomja, ami egy szám
- Amikor egy állat létrejön 50-es az éhsége és 50-es a szomja
- Minden állat tud csinálni dolgokat:
  - eszik() az éhsége csökken eggyel
  - iszik() a szomja csökken eggyel
  - jatszik() az éhsége és szomja növekszik eggyel

### Megoldás (F2):

```py
# allat.py

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
        return self._ehseg
```

```py
# megoldas.py

from allat import Allat

teknos = Allat()
print(teknos.lekerEhseg()) # 50
teknos.eszik()
print(teknos.lekerEhseg()) # 49
```

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)

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

### Megoldás (F3):

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

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)

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

### Megoldás (F4):

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
# thing.py

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

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)

## Feladat 5

Hozz létre diák és tanár osztályokat: Student és Teacher néven

##### `Student`

- `learn()`: Kiírja a képernyőre: "A diák tanul valamit"
- `question(teacher)`: calls the teachers answer method

##### `Teacher`

- `teach(student)`: Meghívja a diák `learn()` metódusát
- `answer()`: Kiírja a képernyőre: "A tanár válaszol a diáknak"

##### Program

- Hozz létre egy `Student` és `Teacher` példányt
- Hívd meg a diák `question()` metódusát és a tanár `teach()` metódusát

### Megoldás (F5):

```py
# student.py

class Student:
    def learn(self):
        print('A diák tanul valamit')
    def question(self, teacher):
        teacher.answer()
```

```py
# teacher.py

class Teacher:
    def answer(self):
        print('A tanár válaszol a diáknak')
    def teach(self, student):
        student.learn()
```

```py
# megoldas.py

from student import Student
from teacher import Teacher

pisti = Student()
marika = Teacher()

pisti.question(marika) # A tanár válaszol a diáknak
marika.teach(pisti) # A diák tanul valamit
```

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)

## Feladat 6

Hozz létre egy töltőállomás és autó osztályt `Station` és `Car` néven.

##### `Station`

Tagváltozók:

- `gas_amount`: A töltőállomás üzemanyag szintje

Metódusok:

- `refill(car)`: Csökkenti a `gas_amount` tagváltozót az átadott autó `capacity` értékével, és megnöveli az autó `gas_amount` tagváltozóját

##### `Car`

Tagváltozók:

- `gas_amount`: Az autó üzemanyag szintje

- `capacity`: Az autó maximális üzemanyag szintje

Metódusok:

Hozz létre egy konstruktort ami beállítja a következő értékeket:

- `gas_amount`: 0
- `capacity`: 100

### Megoldás (F6):

```py
# car.py

class Car:
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity
```

```py
# station.py

class Station:
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount

    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity
```

```py
# megoldas.py

from station import Station
from car import Car

mol = Station(1000)

audi = Car()
bwm = Car(capacity = 200)

mol.refill(audi)
print(mol.gas_amount) # 900
mol.refill(bwm)
print(mol.gas_amount) # 700
```

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)

## Feladat 7

Hozz létre egy filctoll és tolltartó osztályt `Sharpie` és `SharpieSet` néven.

##### `Sharpie`

Az osztály tárolja a filc szinét, vastagságát és tinta mennyiségét.

A létrehozott példány tinta mennyisége legyen 100.

Legyen egy `use()` metódusa ami csökkenti a tinta mennyiségét.

##### `SharpieSet`

Az osztály filceket tárol. Rendelkezzen a következő.

- `add(sharpie)`: Hozzáad egy filcet
- `count_usable()`: Visszaadja a számát azoknak a filceknek amikben még van tinta
- `remove_trash()`: Törli az üres filceket

### Megoldás (F7):

```py
# sharpie.py

class Sharpie:
    def __init__(self, szin, vastagsag, tintaMennyiseg=100):
        self.szin = szin
        self.vastagsag = vastagsag
        self.tintaMennyiseg = tintaMennyiseg

    def use(self):
        self.tintaMennyiseg -= 1

```

```py
# sharpieSet.py

class SharpieSet:
    sharpies = []

    def add(self, sharpie):
        self.sharpies.append(sharpie)

    def count_usable(self):
        count = 0
        for sharpie in self.sharpies:
            if sharpie.tintaMennyiseg > 0:
                count += 1
        return count

    def remove_trash(self):
        for sharpie in self.sharpies:
            if sharpie.tintaMennyiseg <= 0:
                self.sharpies.remove(sharpie)
```

```py
# megoldas.py

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

```

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)

## Feladat 8

##### `Farm`

Használd újra az `Allat` osztályt.

Hozz létre egy `Farm` osztályt.

- tároljon állatokat
- tárolja hogy maximum hány állatot tud tárolni

Metódusok:

- `breed()`: létrehoz egy új állatot ha van neki hely
- `slaughter()`: kiveszi a legkevésbé éhes állatot

### Megoldás (F8):

```py
# farm.py

from allat import Allat


class Farm:
    allatok = []

    def __init__(self, szabadHelyek):
        self.szabadHelyek = szabadHelyek

    def lekerSzabadHelyek(self):
        return self.szabadHelyek - len(self.allatok)

    def add(self, allat):
        if self.lekerSzabadHelyek() > 0:
            self.allatok.append(allat)
        else:
            print('Sajnos nincs több hely jelenleg.')

    def breed(self):
        if self.lekerSzabadHelyek() > 0:
            self.allatok.append(Allat())
        else:
            print('Sajnos nincs több hely jelenleg.')

    def slaughter(self):
        legkevesbeEhesAllat = None
        legkevesebbEhseg = 50
        for allat in self.allatok:
            if allat.lekerEhseg() < legkevesebbEhseg:
                legkevesebbEhseg = allat.lekerEhseg()
                legkevesbeEhesAllat = allat
        self.allatok.remove(legkevesbeEhesAllat)

```

```py
# megoldas.py

from farm import Farm
from allat import Allat

allatFarm = Farm(5)

tigris = Allat()
malac = Allat()
allatFarm.add(tigris)
allatFarm.add(malac)
allatFarm.breed()  # uj random allat
print(allatFarm.allatok)

print(tigris.lekerEhseg())
print(malac.lekerEhseg())

malac.eszik()
print(malac.lekerEhseg())

allatFarm.slaughter()

print(allatFarm.allatok)
```

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)

## Feladat 9

##### `BlogPost`

Hozz létre `BlogPost` osztályt aminek van:

- szerző neve
- címe
- szövege
- dátuma

##### `Blog`

Hozz létre `Blog` ami képes:

- `BlogPost`-okat tárolni
- Hozzáadni egyet a listához
- Törölni egyet index alapján
- Megváltoztatni egyet, egy másik pédányra index alapján

### Megoldás (F9):

```py
# blog.py

class Blog:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def removeByIndex(self, index):
        for i, post in enumerate(self.posts):
            if i == index:
                self.posts.remove(post)

    def updateByIndex(self, index, new_post):
        for i, _ in enumerate(self.posts):
            if i == index:
                self.posts[i] = new_post

    def listBlogPosts(self):
        for post in self.posts:
            print(post.szerzo + " : " + post.cim)
```

```py
# blogPost.py

class BlogPost:
    def __init__(self, szerzo, cim, szoveg, datum):
        self.szerzo = szerzo
        self.cim = cim
        self.szoveg = szoveg
        self.datum = datum
```

```py
# megoldas.py

from blog import Blog
from blogPost import BlogPost

my_blog = Blog()
print(my_blog.posts)  # []

cikk1 = BlogPost("EAP", "Cím", "content", "2020.04.24.")
my_blog.add(cikk1)
cikk2 = BlogPost("Jakab", "Clickbait", "szöveg", "2020.03.12.")
my_blog.add(cikk2)

my_blog.listBlogPosts()

my_blog.removeByIndex(0)  # törli cikk1-et
my_blog.listBlogPosts()

my_blog.updateByIndex(0, cikk1)  # cikk1-re a megmaradt cikk2-t
my_blog.listBlogPosts()
```

[Vissza a tetejére](https://github.com/nemethricsi/python2/blob/master/README.md#python-halad%C3%B3-megold%C3%A1sok)
