import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nextcloud",
  password="Blackbird77",
  database="nextcloud"
)

mycursor = mydb.cursor()