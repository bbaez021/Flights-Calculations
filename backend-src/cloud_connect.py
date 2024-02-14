'Connection to SQL Google cloud instance'
import os
#import pymysql
#import sqlalchemy
import mysql.connector

mydb = mysql.connector.connect(
    host="34.69.30.140",
    user="root",
    password="team112db",
    database="delayscancellations",
    port=3306
)

def most_recent(src):
    """show most recent flights from specified airport"""
    mycursor = mydb.cursor()
    sql = "SELECT * FROM FLIGHTS WHERE SOURCE_AIRPORT = '" + src + "' LIMIT 15;"

    mycursor.execute(sql)
    return mycursor.fetchall()


def delay_probability(src, dest):
    """calculate delay/cancellation probability"""
    mycursor = mydb.cursor(buffered=True)

    new_table = "SELECT * FROM FLIGHTS f WHERE f.SOURCE_AIRPORT = '" + src + "' AND f.DESTINATION_AIRPORT = '" + dest + "'"
    sql_query_1 = "SELECT ROUND(COUNT(rel.IS_CANCELLED) / COUNT(rel.FLIGHT_ID), 2) FROM (" + new_table + ") as rel"
    cond = "ROUND(COUNT(d.NAME) / COUNT(rel.FLIGHT_ID), 2)"
    sql_query_2 = "SELECT " + cond + " FROM (" + new_table + ") AS rel LEFT JOIN DELAYS d USING (FLIGHT_ID)"
    sql = "(" + sql_query_1 + ") UNION (" + sql_query_2 + ")"

    return mycursor.execute(sql)


def delete_flight(flight_id):
    """delete flight"""
    mycursor = mydb.cursor()
    new_table = "DELETE FROM FLIGHTS f WHERE f.FLIGHT_ID = " + flight_id
    try:
        mycursor.execute(new_table)
        return True
    except:
        return False


def update_flight(flight_id, new_src, new_dest):
    """update flight"""
    mycursor = mydb.cursor()
    update = "UPDATE FLIGHTS f "
    setq = "SET f.SOURCE_AIRPORT = '" + new_src + "', f.DESTINATION_AIRPORT = '" + new_dest + "' "
    where = "WHERE f.FLIGHT_ID = " + flight_id
    new_table = update + setq + where

    try:
        mycursor.execute(new_table)
        return True
    except:
        return False


def insert_flight(data):
    """insert flight"""
    mycursor = mydb.cursor()
    mycursor.execute("SELECT MAX(FLIGHT_ID) AS limit FROM FLIGHTS")
    size = mycursor.fetchall()
    size = int(size['limit']) + 1
    if data['IS_CANCELLED'] is None or data['IS_CANCELLED'] == "":
        data['IS_CANCELLED'] = "NULL"
    try:
        sql = (
        "INSERT INTO FLIGHTS (FLIGHT_ID, SOURCE_AIRPORT, DESTINATION_AIRPORT, OFFERED_BY, IS_CANCELLED, MONTH, DAY, DAY_OF_WEEK, SCHEDULED_DEPARTURE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        )

        mycursor.execute(sql, (size, data['src'], data['dest'], data['off_by'], data['is_canc'], data['month'], data['day'], data['dow'], data['departure']))
        return True
    except:
        return False
