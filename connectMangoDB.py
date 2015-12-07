import pymongo

from scrapy.conf import settings

class MangoDBPipeline(object):
	
	def __init__(self):
		connection = pymongo.MangoClient(
			settings['MONGODB_SERVER'],
			settings['MONGODB_PORT']
		)
		
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]
		
	def process_item(self, item, spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing {0}!".format(data))
				
		if valid:
			self.collection.insert(dict(item))
			log.msg("website information added to MangoDB database!",
					level = log.DEBUG, spider = spider)
					
		return item