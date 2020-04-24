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
