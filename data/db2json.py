# Reads incidents from SQLite DB, calculates some stats, and outputs in JSON form

import json
import sqlite3
import sys

if len(sys.argv) < 2:
	usage = "Usage: python " + sys.argv[0] + " sqlite.db"
	print usage
	sys.exit(1)

conn = sqlite3.connect('incidents.db')
c = conn.cursor()

data = {}
ethnicities = {}
for row in c.execute("""SELECT ethnicity, SUM(total) FROM incidents WHERE name = 'Oakland Unified' GROUP BY ethnicity ;"""):
    
	ethnicities[row[0]] = row[1]

	data['ethnicities'] = ethnicities

c.execute("""SELECT SUM(num_weapons), SUM(drugs), SUM(violence_with_injury), SUM(violence_without_injury), SUM(other_non_defiance), 
		SUM(other_defiance)
		FROM incidents WHERE name = 'Oakland Unified';""")
row = c.fetchone()

weapons = row[0]
drugs = row[1]
violence_with_injury = row[2]
violence_without_injury = row[3]
other_non_defiance = row[4]
other_defiance = row[5]

data['category_summaries'] = {'weapons': weapons, 'drugs': drugs, 'violence_with_injury': violence_with_injury,
	'violence_without_injury': violence_without_injury, 'other_non_defiance': other_non_defiance, 'other_defiance': other_defiance
	}

justified = weapons + drugs + violence_with_injury + violence_without_injury
other = other_non_defiance + other_defiance
percent = other / (float(justified)+ other)
data['justified_vs_other'] = {'justified': justified, 'other': other, 'percent_other': percent}

print json.dumps(data)
conn.close()
