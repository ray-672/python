class point:
    def __init__(self,w,y):
        self.w = w
        self.y = y

    def __str__(self):
        return f'({self.w},{self.y})'
    
p1 = point(20,40)

print(p1)