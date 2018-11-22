#!/usr/bin/python
from os import curdir, sep
from bs4 import BeautifulSoup as Soup
import datetime

if __name__ == '__main__':
	print("============ Test Python script ============")
	
	f = open("test.html", "r")
	html = f.read()
	f.close()

	soup = Soup(html)

	lastUpdated = soup.find(id="lastUpdated")
	lastUpdated.clear()
	lastUpdated.insert(0, str(datetime.datetime.now()))

	print(soup)

	# "w" overwrite file contents
	f = open("test.html", "w")
	f.write(soup.prettify())
	f.close()
