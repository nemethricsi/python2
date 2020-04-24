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
