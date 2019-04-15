
class sizeModel:
    
    Size = int()
    Step = int()
    Records = list()

    Sum = int()
    
    def __init__(self, size):
        self.Records = list()
        self.Sum = int()
        self.Size = size        
        
    def addRecord(self, record):
        self.Records.append(record)
        size = int(record['size'])
        self.Sum = self.Sum + size
    
    def printSize(self):
        print('\t' + str(self.Size) + 'k\t' + str(len(self.Records)) + '\t' + str(round(self.Sum/1024, 2)) + 'MB')

    def getCount(self):
        return len(self.Records)

    def getSum(self):
        Sum = int()
        for record in selfRecords:
            size = int(record['size'])
            Sum = Sum + size
        
        return round(int(self.Size*len(self.Records))/1024, 2)
