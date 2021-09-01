import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'techit@2021',
  'host': '127.0.0.1',
  'database': 'temakitech',
  'raise_on_warnings': True
}

mysqlconnector = mysql.connector.connect(**config)
