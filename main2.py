import numpy
a = int(input("enter the number of values to insert: "))
numarray = []
for i in range(a):
    val = int(input("enter the value: "))
    numarray.append(val)
b = numpy.array(numarray)
for i in numpy.nditer(b):
    print(i)
