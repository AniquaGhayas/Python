import sys, math
a = float(sys.argv[1]) 
b = float(sys.argv[2]) 
c = float(sys.argv[3])
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle:", area)