
from modules.models.SizeModel import sizeModel
from operator import attrgetter

class tickModel:
    
    Time = int()
    Records = list()
    
    Sizes = list()
    
    
    def __init__(self, time):
        self.Records = list()
        self.Sizes = list()
        self.Time = time
        
    def addRecord(self, record):
        self.Records.append(record)
        size = int(record['size'])
        if size <= 16:
            size = 16
        elif size <= 128:
            size = 128
        else:
            size = 512
        Size = self.getSize(size)
        Size.addRecord(record)
    
    def getSize(self, size):
        for Size in self.Sizes:
            if Size.Size == size:
                return Size
        return self.addSize(size)

    def addSize(self, size):
        Size = sizeModel(size)
        self.Sizes.append(Size)
        return Size

    def printTick(self):
        print(self.Time)
        sizes = sorted(self.Sizes, key = attrgetter('Size'))
        for Size in sizes:
            Size.printSize()

    #def getTickString(self):


        