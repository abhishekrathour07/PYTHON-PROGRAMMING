A = {"Tokyo", "Madrid", "Berlin", "Delhi"}
A.add("Helsinki")
print(A)

A = {"Tokyo", "Madrid", "Berlin", "Delhi"}
B = {"Helsinki", "Warsaw", "Seoul"}
A.update(B)
print(A)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo") # we also use discard method to remove
print(cities)

# union of set A U B
a = {"Tokyo", "Madrid", "Berlin", "Delhi"}
b = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities = A.union(cities)
print(cities)

# intersection 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

# A-B 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)