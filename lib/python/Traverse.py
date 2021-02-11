import os
import gpsPhoto
import requests
import ReverseGeoLocation
import json
import db_connect
from datetime import datetime
import uuid

# Set the directory you want to start from
rootDir = '/var/www/html/nextcloud/data/lasse/files/Photos/'
output = ""

##Get all the guids
db_connect.mycursor.execute("SELECT guid FROM img_locations")
allguids = [row[0] for row in db_connect.mycursor.fetchall()]

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        #Call the functions in gpsPhoto
        fullFilePath = os.path.join(dirName, fname)
        
        #Check if this uid already is in the database
        uid = uuid.uuid3(uuid.NAMESPACE_DNS, fullFilePath)
        if(str(uid) in allguids):
            #If it is skip it
            continue
        try:
            gpsCoordinates = gpsPhoto.get_gps_info(fullFilePath)
        except:
            gpsCoordinates = "N/A"
            #print('There was an error reading the GPS information for file %s.' % fullFilePath)
        if(gpsCoordinates != "N/A"):
            #print('File: %s' % fullFilePath)
            if(len(gpsCoordinates) >= 1):
                location = ReverseGeoLocation.get_location(gpsCoordinates['Latitude'], gpsCoordinates['Longitude'])
                if(location is not None):
                    for k in location:
                        loc = type(k)
                        city, suburb, country = '','',''
                        try:
                            city = k['address']['city']
                        except:
                            city = 'No city'
                        try:
                            country = k['address']['country']
                        except:
                            city = 'No country'
                        try:
                            suburb = suburb = k['address']['suburb']
                        except:
                            city = 'No suburb'
                        try:
                            date = gpsCoordinates['Date']
                            date += ' '+gpsCoordinates['UTC-Time']
                            timeStamp = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
                        except:
                            timeStamp = None

                        sql = "INSERT INTO img_locations (path, timeStamp, country, city, suburb,lat,lon, guid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        val = (fullFilePath, timeStamp, country, city,suburb, gpsCoordinates['Latitude'], gpsCoordinates['Longitude'], str(uid))
                        db_connect.mycursor.execute(sql,val)
                        db_connect.mydb.commit()
                        output += suburb+', '+city+', '+country
print('The files have been traversed. Images that were not already in the database have been added.')
print('The following is a concatenated string of all the data added:')
print(output)