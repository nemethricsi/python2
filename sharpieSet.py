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
