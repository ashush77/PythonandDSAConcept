Car = {"audi","maruti","volvo","maruti"}

Cars = {"lembo","tata","hyundai","maruti"}

print(Car)
print(Cars)

Car.add("ford")
print(Car)

Cars.remove("lembo")
print(Cars)

AllCars = Car.union(Cars)
print(AllCars)

print(Car.intersection(Cars))
print(Car.difference(Cars))
print(Car.issubset(Cars))
print(Cars.issuperset(Car))