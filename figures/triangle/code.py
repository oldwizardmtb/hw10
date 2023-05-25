def triangle_perimeter(a, b, c):
    perimeter = a + b + c
    print(perimeter)

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = 0.5 ** (p * (p - a) * (p - b) * (p - c))
    print(area)

