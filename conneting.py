import mysql.connector
from mysql.connector.fabric.connection import _validate_ssl_args
mydb = mysql.connector.connect(host='localhost',user='root',passwd='2846', database='test')

print('connected succefully')





