class TRoad:
    def __init__(self, length0, width0):
        self.length=length0 if length0 > 0 else 0
        self.width=width0 if width0 > 0 else 0

class TCar:
    def __init__(self, road0, p0, v0):
        self.road = road0
        self.p=p0
        self.v=v0
        self.x=0

    def move (self):
        self.x+= self.v
        if self.x>self.road.length:
         self.x = 0

N = 3
cars = []
road = TRoad(10,2)
for i in range(N):
    cars.append (TCar(road, i+1, 2*(i+1)))
for k in range(100):
    for i in range(N):
        cars[i].move()
print ("100:")
for i in range(N):
    print (cars[i].x)

