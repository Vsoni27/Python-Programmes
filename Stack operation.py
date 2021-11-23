# stack implementation
def isempty(stk):
    if stk == []:
        return True
    else:
        return False
    
def Push(stk, item):
    stk.append(item)
    top = len(stk)-1
    
def Pop(stk):
    if isempty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk)-1
        return item
    
def Peek(stk):
    if isempty(stk):
        return "Underflow"
    else:
        top = len(stk)-1
        return stk[top]
    
def Display(stk):
    if isempty(stk):
        print("Stack is empty")
    else:
        top = len(stk)-1
        print(stk[top], "<-top")
        for a in range(top-1,-1,-1):
            print(stk[a])
            
stk = []
top = None
while True:
    print("########################## STACK OPERATIONS #############################")
    print("--------------------")
    print("| 1. Push          |")
    print("| 2. Pop           |")
    print("| 3. Peek          |")
    print("| 4. Display stack |")
    print("| 5. Exit          |")
    print("--------------------")
    ch = int(input("enter your choice(1-5): "))
    if ch == 1:
        item = int(input("Enter item: "))
        Push(stk, item)
    elif ch == 2:
        item = Pop(stk)
        if item == "Underflow":
            print("Underflow! Stack is empyty!")
        else:
            print("Popped item is", item)
    elif ch == 3:
        item = Peek(stk)
        if item == "Underflow":
            print("Stack is empyty!")
        else:
            print("Topmost item is", item)
    elif ch == 4:
        Display(stk)
    elif ch == 5:
        break
    else:
        print("Invalid choice")
