class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    number_of_sides = 3 # member variable
    
    def check_angles(self):
        if sum([self.angle1, self.angle2, self.angle3]) == 180:
            return True
        else:
            return False
            
my_triangle = Triangle(60,60,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle): # Class Equilateral is inherited from class Triangle
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
        
    angle = 60 # member variable