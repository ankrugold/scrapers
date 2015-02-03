#!/usr/bin/python
__author__ = 'agni'

import sys
from Seeder import Seeder
from Crawler import Crawler
import logging

def main(argv):
	logging.info("Looking in components for " + argv[0])
	components = {
		"seeder"  : Seeder(Crawler(), sys.argv[2]).seed()
	}	
	if len(argv > 1):
		components[argv[1]]()
	else:
		print "Not enough arguments. Exiting..."
		sys.exit(1)


if __name__ == "__main__": 
	main(sys.argv[1:])
