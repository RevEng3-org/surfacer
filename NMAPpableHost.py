from TestableHost import *
import subprocess

class NMAPpableHost(TestableHost):
	hdrRE = '^Starting Nmap ([\d\.]+) \( https:\/\/nmap.org \) at (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) (.+)$'
	rptRE = '^Nmap scan report for (.+) \((.+)\)$'
	hupRE = '^Host is up(.+)$'
	other = '^Other(.+): (.+)$'
	rDNSre = '^rDNS record for (.+): (.+)$'
	LastRE = '^Nmap done(.+) scanned in (.+) seconds$'
	FailedToResolve_RE = '^Failed to resolve "(.+)".$'
	FailRE = '^Nmap done: 0 IP addresses \(0 hosts up\) scanned in (.+)$'
	def __init__(self,hn):
		super().__init__(hn)
		self.command = ['nmap', '-PE', '-sn', hn]
		self.result = ''
		self.nmapVersion = ''

	def test(self):
		resultRaw = subprocess.run(self.command, stdout=subprocess.PIPE)
		self.result = resultRaw.stdout.decode("utf-8") 
		pass

	pass