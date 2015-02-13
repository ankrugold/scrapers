import os
import re
import logging
from urlparse import urlparse

class FileSystemWriter:

	def __init__(self, writerHead):
		self.writerHead = writerHead
	def write(self, url, data):
		logging.info("[Writer] Url : " + url)
		parsedUrl = urlparse(url)
		
		if not (os.path.exists(self.writerHead + "/" + parsedUrl.netloc)):
			os.makedirs(self.writerHead + "/" + parsedUrl.netloc)
		fileName = self.writerHead + "/" + parsedUrl.netloc + "/" + self.cleanWithDashes(parsedUrl.path + parsedUrl.query)
		fileToWrite = open(fileName, "w")
		
		logging.info("Writing to : " + fileName)
		fileToWrite.write(data.encode('utf8'))
		
		logging.info("Finished writing to : " + fileName)
		fileToWrite.close()

	def cleanWithDashes(self, string):
		return re.sub("[=&/]", "--", string)

