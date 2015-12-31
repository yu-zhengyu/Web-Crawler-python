#############################################################################
#  Utilitiy functions shared by DFS and BFS crawlers. Set aside to improve  # 
#  code reusability              											#
#############################################################################

import heapq
import MySQLdb as mdb
import os
import sys
import urllib
from prettytable import PrettyTable

# Print out top-scored pages given a heap queue
def get_top_scored_pages(heap):
	print "Top 10 Pages By Number of Relevant URLs: \n"
	table = PrettyTable(['Rank', 'Page Title', 'Number of Relevant URLs'])
	rank = len(heap)
	while len(heap) > 0:
		item = heapq.heappop(heap)
		table.add_row([rank, item[1], item[0]])
		rank -= 1
	print table

# Download image from the given link
def download_image(image_directory, image_url):
	print "An image is found. Dowloading from " + image_url
	urllib.urlretrieve(image_url, image_directory + "/" 
			+ os.path.basename(image_url))

# Insert a new record into MySQL database
def save_data_in_DB(title, link, time, keyword): 
	con = mdb.connect('localhost', 'root', 'root', 'test');
	sql = "INSERT INTO " + "KeyWord" + keyword + "(Title, Link, Time) VALUES('%s', '%s', '%s')" %(title,link,time)
	with con:
		cur = con.cursor()		
		cur.execute(sql)
		
	con.close()
	return

# Save just the link and its respective keyword into MySQL database
def save_current_info(link, keyword):
	con = mdb.connect('localhost', 'root', 'root', 'test');	
	sql = "INSERT INTO " + keyword + "(Link) VALUES('%s')" %(link)
	with con:
		cur = con.cursor()		
		cur.execute(sql)
		
	con.close()
	return

# Batch saving webpages into MySQL database, based on whether or not the link has actually been visited 
# this function will provide a different tag for each link	
def save_webs_in_two_list(keyword, pattern, urls, visitied):
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
		save_current_info(visitlink, keyword + "visited_" + pattern)
	
	
	for unvisitlink in urls:				
		save_current_info(unvisitlink, keyword + "unvisited_" + pattern)			