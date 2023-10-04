
def triangle(l,b,h):
    area = 0.5*l*b*h
    print(f"Area of triangle is {area}")
    

def circle(r):
    area = 3.14 *r*r
    Circum = 2 * 3.14 * r
    diameter = 2 *r
    print(f"Area of circle is {area}")
    print(f"Circumfrance  of circle is {Circum}")
    print(f"Diameter of circle is {diameter}")
    

a = int(input("Enter the radius of circle"))
l = int(input("Enter the length of triangle"))
b = int(input("Enter the bredth of triangle"))
h = int(input("Enter the height of triangle"))

triangle(l,b,h)
circle(a)



