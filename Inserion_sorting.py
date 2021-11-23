#insertion sorting
n=int(input("enter the number of items: "))
lst = [0 for i in range(0,n)]
for i in range(0,n):
    lst[i] = int(input("enter the element: "))
print("original list: ", lst)
for i in range(n):
    key = lst[i]
    j = i-1
    while j>=0 and key < lst[j]:
        lst[j+1] = lst[j]
        j =j-1
    else:
        lst[j+1] =key
print("list after sorting: ", lst)
