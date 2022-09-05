import numpy
import seaborn
import matplotlib.pyplot as plt
a = int(input("enter the number of values to insert: "))
numarray = []
for i in range(a):
    val = int(input("enter the value: "))
    numarray.append(val)
b = numpy.array(numarray)
for i in numpy.nditer(b):
    print(i)
for i, j in numpy.ndenumerate(b):
    print(i, j)
c = numpy.random.randint(20)
c = numpy.random.rand()
c = numpy.random.randint(20, size = 3)
print(c)
d = numpy.random.rand(3, 3, 3)
print(d)
e = numpy.random.choice([4, 1, 2], size = (3, 2))
print(e)
f = numpy.random.choice([5, 1, 4, 9], p = [0.2, 0, 0.5, .3], size = (4, 1, 5))
print(f)
print('permutation', numpy.random.permutation(f), 'original', f)
numpy.random.shuffle(f)
print('shuffle', f, 'shape', f.shape)
seaborn.distplot([0, 1, 2, 3, 4, 5], hist = True)
plt.show()
seaborn.distplot(numpy.random.normal(size = (10, 2)), hist = False)
plt.show()
