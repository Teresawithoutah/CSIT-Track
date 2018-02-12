import math

print ("This program will calculate the surface area and volume of a 3-dimensional cone.Just input radius and height!")

radius = float(input('Enter desired Radius:' ))
height = float(input('Enter desired Height' ))


def main(radius, height):
    cone_surface_area(radius, height)
    cone_volume(radius, height)

def cone_surface_area(radius, height):
    SA = math.pi * radius * radius + math.pi * radius * (math.sqrt(radius * radius + height * height))
    print ("The Area of the cone is","%.2f" %SA) 


def cone_volume(radius, height):
    Volume = (1.0/3) * math.pi * radius * radius * height
    print ("The volume of the cone is","%.2f"%Volume) 


main(radius,height)
