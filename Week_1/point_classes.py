import math

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        self.r = math.sqrt(self.x**2 + self.y**2)
        if a==0:
            self.theta=math.pi/2
        else:
            self.theta=math.atan(self.y/self.x)
    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay
    def odistance(self): # returns the distance from the origin
        dist = math.sqrt(self.x**2 + self.y**2)
        return dist
    
    def translatewithpolar(self, deltax, deltay):
        self.x=self.r*math.cos(self.theta)
        self.y=self.r*math.sin(self.theta)
        self.x += deltax
        self.y += deltay
        self.r = math.sqrt(self.x**2 + self.y**2)
        if self.x==0:
            self.theta=math.pi/2
        else:
            self.theta=math.atan(self.y/self.x)
    
    def __str__(self):
        return "Coordinates: ({}, {})".format(self.x, self.y)
    
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

testpoint = Point(3,4)
print(testpoint)

testpoint1=Point(3,4)
print(testpoint+testpoint1)
    
    
    

    