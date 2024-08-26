area = input("What shape do you want to calculate the area")
area = area.lower()
if (area == 'square'):
    s1 = input('What is the lenght of the square ?')
    print(f'The area of the square is {s1 * s1}')
elif (area == 'rectangle'):
    r1 = input('What is the lenght of the rectangle ?')
    r1 = int(r1)
    r2 = input('What is the breadth of the rectangle ?')
    r2 = int(r2)
    print(f'The area of the rectangle is {r1 * r2}')
elif (area == 'parallelogram'):
    p1 = input('What is the base of the parallelogram ?')
    p1 = int(p1)
    p2 = input('What is the height of the parallelogram ?')
    p2 = int(p2)
    print(f'The area of the parallelogram is {p1 * p2}')
elif (area == 'triangle'):
    t1 = input('What is the base of the triangle ?')
    t1 = int(t1)
    t2 = input('What is the height of the triangle ?')
    t2 = int(t2)
    print(f'The area of the triangle is {t1  /  2 * t2}')
else:
    print('We only calculate the area of\nsquares\nrectangles\nparallelograms and triangles')