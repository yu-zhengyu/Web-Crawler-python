########################
# Breath-First crawler #
########################

import check
import crawler_utils
import heapq
import MySQLdb as mdb
import os
import re
import sys
import threading
import time
import urlparse
import urllib
from bs4 import BeautifulSoup
from collections import deque
from time import ctime,sleep
import wordcloudprint

start_url = "http://www.geeksforgeeks.org"

# BFS
urls = deque([start_url]) # stack of urls
visitied = [] # history record of url


# Min heap to keep track of top 10 urls with the highest contribution of relevant pages
heap = []
heap_size = 10

def bfs_search(keyword):
	# Create image directory under current path if not exists
	directory = os.getcwd() + "/image"
	print "Image directory: " + directory
	if not os.path.exists(directory):
		os.makedirs(directory)

	keyword = keyword.lower()
	
	
	#Check if there is a record in database, if yes, user can choose start from previous point or restart again
	global urls
	check.selectModel(keyword, "bfs", urls, visitied)
	
	while len(urls) > 0:
		try:
		
			time.sleep(2)
			htmltext = urllib.urlopen(urls[0]).read()
			soup = BeautifulSoup(htmltext, "lxml")
			visitied.append(urls[0])
			print "There are still " + str(len(urls)) + " websites to visit in the queue" 
			print "We are visiting:"
			print "Link: " + urls[0]
			title = soup.title.text
			print "Title: " + soup.title.text
			
			crawler_utils.save_data_in_DB(soup.title.text, urls[0], time.strftime('%Y-%m-%d-%H-%M-%S', \
				time.localtime(time.time())), keyword + "_bfs")			
			urls.popleft()
			print "We already visited " + str(len(visitied)) + " websites" 
			
			count = 0
			#items = [x for x in soup.]
			for link in soup.findAll('a'):
				currentlink = link.get('href')
				if currentlink is not None and "http://" in currentlink:
					if currentlink not in visitied and keyword in currentlink and currentlink not in urls:
						count += 1
						urls.append(currentlink)
			

			# Score and rank the current page by number of relevant urls			
			if len(heap) < heap_size:	
				heapq.heappush(heap, (count, title))
			else:
				peek = heap[0]
				if (count > peek[0]):
					heapq.heapreplace(heap, (count, title))

			# Find and dowload images
			# To avoid flooding image directory, we only download first image found on every page
			image_tag = soup.find("img")
			if image_tag is not None:
				crawler_utils.download_image(directory, image_tag.get("src"))


		except KeyboardInterrupt:
			print "\nPausing...  (Hit ENTER to continue, type quit to exit, type print you can print the word cloud image for current webpage)"
			response = raw_input()
			if response == "print":
				wordcloudprint.printwordCloud(soup.p.get_text())
				
			if response == "quit":
				# Print out top pages by number of relevant urls			
				crawler_utils.get_top_scored_pages(heap)
				# When quit, store the visited and unvisitWebs into database
				crawler_utils.save_webs_in_two_list(keyword, "bfs", urls, visitied)
				break
			else:
				continue
	
	# Print out top ranked pages if haven't done so
	if len(heap) > 0:
		crawler_utils.get_top_scored_pages(heap)


