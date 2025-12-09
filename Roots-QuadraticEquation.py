import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b*b - 4*a*c

if D > 0:
    print("Roots are real and distinct")
    print("Root 1:", (-b + math.sqrt(D)) / (2*a))
    print("Root 2:", (-b - math.sqrt(D)) / (2*a))

elif D == 0:
    print("Roots are real and equal")
    print("Root:", -b / (2*a))

else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("Roots are complex")
    print("Root 1: {} + {}i".format(real, imag))
    print("Root 2: {} - {}i".format(real, imag))
