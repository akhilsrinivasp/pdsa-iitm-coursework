import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Is_valid(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False

    def Side_Classification(self):
        if self.Is_valid():
            if self.a == self.b and self.a == self.c:
                return "Equilateral"
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                return "Isosceles"
            else:
                return "Scalene"
        else: 
            return "Not a triangle"
    def Angle_Classification(self):
        if self.Is_valid():    
            l=[self.a**2, self.b**2, self.c**2]
            l=l.sort()
            if l[0] + l[1] == l[2]:
                return "Right"
            elif l[0] + l[1] < l[2]:
                return "Obtuse"
            elif l[0] + l[1] > l[2]:
                return "Acute"
        else:
            return "Not a triangle"
    def Area(self):
        if self.Is_valid():
            s=(self.a+self.b+self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        else:
            return "Not a triangle"
        
a=input("Enter the first side: ")
b=input("Enter the second side: ")
c=input("Enter the third side: ") 
triangle=Triangle(int(a), int(b), int(c))
print(triangle.Is_valid())
print(triangle.Side_Classification())
print(triangle.Angle_Classification())
print(triangle.Area())


    