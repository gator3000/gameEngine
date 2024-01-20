from math import *
#! not used yet :
# from pygame import *


#* function who caluculate mean of *args
def mean(*args):
    len_of_args = len(args)
    sum_of_args = 0
    for arg in args:
        sum_of_args += arg
    return sum_of_args / len_of_args




#! DO NOT DELETE
current_id = 0

#* library for all instances of this module
instances = {
    "list_by_creation":[],
    "dict_by_id":{}
}


#* library for Points
points = {
    "list_by_creation":[],
    "dict_by_id":{}
}
#* class for Points
class Point():
    def __init__(self, x:float=0.0, y:float=0.0, name:str="unnamedPoint"):
        global current_id
        global points
        global instances
        self.id = current_id
        current_id += 1
        points["list_by_creation"].append(self)
        points["dict_by_id"][str(self.id)] = self
        instances["list_by_creation"].append(self)
        instances["dict_by_id"][str(self.id)] = self

        self.name = name
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    
    def get_id(self):
        return self.id

    def get_distance_x(self, point):
        return self.x-point.x
    def get_distance_y(self, point):
        return self.y-point.y

    def get_distance(self, point):
        return round(self.get_distance_exacte(point),3)
    def get_distance_exacte(self, point):
        return sqrt((self.get_distance_x(point)**2)+(self.get_distance_y(point)**2))

#* library for Vectors
vectors = {
    "list_by_creation":[],
    "dict_by_id":{}
}
#* class for Vectors
class Vector():
    def __init__(self, origin:Point=Point(0,0), target:Point=Point(0,0), name:str="unnamedVector"):
        global current_id
        global vectors
        global instances
        self.id = current_id
        current_id += 1
        vectors["list_by_creation"].append(self)
        vectors["dict_by_id"][str(self.id)] = self
        instances["list_by_creation"].append(self)
        instances["dict_by_id"][str(self.id)] = self
        self.name = name

        self.i = target.get_distance_x(origin)
        self.j = target.get_distance_y(origin)
    
    def get_coords(self):
        return (self.i, self.j)
    def get_norma(self):
        return sqrt(self.i**2 + self.j**2)  #* Pythagore
    def get_direction(self):
        '''return direction in degrees'''
        return math.degrees(math.atan2(self.j, self.i))
    def get_sens(self):
        return 1 if self.direction > 0 else 2 if self.direction < 0 else 0

class Force(Vector):
    def __init__(self, intensity:float=0, direction:float=0, name:str="unnamedForce"):
        i = intensity * cos(radians(direction))
        j = intensity * sin(radians(direction))
        super().__init__(i,j,name)

class Acceleration(Vector):
    def __init__(self, intensity:float=0, direction:float=0, name:str="unnamedAcceleration"):
        i = intensity * cos(radians(direction))
        j = intensity * sin(radians(direction))
        super().__init__(i,j,name)

class Speed(Vector):
    def __init__(self, intensity:float=0, direction:float=0, name:str="unnamedSpeed"):
        i = intensity * cos(radians(direction))
        j = intensity * sin(radians(direction))
        super().__init__(i,j,name)

class Gravity(Force):
    def __init__(self, intensity:float=0, direction:float=270, name:str="unnamedSpeed"):
        i = intensity * cos(radians(direction))
        j = intensity * sin(radians(direction))
        super().__init__(i,j,name)


#* library for Shapes
shapes = {
    "list_by_creation":[],
    "dict_by_id":{}
}
#* class for Shapes
class Shape():
    def __init__(self, type:str="square", name:str="unnamedShape", area:float=1):
        global current_id
        global shapes
        global instances
        self.id = current_id
        current_id += 1
        shapes["list_by_creation"].append(self)
        shapes["dict_by_id"][str(self.id)] = self
        instances["list_by_creation"].append(self)
        instances["dict_by_id"][str(self.id)] = self
        self.name = name
        self.type = type
        self.area = area

class Square(Shape):
    def __init__(self, side:float=1, name:str="unnamedSquare"):
        super().__init__(type="square", name=name, area=side**2)
        self.side = side

class Regtangle(Shape):
    def __init__(self, widht:float=1, height:float=1, name:str="unnamedRectangle"):
        super().__init__(type="rectangle", name=name, area=widht*height)
        self.height= height
        self.widht = widht

class Circle(Shape):
    def __init__(self, radius:float=1, name:str="unnamedCircle"):
        super().__init__(type="circle", name=name, area=pi*radius**2)
        self.radius=radius

class Triangle(Shape):
    def __init__(self, pointOne:Point, pointTwo:Point, pointThree:Point, name:str="unnamedCircle"):
        self.len_base = pointOne.get_distance_exacte(pointTwo)
        self.len_height = pointThree.get_distance_exacte(Point(mean(pointOne.x,pointTwo.x),mean(pointOne.y,pointTwo.y)))
        area = self.len_base*self.len_height/2
        super().__init__(type="triangle", name=name, area=area)
        self.point1 = pointOne
        self.point2 = pointTwo
        self.point3 = pointThree

class Image():
    pass

class Hitbox():
    def __init__(self, type:str,*dims ,name:str="unnamedHitbox"):
        pass

#* library for Objects
objects = {
    "list_by_creation":[],
    "dict_by_id":{}
}
#* class for Objects
class Object():
    def __init__(self, position:Point, texture:Image, hitbox:Hitbox, name:str="unnamedObject"):
        global current_id
        global objects
        global instances
        self.id = current_id
        current_id += 1
        objects["list_by_creation"].append(self)
        objects["dict_by_id"][str(self.id)] = self
        instances["list_by_creation"].append(self)
        instances["dict_by_id"][str(self.id)] = self
        self.name = name

        self.position = position
        self.texture = texture
        self.hitbox = hitbox


# TODO: charaters etc..

#s = Point(0,1)
#s2 = Point(1,2)
#print(s.id)
#print(s2.id)
print(instances['dict_by_id'])
# print(instances['dict_by_id']['0'].get_y())
# print(instances['dict_by_id']['1'].get_y())
# print(instances['dict_by_id']['2'].get_y())
#print(instances['dict_by_id']['3'].get_y())