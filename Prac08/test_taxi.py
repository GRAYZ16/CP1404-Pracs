from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi

prius = Taxi("Prius 1", 100)
prius.drive(40)
print(prius)

prius.start_fare()
prius.drive(100)
print(prius)

lada = UnreliableCar("Lada", 100, 50)
lada.drive(10)
print(lada)
lada.drive(10)
print(lada)
lada.drive(20)
print(lada)
lada.drive(60)
print(lada)

silver = SilverServiceTaxi("SST", 100, 2)
silver.drive(10)
print(silver.get_fare())
print(silver)