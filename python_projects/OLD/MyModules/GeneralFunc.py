def str_to_left(base, string):
    return string + base

def pythagoras(side_a, side_b):
    result = (side_a**2+side_b**2)**0.5
    return format(result,".2f")

def sphere_volume(rad):
    return format(4/3*3.14*rad**3, ".2f")

def cube_volume(side):
    return side**3

def rectangle_volume(length, width, height):
    return length*width*height

def cylinder_volume(rad, height):
    return 3.14*rad**2*height