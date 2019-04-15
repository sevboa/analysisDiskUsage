from modules.models.TimeUnit import timeUnit

class dataKeeper:
	
	Data = list()
	TimeUnits = dict()
	
	def addData(self, dataString):
		self.Data.append(dataString)
		TimeUnit = timeUnit(dataString['time'], 60)
		TimeUnit.addSize(dataString)
		if self.TimeUnits.get(TimeUnit.Time, None) == None:
			self.TimeUnits[TimeUnit.Time] = TimeUnit
		self.TimeUnits[TimeUnit.Time].addSize(dataString)
		
		
	def getData(self):
		for time in self.TimeUnits.keys():
			print(time)
			self.TimeUnits[time].getSize()