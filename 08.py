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
