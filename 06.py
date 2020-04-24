from station import Station
from car import Car

mol = Station(1000)

audi = Car()
bwm = Car(capacity = 200)

mol.refill(audi)
print(mol.gas_amount)
mol.refill(bwm)
print(mol.gas_amount)

