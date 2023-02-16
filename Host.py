import re
from NMAPpableHost import *

class Host(NMAPpableHost):
	def __init__(self,hn):
		super().__init__(hn)
		self.hostnameCheck = ''
		self.ipAddress = ''
		self.isUP = False
		self.otherIPs=[]
		self.reDNShostname = ''
		self.test()
		self.refactoredParse()
		self.document()

		pass

	def refactoredParse(self):
		lines = self.result.split('\n')
		failed = False
		warning = re.compile(self.FailRE)
		report = re.compile(self.rptRE)
		hostUP = re.compile(self.hupRE)
		rDNSre = re.compile(self.rDNSre)
		otherIPregExp = re.compile(self.other)
		for line in lines:
			rez = warning.findall(line)
			if (rez):
				failed = True

		if not failed:
			header = re.compile(self.hdrRE)
			for line in lines:
				rez = header.findall(line)
				if (rez):
					(self.nmapVersion,self.dateExecuted,self.timeExecuted,self.timeZone)=rez[0]
				rez = report.findall(line)
				if (rez):
					(self.hostnameCheck,self.ipAddress)=rez[0]
				rez = hostUP.search(line)
				if (rez):
					self.isUP = True
				rez = otherIPregExp.findall(line)
				if (rez):
					(tmp,others)=rez[0]
					print(others)
					if (len(others)>0):
						self.otherIPs=others.split(' ')
				rez = rDNSre.findall(line)
				if(rez):
					print(rez[0])
					(tmp,self.reDNShostname)=rez[0]
		else:
			self.isUP = False
		pass

	def document(self):
		pass
	pass