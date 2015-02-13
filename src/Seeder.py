#!/usr/bin/python
__author__='agni'

import requests
import logging
from bs4 import BeautifulSoup
from urlparse import urlparse
from Util import Util

class Seeder:

	def __init__(self, crawler, site):
		self.crawler = crawler
		self.site = site
		self.siteConfig = Util().getSiteConfig(site)
		self.seedInitial()

	def seedInitial(self):
		logging.info("Seeding initiating...")
		initialPages = self.siteConfig.get_list("initial_pages")
		initialSelects = self.siteConfig.get_list("seeder.initial_selects")
		self.crawler.queue.put(initialPages)
		for page in initialPages:
			self.crawler.queue.put(self.seedOnePage(initialSelects))
	#Infinitely recursive. But should stop/wait once the queue finishes. Same holds for Crawler's keepFetching method.
	def seed(self):
		while True:
			self.crawler.queue.put(self.seedOnePage(self.siteConfig.get("seeder.final_selects")))
	def seedOnePage(self, selects):
		page = self.crawler.fetchAndWrite()
		seeds = []
		for select in selects:
			soup = BeautifulSoup(page)
			seeds.extend(self.seedsFromSelects(soup, select))
		return seeds
	def seedsFromSelects(self, soup, select):
		seeds = []
		for s in soup.select(select):
			ref = urlparse(s.get("href"))
			seedUrl = ref
			if not ref.netloc:
				seedUrl = "http://" + self.site + "/" + ref.path
			seeds.append(seedUrl)
		return seeds
