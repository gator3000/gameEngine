from math import *
#! not used yet : from pygame import *


#* function who caluculate mean of *args
def mean(*args):
    len_of_args = len(args)
    sum_of_args = 0
    for arg in args:
        sum_of_args += arg
    return sum_of_args / len_of_args




#! DO NOT DELETE
current_id = 0
DEFINED_TYPES_OF_SHAPES = ("rectangle", "circle")

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
    def __init__(self, coords:tuple=(0,0), name:str="unnamedVector"):
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

        self.i = coords[0]
        self.j = coords[1]
    
    def get_coords(self):
        return (self.i, self.j)
    def get_norma(self):
        return sqrt(self.i**2 + self.j**2)  #* Pythagore
    def get_direction(self):
        '''return direction in degrees'''
        return math.degrees(math.atan2(self.j, self.i))
    def get_sens(self):
        '''return 1 if direction is -x°, 2 if dir is +x° and 0 if 0°'''
        return 1 if self.direction > 0 else 2 if self.direction < 0 else 0

class Force(Vector):
    def __init__(self, intensity:float=0, direction:float=0, name:str="unnamedForce"):
        i = intensity * cos(radians(direction))
        j = intensity * sin(radians(direction))
        super().__init__((i,j),name)

class Acceleration(Vector):
    def __init__(self, intensity:float=0, direction:float=0, name:str="unnamedAcceleration"):
        i = intensity * cos(radians(direction))
        j = intensity * sin(radians(direction))
        super().__init__((i,j),name)

class Speed(Vector):
    def __init__(self, intensity:float=0, direction:float=0, name:str="unnamedSpeed"):
        i = intensity * cos(radians(direction))
        j = intensity * sin(radians(direction))
        super().__init__((i,j),name)

class Gravity(Force):
    def __init__(self, intensity:float=0, direction:float=270, name:str="unnamedSpeed"):
        super().__init__(intensity, direction, name)


#* library for Shapes
shapes = {
    "list_by_creation":[],
    "dict_by_id":{}
}
#* class for Shapes
class Shape():
    def __init__(self, type:str, name:str="unnamedShape", area:float=1):
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
    def get_type(self):
        return self.type
    def get_area(self):
        return self.area

class Rectangle(Shape):
    def __init__(self, widht:float=1, height:float=1, name:str="unnamedRectangle"):
        super().__init__(type="rectangle", name=name, area=widht*height)
        self.height= height
        self.widht = widht
    def is_touching(self, obj, pos):
        if obj.hitbox.shape == "rectangle":
            distheight = (obj.hitbox.self.height + self.height) / 2
            distwidth = (obj.hitbox.self.widht + self.widht) / 2
            return pos.get_distance_x(obj.position) <= distwidth and pos.get_distance_y(obj.position) <= distheight
        elif obj.hitbox.shape == "circle":
            distheight = (obj.hitbox.self.side + self.height) / 2
            distwidth = (obj.hitbox.self.side + self.widht) / 2
            return pos.get_distance_x(obj.position) <= distwidth and pos.get_distance_y(obj.position) <= distheight
        else:
            return "<FUNCTION NOT DEFINED>"


class Circle(Shape):
    def __init__(self, radius:float=1, name:str="unnamedCircle"):
        super().__init__(type="circle", name=name, area=pi*radius**2)
        self.radius=radius
    def is_touching(self, obj, pos):
        if obj.hitbox.shape == "circle":
            return (self.radius + obj.hitbox.self.radius) / 2 >= pos.get_distance_exacte(obj.position)
        if obj.hitbox.shape == "rectangle":
            x = (obj.side + self.radius) /2 >= obj.position.get_distance_x(pos)
            y = (obj.side + self.radius) /2 >= obj.position.get_distance_y(pos)
            return True if x and y else "<FUNCTION NOT DEFINED>"
        else:
            return "<FUNCTION NOT DEFINED>"


#* library for Images
images = {
    "list_by_creation":[],
    "dict_by_id":{}
}
#* class for Images
class Image():
    pass

#* library for Hitboxes
hitboxes = {
    "list_by_creation":[],
    "dict_by_id":{}
}
#* class for Hitboxes
class Hitbox():
    def __init__(self, shapeType:str,*dims ,name:str="unnamedHitbox"):
        assert shapeType in DEFINED_TYPES_OF_SHAPES, ValueError(f"{shapeType} is not defined")
        global current_id
        global hitboxes
        global instances
        self.id = current_id
        current_id += 1
        hitboxes["list_by_creation"].append(self)
        hitboxes["dict_by_id"][str(self.id)] = self
        instances["list_by_creation"].append(self)
        instances["dict_by_id"][str(self.id)] = self
        self.name = name

        self.shape = shapeType.lower()
        if self.shape == "rectangle": self.self = Rectangle(name=f"shape of hitbox {self.name}", *dims)
        elif self.shape == "circle": self.self = Circle(name=f"shape of hitbox {self.name}", *dims)
        
    def get_shape():
        return self.shape, self.self


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

    def is_touching(self, obj):
        if self.hitbox.shape == "rectangle":return self.hitbox.self.is_touching(obj, self.position)
        elif self.hitbox.shape == "circle": return self.hitbox.self.is_touching(obj, self.position)

# TODO: charaters etc..

s = Point(0,1)
s2 = Point(1,2)
v = Vector((1,5))
g = Gravity(9.81, 270)


print(instances['dict_by_id'])
# print(instances['dict_by_id']['0'].get_y())
# print(instances['dict_by_id']['1'].get_y())
# print(instances['dict_by_id']['2'].get_y())
#print(instances['dict_by_id']['3'].get_y())