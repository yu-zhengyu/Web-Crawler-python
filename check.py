import MySQLdb as mdb
import sys

def selectModel(keyword, pattern, urls, visitied):
	con = mdb.connect('localhost', 'root', 'root', 'test') 
	tableName = "keyword" + keyword + "_" + pattern
	sql = "CREATE TABLE IF NOT EXISTS " + tableName + "(Id INT PRIMARY KEY AUTO_INCREMENT,  Title Text, Link Text, Time DATETIME )"		 
	with con:
		cur = con.cursor()
		cur.execute("show tables")
		tables = cur.fetchall()
		table = (tableName,)
		tableVisited = (keyword + "visited_" + pattern,)
		if(table in tables):
			print "The KeyWord had been crawled before. Do you want to restart from the previous point? (Hit yes or no)"
			answer = raw_input()
			
			if answer == "yes":  #Get the visited and unvisitWebs from database and put them in current stack or queue
				if(pattern == "bfs"):
					urls.popleft()
				else:
					urls.pop()
				if(tableVisited in tables):
					cur.execute("select * from " + keyword + "visited_" + pattern)
					visitWebs = cur.fetchall()
					cur.execute("select * from " + keyword + "unvisited_" + pattern)
					unvisitWebs = cur.fetchall()
					
					for web in visitWebs:
						#print web[1]
						visitied.append(web[1])
						
					#print "debug"
					for web in unvisitWebs:
					#	print web[1]
						urls.append(web[1])
				else:
					print "We already finished this keyword before. You can check the result in database."
			else:
				cur.execute("drop table if exists " + tableName)
				cur.execute("drop table if exists " + keyword + "visited_" + pattern)
				cur.execute("drop table if exists " + keyword + "unvisited_" + pattern)
				cur.execute(sql)
				
		else:
			cur.execute(sql)
				
				
	con.close()	