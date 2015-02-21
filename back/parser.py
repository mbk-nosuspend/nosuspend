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
		continue

	fields = line.split("\t")

	incident = {}

	aggregate_level = fields[0]
	incident['aggregate_level'] = aggregate_level

	# TODO - parse other fields and add to map
	cds=fields[1]
	incident['cds'] = cds

	name=fields[2]
	incident['name'] = name

	discipline_type=fields[3]
	
	if discipline_type=='E':
		discipline_type='expulsion'
	if discipline_type=='I':
		discipline_type='In-School Suspension'
	if discipline_type=='O':
		discipline_type='Out-of-School Suspension'
	incident['discipline_type'] = discipline_type

	ethnicity= int(fields[4])
	if ethnicity==0:
		ethnicity='not recorded'
	if ethnicity==1:
		ethnicity='American Indian or Alaskan Native'
	if ethnicity==2:
		ethnicity='Asian'
	if ethnicity==3:
		ethnicity='Pacific Islander'
	if ethnicity==4:
		ethnicity='Filipino'
	if ethnicity==5:
		ethnicity='Hispanic/Latino'
	if ethnicity==6:
		ethnicity='African American'
	if ethnicity==7:
		ethnicity='White'
	if ethnicity==9:
		ethnicity='Two or more races'
	incident['ethnicity'] =ethnicity










	data.append(incident)

print data[1]