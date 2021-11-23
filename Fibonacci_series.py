# Python Fibonacci series Program 
Number = int(input("\nPlease Enter the Range Number: "))
First_Value = 0
Second_Value = 1
           

for Num in range(0, Number):
    if(Num <= 1):
        Next = Num
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print(Next)
