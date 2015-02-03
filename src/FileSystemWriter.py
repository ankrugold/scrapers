import re
import logging
from urlparse import urlparse

class FileSystemWriter:

	def __init__(self, writerHead):
		self.writerHead = writerHead
	def write(self, url, data):
		logging.info("[Writer] Url : " + url)
		parsedUrl = urlparse(url)

		fileName = self.writerHead + parsedUrl.netloc + self.cleanWithDashes(parsedUrl.path + parsedUrl.query)
		fileToWrite = open(self.writerHead + parsedUrl.netloc + cleanWithDashes(parsedUrl.path + parsedUrl.query), "w")
		
		logging.info("Writing to : " + fileName)
		fileToWrite.write(data)
		
		logging.info("Finished writing to : " + fileName)
		fileToWrite.close()

	def cleanWithDashes(self, str):
		re.sub("[=&/]", "--", str)

