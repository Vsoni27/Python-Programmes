import math
import matplotlib.pyplot as plt

p = int(input("Enter the monthy investment: "))
R = int(input("Enter the rate of interest: "))
y = int(input("Enter the no of years: "))

net_value = []
years = []

Net_am = 0

A = p
per_rate = R/12
for i in range(y*12):
    A = A*(1+(per_rate/100))
    if i == (y*12)-1:
        Net_am = A
    net_value.append(math.floor(A))
    years.append(i+1)
    A = A+p



print("Total invested amount: ", 12*p*y)
print("Estimated Return: ", math.floor(Net_am-(12*p*y)))
print("Net Value: ", math.floor(Net_am))

# graph showing growth in our amount with respect to months
plt.plot(years,net_value)
plt.show()
# pie chart showing percentages of total invested amount and total return
y = [12*p*y,math.floor(Net_am-(12*p*y))]
name = ["Investment","Return"]
colors = ['b','g']
plt.pie(y, labels = name,radius = 1.2, autopct = '%1.1f%%')
plt.legend()
plt.show()
