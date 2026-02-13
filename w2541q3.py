HashTable = []

class Record():
    def __init__(self, key, data):
        self.key = key
        self.data = data

def InitialiseHashTable():
    global HashTable
    HashTable = [[None for _ in range(10)] for _ in range(100)]

def Hash(key):
    return key % 100

def InsertData(record):
    global HashTable
    hash = Hash(record.key)
    i = 0
    while i < 10:
        if HashTable[hash][i] is None:
            print(record.data)
            HashTable[hash][i] = record
            break
        i += 1

def ReadData():
    with open("9618_w25_qp_41_HashTableData.txt") as file:
        for line in file:
            line = line.strip()
            key = int(line.split(",")[0])
            data = line.split(",")[1]
            #print(key,data)
            InsertData(Record(key,data))

def GetRecord(key):
    global HashTable
    hash = Hash(key)
    print(hash)
    i = 0
    while i < 10:
        if HashTable[hash][i] is not None:
            if HashTable[hash][i].key == key:
                return HashTable[hash][i].data
                break
        i += 1
    return "Not found"

InitialiseHashTable()
ReadData()
print(GetRecord(528))
