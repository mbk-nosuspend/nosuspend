# NoSuspend
[NoSuspend](http://mbk-nosuspend.github.io/nosuspend) is an informational website built to raise awareness of the high suspensions rates in Oakland schools, especially for African-American and Hispanic youth. It was built over a weekend in February 2015 in Oakland, California as part of the My Brother's Keeper Hackathon ([#MBKHack](http://www.mbkhack.com/)) powered by Qeyno Labs.

## Generating data

Create the SQLite DB

    ./createDb.sh

Parse data and populate DB

    python parser_sql.py SuspExpData-2013-14.txt

Convert to JSON

    python db2json.py incidents.db > ../data.json

## Serve the site

    python -m SimpleHTTPServer 8000

[http://localhost:8000](http://localhost:8000)
