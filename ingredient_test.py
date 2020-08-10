from units import *
from ingredients import *

print("Testing Quantity")
print("Same units")

q1 = Quantity(gram, 1)
print("unit display name: ", q1.get_unit()["display_name"])
print("unit amount: ", q1)

q2 = Quantity(ml, 2)
print("unit amount: ", q2)

q3 = Quantity(each, 3)
print("unit amount: ", q3)

print("Summing units")
print("same unit")
q4 = q1 + q1 
print(q4)

print("converting and back")
q5 = Quantity(pound, 5)
print(q5)
q5.convert(gram)
print(q5)
q5.convert(pound)
print(q5)

print("same unit type")

q6 = q5 + q1
print(q6)

q7 = Quantity(cup, 1)
q8 = Quantity(ml, 500)
print(q7 + q8)

print("different unit type")
try:
    q = q1 + q3
except MeasurementTypeMismatch:
    print("caught measurement mismatch")

print("Units tested successfully")

print("Testing ingredients")

ing1 = Ingredient("carrots", "produce", Quantity(pound, 5))
ing2 = Ingredient("carrots", "produce", Quantity(mass_ounce, 20))
ing3 = ing1 + ing2

print(ing3)
