def ReadData():
    array = [""]*45
    file = open("Data.txt", "r")
    
    i = 0
    for line in file:
        array[i] = line.strip()
        i += 1

    file.close()
    return array

def FormatArray(array):
    string = ""
    for word in array:
        string = string + word + " "
    return string

def CompareStrings(str1, str2):
    i = 0
    while True:
        if str1[i] == str2[i]:
            i += 1
        else:
            if str1[i] > str2[i]:
                return 1
            else:
                return 2

def Bubble(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if CompareStrings(array[j], array[j+1]) == 1:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(FormatArray(Bubble(ReadData())))
