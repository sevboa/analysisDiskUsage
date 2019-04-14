from modules.CsvWorker import csvWorker

data = csvWorker.load('input/Diskmon.LOG', ['number','time','delay','4','type','process_id','size'], delimeter='\t')

result = dict()

i = 0
while i < 100:
	print(data[i])
	i = i + 1
	result = {
	   'minute': int(float(data[i])/60),
