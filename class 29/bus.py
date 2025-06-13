class veh:
    def __init__(self,mileage,name,max_speed):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed

    def dis(self):
        print(f'the bus name is{self.name}')
        print(f'the bus max speed is{self.max_speed}')
        print(f'the bus mileage is{self.mileage}')

class bus(veh):
    pass

bus1 = bus(20,'valvo',120)

bus1.dis()