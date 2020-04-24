class Station:
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount

    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity