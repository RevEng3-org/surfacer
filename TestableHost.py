from BaseHost import *

class TestableHost(BaseHost):
	def __init__(self,hn):
		super().__init__(hn)
		self.dateExecuted = ''
		self.timeExecuted = ''
		self.timeZone = ''
		pass
	pass