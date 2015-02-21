import sqlite3
import sys

usage = "Usage: python parser.py dataFile"

if len(sys.argv) < 2:
	print usage
	sys.exit(1)

conn = sqlite3.connect('incidents.db')
c = conn.cursor()

data_file = open(sys.argv[1], 'r')

headers = None

data = {}

incidents = []
for line in data_file:
	if not headers:
		headers = True

	fields = line.split("\t")

	print fields

	aggregate_level = fields[0]
	
	# TODO - parse other fields and insert into database
	incident = (
		aggregate_level,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None,
		None
		)

	incidents.append(incident)
c.executemany('INSERT INTO incidents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', incidents)
c.close()
conn.commit()
conn.close()