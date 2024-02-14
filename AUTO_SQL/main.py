import pandas as pd
import math


def exists(istr):
    try:
        return math.isnan(float(istr))
    except:
        return False


data = pd.read_csv('flights.csv')

flight_id = 0
delay_id = 0
cancel_id = 0
with open('flight.txt', 'w') as f, open('delayed.txt', 'w') as d, open('iscancelled.txt', 'w') as isc:
    for i in range(0, len(data)):
        this = data.iloc[i]

        MONTH = (this['MONTH'])
        DAY = (this['DAY'])
        DAY_OF_WEEK = (this['DAY_OF_WEEK'])

        OFFERED_BY = this['AIRLINE']
        SOURCE = this['ORIGIN_AIRPORT']
        DEST = this['DESTINATION_AIRPORT']
        IS_CANCELLED = this['CANCELLATION_REASON']
        SCHEDULED = (this['SCHEDULED_DEPARTURE'])

        AIR_SYSTEM = 0
        if math.isnan(this['AIR_SYSTEM_DELAY']) is False:
            AIR_SYSTEM = int(this['AIR_SYSTEM_DELAY'])

        SECURITY = 0
        if math.isnan(this['SECURITY_DELAY']) is False:
            SECURITY = int(this['SECURITY_DELAY'])

        INTERNAL = 0
        if math.isnan(this['AIRLINE_DELAY']) is False:
            INTERNAL = int(this['AIRLINE_DELAY'])

        AIRCRAFT = 0
        if math.isnan(this['LATE_AIRCRAFT_DELAY']) is False:
            AIRCRAFT = int(this['LATE_AIRCRAFT_DELAY'])

        WEATHER = 0
        if math.isnan(this['WEATHER_DELAY']) is False:
            WEATHER = int(this['WEATHER_DELAY'])

        to_write = ''

        if exists(IS_CANCELLED) is True:
            to_write = 'NULL'
        else:
            to_write = '\'' + IS_CANCELLED + '\''
            isc.write('(' + str(cancel_id) + ', ' + str(flight_id) + ', \'' + IS_CANCELLED + '\'),\n')
            cancel_id += 1

        f.write('(' + str(flight_id) + ', \'' + SOURCE + '\', \'' + DEST + '\', \'' + OFFERED_BY + '\', ' + to_write +
                ', ' + str(MONTH) + ', ' + str(DAY) + ', ' + str(DAY_OF_WEEK) + ', ' + str(SCHEDULED) + '),\n')

        if AIR_SYSTEM != 0:
            d.write('(' + str(delay_id) + ', \'AIR_SYSTEM\', ' + str(flight_id) + ', ' + str(AIR_SYSTEM) + '),\n')
            delay_id += 1
        if SECURITY != 0:
            d.write('(' + str(delay_id) + ', \'SECURITY\', ' + str(flight_id) + ', ' + str(SECURITY) + '),\n')
            delay_id += 1
        if INTERNAL != 0:
            d.write('(' + str(delay_id) + ', \'INTERNAL\', ' + str(flight_id) + ', ' + str(INTERNAL) + '),\n')
            delay_id += 1
        if AIRCRAFT != 0:
            d.write('(' + str(delay_id) + ', \'AIRCRAFT\', ' + str(flight_id) + ', ' + str(AIRCRAFT) + '),\n')
            delay_id += 1
        if WEATHER != 0:
            d.write('(' + str(delay_id) + ', \'WEATHER\', ' + str(flight_id) + ', ' + str(WEATHER) + '),\n')
            delay_id += 1

        flight_id = flight_id + 1

        if flight_id > 1000 and delay_id > 1000 and cancel_id > 1000:
            print(flight_id)
            break
