#############################################################################
#  Utilitiy functions shared by DFS and BFS crawlers. Set aside to improve  # 
#  code reusability              											#
#############################################################################

import heapq
import os
import urllib
from prettytable import PrettyTable

def get_top_scored_pages(heap):
	print "Top 10 Pages By Number of Relevant URLs: \n"
	table = PrettyTable(['Rank', 'Page Title', 'Number of Relevant URLs'])
	rank = len(heap)
	while len(heap) > 0:
		item = heapq.heappop(heap)
		table.add_row([rank, item[1], item[0]])
		rank -= 1
	print table

def download_image(image_directory, image_url):
	print "An image is found. Dowloading from " + image_url
	urllib.urlretrieve(image_url, image_directory + "/" 
			+ os.path.basename(image_url))			