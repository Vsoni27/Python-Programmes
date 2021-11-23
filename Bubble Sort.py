#bubble sorting

n=int(input("enter the number of items: "))
lst = [0 for i in range(0,n)]

for i in range(0,n):
    lst[i] = int(input("enter the element: "))
print("original list: ")
print(lst)

for i in range (n):
    for j in range(0,n-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print("list after sorting: ",lst)
