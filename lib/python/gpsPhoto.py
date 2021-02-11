from GPSPhoto import gpsphoto

# Get the data from image file and return a dictionary
def get_gps_info(img):
    imgPath = 'Images/2020/08/IMG_20200807_161158.jpg'
    data = gpsphoto.getGPSData(img)
    rawData = gpsphoto.getRawData(img)
    return data