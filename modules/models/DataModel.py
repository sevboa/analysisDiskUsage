
from modules.models.TickModel import tickModel

class dataModel:
	
	TimeInterval = int()
	Records = list()
	Ticks = list()
	
	def __init__(self, timeInterval):
		self.TimeInterval = timeInterval
	
	def addRecord(self, record):
		self.Records.append(record)
		Tick = self.getTick(record['time'])
		Tick.addRecord(record)
		
	def getTick(self, time):
		time = int(float(time)/self.TimeInterval)
		for Tick in self.Ticks:
			if Tick.Time == time:
				return Tick
		return self.addTick(time)
	
	def addTick(self, time):
		Tick = tickModel(time)
		self.Ticks.append(Tick)
		return Tick

	def printRecords(self):
		for Tick in self.Ticks:
			Tick.printTick()