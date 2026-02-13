Queue = [-1 for _ in range(20)]
HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueue(item):
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == len(Queue):
        return False
    
    if NumberItems == 0:
        HeadPointer += 1
    TailPointer += 1
    if TailPointer > len(Queue)-1:
        TailPointer = 0
    NumberItems += 1
    Queue[TailPointer] = item
    return True

def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return -1
    
    returnValue = Queue[HeadPointer]
    HeadPointer += 1
    if HeadPointer > len(Queue)-1:
        HeadPointer = 0
    NumberItems -= 1
    return returnValue

for i in range(1,26):
    enqueue = Enqueue(i)
    if enqueue:
        print(f"{i} successful")
    else:
        print(f"{i} unsuccessful")

print(Dequeue())
print(Dequeue())
