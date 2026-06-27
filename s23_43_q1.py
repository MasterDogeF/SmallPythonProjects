DataArray = [] #25 elements Integer

try:
    file = open("Data.txt")
    for line in file:
        DataArray.append(line.strip())
    file.close()
except IOError:
    print("you stupid bitch")

def PrintArray(array):
    for item in array:
        print(item, end=" ")

PrintArray(DataArray)