count = 0
answer = []

def parent(i):
    return (i-1)//2

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*i + 2

def swap(paraList, index1, index2):
    global count
    count += 1
    answer.append([index1, index2])
    temp = paraList[index1]
    paraList[index1] = paraList[index2]
    paraList[index2] = temp

def siftUp(paraList, i):
    while i > 1 and newList[parent(1)] > newList[i]:
        swap(paraList, parent(i), i)
        i = parent(i)

def siftDown(paraList, size, i):
    maxIndex = i
    l = leftChild(i)
    if l <= size-1 and paraList[l] < paraList[maxIndex]:
        maxIndex = l
    r = rightChild(i)
    if r <= size - 1 and paraList[r] < paraList[maxIndex]:
        maxIndex = r
    if i != maxIndex:
        swap(paraList, i, maxIndex)
        siftDown(paraList, size, maxIndex)

def Extractmax(paraList, size):
    result = paraList[1]
    paraList[1] = paraList[size]
    size -= 1
    siftDown(paraList, size, 1)
    print(result)
    return result

def buildHeap(paraList, size):
    for i in reversed(range(size//2)):
        siftDown(paraList, size, i)

n = int(input())
newList = list(map(int, input().split()))
buildHeap(newList, n)
print(count)
for elements in answer:
    for element in elements:
        print(element, end=" ")
    print("")