# programme to search an element in a sorted list using binary search

def bsearch(lst,x):
    first  = 0
    last = len(lst)-1
    mid = 0
    pos = -1
    while first < last:
        mid = (first+last)//2
        if lst[mid] == x:
            pos = mid+1
            break
        elif lst[mid] > x:
            last = mid-1
        else:
            first = mid+1
    if pos == -1:
        return "element not found"
    else:
        return "the position of the element is: ", pos

list = []
n = int(input("enter the number of elements: "))
print("enter the element in ascending order")

for i in range(n):
    temp = int(input())
    list.append(temp)
print(list)

num = int(input("enter the number you want to search: "))
print(bsearch(list,num))
