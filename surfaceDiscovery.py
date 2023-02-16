import subprocess
import re

# for the db

# 


from pprint import pprint

from Host import *
from SurfacerDB import *

hostname = 'studio-api-us.ai.vonage.com'









H = Host(hostname)
print("[][][][][][][]")
print(H.result)
print("[][][][][][][]")
pprint(vars(H))


D = SurfacerDB('sodomitico.sqlite')

DateExecuted = '2023-02-16'
TimeExecuted = '09:17'
TimeZone = 'GMT'
hostname = 'studio-api-us.ai.vonage.com'
mainIPaddress = '52.71.224.241'
isUP = 1
otherIPaddresses = '34.233.167.105 54.242.160.234'
reverseDNShostname = "ec2-52-71-224-241.compute-1.amazonaws.com"
fullResult = """Nmap scan report for studio-api-us.ai.vonage.com (52.71.224.241)
is up (0.081s latency).
Other addresses for studio-api-us.ai.vonage.com (not scanned): 34.233.167.105 54.242.160.234
rDNS record for 52.71.224.241: ec2-52-71-224-241.compute-1.amazonaws.com
Nmap done: 1 IP address (1 host up) scanned in 0.17 seconds
"""

D.insertExtractionRecord(DateExecuted,TimeExecuted,TimeZone,hostname,mainIPaddress,isUP,otherIPaddresses,reverseDNShostname,fullResult)

