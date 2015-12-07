import MySQLdb as mdb
import sys

def saveDataInDB(title, link, time, keyword): 
	con = mdb.connect('localhost', 'root', 'root', 'test');
	sql = "INSERT INTO " + "KeyWord" + keyword + "(Title, Link, Time) VALUES('%s', '%s', '%s')" %(title,link,time)
	with con:
		cur = con.cursor()		
		cur.execute(sql)
		
	con.close()
	return

def saveCurrentInfo(link, keyword):
	con = mdb.connect('localhost', 'root', 'root', 'test');	
	sql = "INSERT INTO " + keyword + "(Link) VALUES('%s')" %(link)
	with con:
		cur = con.cursor()		
		cur.execute(sql)
		
	con.close()
	return
	
def saveWebsInTwoList(keyword, pattern, urls, visitied):
	con = mdb.connect('localhost', 'root', 'root', 'test') 
	sql = "CREATE TABLE IF NOT EXISTS " + keyword + "visited_" + pattern + "(Id INT PRIMARY KEY AUTO_INCREMENT, Link Text)"		 
	sqlun = "CREATE TABLE IF NOT EXISTS " + keyword + "unvisited_" + pattern + "(Id INT PRIMARY KEY AUTO_INCREMENT, Link Text)"	
	with con:
		cur = con.cursor()
		cur.execute("drop table if exists " + keyword + "visited_" + pattern)
		cur.execute("drop table if exists " + keyword + "unvisited_" + pattern)
		cur.execute(sql)
		cur.execute(sqlun)
	con.close()	
	
	# When quit, store the visited and unvisitWebs into database
	for visitlink in visitied:
		saveCurrentInfo(visitlink, keyword + "visited_" + pattern)
	
	
	for unvisitlink in urls:				
		saveCurrentInfo(unvisitlink, keyword + "unvisited_" + pattern)