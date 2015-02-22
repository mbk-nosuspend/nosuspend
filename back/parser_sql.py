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

incidents = []
incidents_sql = []

def parse_int(val):
	if val == '*':
		return 0
	return int(val)

suspensions_by_ethnicity = {}

for line in data_file:
	if not headers:
		headers = True
		continue

	fields = line.split("\t")

	incident = {}

	agg_level = fields[0]
	if agg_level == 'D':
		agg_level = 'local_educational_agency_totals'
	elif agg_level == 'O':
		agg_level = 'county_level'
	elif agg_level == 'S':
		agg_level = 'school_totals'
	elif agg_level == 'T':
		agg_level = 'state_totals'

	incident['agg_level'] = agg_level

	# TODO - parse other fields and add to map
	cds=fields[1]
	incident['cds'] = cds

	if not cds.find('1612590'):
		continue

	name=fields[2]
	incident['name'] = name

	discipline_type=fields[3]
	if discipline_type=='E':
		discipline_type='expulsion'
	if discipline_type=='I':
		discipline_type='in_school_suspension'
	if discipline_type=='O':
		discipline_type='out_of_school_suspension'
	incident['discipline_type'] = discipline_type

	ethnicity= int(fields[4])
	if ethnicity==0:
		ethnicity='not_recorded'
	if ethnicity==1:
		ethnicity='american_indian_or_alaskan_native'
	if ethnicity==2:
		ethnicity='asian'
	if ethnicity==3:
		ethnicity='pacific_islander'
	if ethnicity==4:
		ethnicity='filipino'
	if ethnicity==5:
		ethnicity='hispanic_latino'
	if ethnicity==6:
		ethnicity='african_american'
	if ethnicity==7:
		ethnicity='white'
	if ethnicity==9:
		ethnicity='two_or_more'
	incident['ethnicity'] =ethnicity

	weapons = parse_int(fields[5])
	incident['num_weapons'] = weapons

	num_drugs = parse_int(fields[6])
	incident['num_drugs'] = num_drugs

	violence_with_injury = parse_int(fields[7])
	incident['num_violence_with_injury'] = violence_with_injury 

	violence_without_injury = parse_int(fields[8])
	incident['num_violence_without_injury'] = violence_without_injury

	other_non = parse_int(fields[9])
	incident['other_non_defiance'] = other_non

	other_defiance = parse_int(fields[10])
	incident['other_defiance'] = other_defiance

	total = parse_int(fields[11])
	incident['total'] = total

	year = fields[12]
	incident['year'] = year


	incidents.append(incident)
	incidents_sql.append(
		[agg_level, cds, name, discipline_type, ethnicity, weapons,
		num_drugs, violence_with_injury, violence_without_injury, other_non,
		other_defiance, total, year])

c.executemany('INSERT INTO incidents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', incidents_sql)
c.close()
conn.commit()
conn.close()