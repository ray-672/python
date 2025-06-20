from abc import ABC, abstractmethod

class ani(ABC):
    @ abstractmethod
    def move():
        pass


class hum(ani):
    def move(self):
        print('i am a human i can walk')


class sna(ani):
    def move(self):
        print('i am a snake i can crawl around')

h1 = hum()
h1.move()

s1 = sna()
s1.move()