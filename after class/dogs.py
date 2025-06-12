class d:
    species = 'bull dog'

    def __init__(self,age,name):
        self.name = age
        self.age = name

d1 = d('Max',4)
d2 = d('Lily', 5)

print('the dog species is',d1.species)
print('the dog name is',d1.name)
print('the dog age is',d1.age)

print('the dog species is',d2.species)
print('the dog name is',d2.name)
print('the dog age is',d2.age)