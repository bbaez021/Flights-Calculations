"""APP.PY for flask"""
import cloud_connect as cc
from flask import Flask, render_template, request

app = Flask(__name__)

# basic show homepage
@app.route("/")
def homepage():
    """Renders homepage"""
    return render_template("index.html")

# show most recent flights from specified airport
@app.route("/startingAirport", methods=['GET'])
def basicInfo():
    """Flask code for most_recent()"""
    airport = request.args.get('airport', '')
    myresult = cc.most_recent(airport)
    
    result = "FLIGHT_ID | SOURCE_AIRPORT | DESTINATION_AIRPORT | OFFERED_BY | IS_CANCELLED | MONTH | DAY  | DAY_OF_WEEK | SCHEDULED_DEPARTURE"
    for x in myresult:
        result += "<li>" + str(x) + "</li>"
    return result

# calculate delay/cancellation probability
@app.route("/calcProbability", methods=['GET'])
def calcDelayProb():
    """Flask code for delay_probability"""
    src = request.args.get('src', '')
    dest = request.args.get('dest', '')
    
    print(src)
    print(dest)
    
    results = cc.delay_probability(src, dest)
    return results

# delete flight
@app.route("/deleteFlight", methods=['DELETE'])
def deleteFlight():
    """Flask code for delete flight"""
    flight_id = request.args.get('id', '')
    result_from_action = cc.delete_flight(flight_id)
    if result_from_action is True:
        return "SUCCESS: Deleted flight " + flight_id
    return "Delete failed"

# update flight
@app.route("/updateFlight", methods=['PUT'])
def updateFlight():
    """flask code for update flight"""
    flight_id = request.args.get('id', '')
    update_src = request.args.get('src', '')
    update_dest = request.args.get('dest', '')

    result_from_action = cc.update_flight(flight_id, update_src, update_dest)
    
    if result_from_action is True:
        return "SUCCESSFULLY UPDATED FLIGHT " + flight_id
    else:
        return "Update failed"

# insert flight
@app.route("/insertFlight", methods=['PUT'])
def insertFlight():
    """flask code for insert flight"""
    src = request.args.get('src', '')
    dest = request.args.get('dest', '')
    off_by = request.args.get('off_by', '')
    is_canc = request.args.get('is_canc', '')
    month = request.args.get('month', '')
    day = request.args.get('day', '')
    dow = request.args.get('dow', '')
    departure = request.args.get('departure', '')

    data = [{'MONTH': month,
            'DAY': day,
            'DAY_OF_WEEK': dow,
            'OFFERED_BY': off_by,
            'SRC': src,
            'DEST': dest,
            'CANCELLED': is_canc,
            'SCHEDULED': departure
            }]

    result_from_action = cc.insert_flight(data)
    if result_from_action is True:
        return "SUCCESSFULLY ADDED FLIGHT"
    return "Insert failed"
