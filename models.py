import pymysql as mysqldb

def insertToliuyan(host,content):
	with mysqldb.connect('127.0.0.1',3306,'root','liuyan') as connect:
		cur = connect.cursor()
		cur.execute("INSERT INTO liuyan(host,content)VALUES('{}','{}')".format(host,content))
		connect.commit()
  
