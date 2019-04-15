
from modules.CsvWorker import csvWorker
from modules.models.DataModel import dataModel

data = csvWorker.load('input/Diskmon.LOG', ['number','time','delay','disk','type','sector','size'], delimeter='\t')

Data = dataModel(timeInterval = 60)

i = 0
while i < 40000 and i < len(data)-1:
	i = i + 1
	Data.addRecord(data[i])
Data.printRecords()
