class p:
    species = 'cape parrot'

    def __init__(self,age,name):
        self.name = name
        self.age = age

p1 = p('blu',4)
p2 = p('browny', 5)

print('the parrot species is',p1.species)
print('the parrot name is',p1.name)
print('the parrot age is',p1.age)

print('the parrot species is',p2.species)
print('the parrot name is',p2.name)
print('the parrot age is',p2.age)