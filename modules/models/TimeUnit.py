

class timeUnit:
	
	Time = int()
	Sizes = dict()
	
	
	def __init__(self, time, divider):
		self.Time = int(float(time)/divider)
		
	def addSize(self, record):
		sizeList = self.Sizes.get(record['size'], None)
		if sizeList == None:
			self.Sizes[record['size']] = list()
		self.Sizes[record['size']].append(record)
	
	def getSize(self):
		for size in self.Sizes.keys().sort():
			print(' ', size, len(self.Sizes[size]))
		