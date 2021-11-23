# Queue implemenation

def isempty(Qu):
    if Qu == []:
        return True
    else:
        return False
    
def Enqueue(Qu, item):
    Qu.append(item)
    if len(Qu) == 1:
        front = rear = 0
    else:
        rear = len(Qu)-1
        
def Dequeue(Qu):
    if isempty(Qu):
        return "Underflow"
    else:
        item = Qu.pop(0)
    if len(Qu) == 0:
        front = rear = None
    return item

def Peek(Qu):
    if isempty(Qu):
        return "Underflow"
    else:
        front = 0
    return Qu[front]

def Display(Qu):
    if isempty(Qu):
        print("Queue empty!")
    elif len(Qu) == 1:
        print(Qu[0], "<== front, rear")
    else:
        front = 0
        rear = len(Qu) - 1
        print(Qu[front], "<== front")
        for a in range(1, rear):
            print(Qu[a])
        print(Qu[rear], "<== rear")
        
qu = []
front = None
while True:
    print("############################# QUEUE OPERATIONS ##################################")
    print("--------------------")
    print("| 1. Enqueue       |")
    print("| 2. Dequeue       |")
    print("| 3. Peek          |")
    print("| 4. Display queue |")
    print("| 5. Exit          |")
    print("--------------------")
    ch = int(input("Enter your choice(1-5): "))
    if ch == 1:
        item = int(input("enter item: "))
        Enqueue(qu, item)
    elif ch == 2:
        item = Dequeue(qu)
        if item == "Underflow":
            print("Underflow! Queue is empty!")
        else:
            print("Dequeue-ed item is", item)       
    elif ch == 3:
        item = Peek(qu)
        if item == "Underflow":
            print("Queue is empty!")
        else:
            print("Frontmost item is: ", item)     
    elif ch == 4:
        Display(qu)        
    elif ch == 5:
        break
    else:
        print("Invalid choice!")
