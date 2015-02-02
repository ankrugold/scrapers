#!/usr/bin/python
__author__='agni'

import requests
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
		initialPages = self.siteConfig.get("initial-pages")
		initialSelects = self.siteConfig.get("initial-selects")
		self.queue.put(initialPages)
		for page in initialPages:
			self.crawler.queue.put(self.seedOnePage(initialSelects))
	#Infinitely recursive. But should stop/wait once the queue finishes. Same holds for Crawler's keepFetching method.
	def seed(self):
		self.crawler.queue.put(seedOnePage(self.siteConfig.get("final-selects")))
		self.seed()
	def seedOnePage(self, selects):
		page = self.crawler.fetchAndWrite()
		seeds = []
		for select in selects:
			soup = BeautifulSoup(page)
			seeds.extend(seedsFromSelects(soup, select))
		return seeds
	def seedsFromSelects(self, soup, select):
		seeds = []
		for s in soup.select(select):
			ref = urlparse(s.get("href"))
			seedUrl = ref
			if not ref.netloc:
				seedUrl = "http://" + self.site + "/" + ref
			seeds.append(seedUrl)
		return seeds
