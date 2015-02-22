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


data['justified_vs_other'] = {'weapons': row[0], 'drugs': row[1], 'violence_with_injury': row[2],
	'violence_without_injury': row[3], 'other_non_defiance': row[4], 'other_defiance': row[5],
	}

print json.dumps(data)
conn.close()
