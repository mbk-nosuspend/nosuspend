import sqlite3
import sys

usage = "Usage: python parser.py dataFile"

if len(sys.argv) < 2:
	print usage
	sys.exit(1)

data_file = open(sys.argv[1], 'r')

headers = None

data = []

for line in data_file:
	if not headers:
		headers = True

	fields = line.split("\t")

	incident = {}

	aggregate_level = fields[0]
	incident['aggregate_level'] = aggregate_level

	# TODO - parse other fields and add to map

	data.append(incident)

print data