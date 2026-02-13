import random
lists = []

count = 0

while True:
    currentList = []
    while len(currentList) < 4:
        numFound = True

        while numFound:
            numFound = False
            num = random.randint(1,4)
            if num in currentList:
                numFound = True

        currentList.append(num)

    if currentList not in lists:
        print(currentList)
        lists.append(currentList)
    


