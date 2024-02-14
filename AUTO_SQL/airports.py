import pandas as pd


data = pd.read_csv('archive (2)/airports.csv')
loc = []

with open('location.txt', 'w') as l, open('airports.txt', 'w') as a:
    for i in range(0, len(data)):
        this = data.iloc[i]

        CODE = this['IATA_CODE']
        NAME = this['AIRPORT']
        CITY = this['CITY']
        STATE = this['STATE']

        a.write('(\'' + CODE + '\', \'' + CITY + '\', \'' + STATE + '\', \'' + NAME + '\'),\n')

        if (CITY + STATE) not in loc:
            loc.append(CITY + STATE)
            l.write('(\'' + CITY + '\', \'' + STATE + '\'),\n')
