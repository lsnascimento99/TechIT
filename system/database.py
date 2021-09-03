import mysql.connector
from mysql.connector import errorcode

class database():
  def __init__(self):
     self.config = {
      'user': 'root',
      'password': 'techit@2021',
      'host': '127.0.0.1',
      'database': 'temakitech',
      'raise_on_warnings': True
    }

  def abrirConexao(self):
    mysqlconnector = mysql.connector.connect(**self.config)

    return mysqlconnector
  
  def commitWork(self):
    mysqlconnector = mysql.connector.connect(**self.config)
    mysqlconnector.commit()

  





