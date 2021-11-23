# programme to plot the greatest integer function f(x) = [x] using matplot libraries
import math 
import numpy as np
import matplotlib.pyplot as plt
def GIF(x):
    if x - math.floor(x) != 0:
        y = math.floor(x)
        return y
    else:
        y = x
        return y
n1 = float(input("enter the number to start with: "))
n2 = float(input("enter the number to end with: "))
x = np.arange(n1,n2,0.001)
y = []
for i in x:
    y.append(GIF(i))
plt.plot(x,y)
plt.show()
