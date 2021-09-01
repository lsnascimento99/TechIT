from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'techit@2021'
app.config['MYSQL_DB'] = 'temakitech'

mysql = MySQL(app)

@app.route('/teste', methods=['GET', 'POST'])
def index():
    id       = int(1)
    username = str('Lucas')
    password = str('teste')
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuarios(id,usuario,senha) VALUES (%s,%s, %s)", (id, username, password))
    mysql.connection.commit()
    cur.close()
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)

