import datetime
import sqlite3
from sqlite3 import Error

class SurfacerDB:
	def __init__(self,fn):
		self.extractionTime = ''
		self.extractionDate = ''
		self.timestamp = ''
		self.filename = fn
		self.currentTableName = ''
		self.connection = None
		self.status = 0
		self.condition = "Starting"
		self.prepareInsertion()
		self.prepareConnection()
		self.prepareMasterIndex()
		self.prepareNewExtraction()

	def prepareInsertion(self):
		ct = datetime.datetime.now()
		date = f'{ct.date()}'
		time = f'{ct.time()}'[0:8]
		timestamp = f'{int(ct.timestamp())}'
		self.extractionDate = date
		self.extractionTime = time
		self.timestamp = timestamp
		self.currentTableName = f'Extraction_{timestamp}'

	def prepareConnection(self):
		conn = None
		try:
			conn = sqlite3.connect(self.filename)
			self.connection = conn
			self.condition = "Connected to the Database"
		except Error as e:
			self.status = 1
			self.condition = e
		pass

	def prepareMasterIndex(self):
		SQLstatement = """
		CREATE TABLE IF NOT EXISTS "Extractions" (
			"idRecord"	INTEGER NOT NULL UNIQUE,
			"TableName"	TEXT NOT NULL UNIQUE,
			"ExtractionDate"	TEXT NOT NULL,
			"ExtractionTime"	TEXT NOT NULL,
			PRIMARY KEY("idRecord")
		);
		"""
		if (self.status == 0):
			try:
				c = self.connection.cursor()
				c.execute(SQLstatement)
			except Error as e:
				self.status = 2
				self.condition = e
		pass

	def prepareNewExtraction(self):
		SQLstatement = f"""
		CREATE TABLE IF NOT EXISTS "{self.currentTableName}" (
			"IDrecord"	INTEGER NOT NULL UNIQUE,
			"DateExecuted"	TEXT,
			"TimeExecuted"	TEXT,
			"TimeZone"	TEXT,
			"hostname"	TEXT NOT NULL,
			"mainIPaddress"	TEXT,
			"isUP"	INTEGER,
			"otherIPaddresses"	TEXT,
			"reverseDNShostname"	TEXT,
			"fullResult"	BLOB,
			PRIMARY KEY("IDrecord" AUTOINCREMENT)
		);
		"""
		if (self.status == 0):
			try:
				c = self.connection.cursor()
				c.execute(SQLstatement)
				if (self.status == 0):
					self.insertExtractionSummary()
			except Error as e:
				self.status = 2
				self.condition = e
		pass

	def insertExtractionSummary(self):
		record = (self.currentTableName,self.extractionDate,self.extractionTime)
		SQL = 'INSERT INTO Extractions (TableName, ExtractionDate, ExtractionTime) VALUES(?,?,?)'
		try:
			c = self.connection.cursor()
			c.execute(SQL,record)
			self.connection.commit()
		except Error as e:
			self.status = 3
			self.condition = e
		pass

	def insertExtractionRecord(self,DateExecuted,TimeExecuted,TimeZone,hostname,mainIPaddress,isUP,otherIPaddresses,reverseDNShostname,fullResult):
		record = (DateExecuted,TimeExecuted,TimeZone,hostname,mainIPaddress,isUP,otherIPaddresses,reverseDNShostname,fullResult)

		
		SQL = f"INSERT INTO {self.currentTableName}"
		SQL += "(DateExecuted,TimeExecuted,TimeZone,hostname,"
		SQL += "mainIPaddress,isUP,otherIPaddresses,reverseDNShostname,"
		SQL += "fullResult) VALUES (?,?,?,?,?,?,?,?,?)"

		try:
			c = self.connection.cursor()
			c.execute(SQL,record)
			self.connection.commit()
		except Error as e:
			self.status = 4
			self.condition = e
		pass

	pass