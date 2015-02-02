__author__ = 'agni'

import sys
from Crawler import Crawler
from Seeder import Seeder
from Parser import Parser

def main(argv):
	components = {
		"crawler" : Crawler().keepFetching(),
		"seeder"  : Seeder(Crawler(), sys.argv[1]).seed(),
		"parser"  : Parser()
	}	
	components[argv[0]]()


if __name__ == "__main__": 
	main(sys.argv[1:])
