from modules.CsvWorker import csvWorker
from modules.models.DataKeeper import dataKeeper
from modules.models.TimeUnit import timeUnit

data = csvWorker.load('input/Diskmon.LOG', ['number','time','delay','disk','type','sector','size'], delimeter='\t')

DataKeeper = dataKeeper()

i = 0
while i < 1000:
	i = i + 1
	DataKeeper.addData(data[i])
DataKeeper.getData()
