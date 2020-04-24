class Sharpie:
    def __init__(self, szin, vastagsag, tintaMennyiseg=100):
        self.szin = szin
        self.vastagsag = vastagsag
        self.tintaMennyiseg = tintaMennyiseg

    def use(self):
        self.tintaMennyiseg -= 1
