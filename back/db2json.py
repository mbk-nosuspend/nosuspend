import json
import sqlite3

conn = sqlite3.connect('incidents.db')
c = conn.cursor()

data = {}
ethnicities = {}
for row in c.execute("""select ethnicity, count(*) from incidents 
	where aggregate_level = 'school_totals' AND CAST(cds as TEXT) LIKE '1612590%' 
	group by ethnicity;"""):
    
	ethnicities[row[0]] = row[1]

	data['ethnicities'] = ethnicities

print json.dumps(data)
conn.close()	