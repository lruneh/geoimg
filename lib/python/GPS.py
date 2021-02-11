from geopy import distance
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
from GPSPhoto import gpsphoto

center_point = [{'lat': -7.7940023, 'lng': 110.3656535}]
test_point = [{'lat': -7.79457, 'lng': 110.36563}]
radius = 5 # in kilometer
center_point_tuple = tuple(center_point[0].values()) # (-7.7940023, 110.3656535)
test_point_tuple = tuple(test_point[0].values()) # (-7.79457, 110.36563)
dis = distance.distance(center_point_tuple, test_point_tuple).km
print("Distance: {}".format(dis)) # Distance: 0.0628380925748918
if dis <= radius:
    print("{} point is inside the {} km radius from {} coordinate".format(test_point_tuple, radius, center_point_tuple))
else:
    print("{} point is outside the {} km radius from {} coordinate".format(test_point_tuple, radius, center_point_tuple))


## The start of something new

gpsCoordinates = gpsphoto.getGPSData('Images/2020/08/IMG_20200807_161158.jpg')

print(gpsCoordinates)