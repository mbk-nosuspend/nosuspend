import json
import sqlite3

conn = sqlite3.connect('incidents.db')
c = conn.cursor()

data = {}
ethnicities = {}
for row in c.execute("""SELECT ethnicity, SUM(total) FROM incidents WHERE name = 'Oakland Unified' GROUP BY ethnicity ;"""):
    
	ethnicities[row[0]] = row[1]

	data['ethnicities'] = ethnicities


print json.dumps(data)
conn.close()