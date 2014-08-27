from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re

def cleanHtml(i):
	i = str(i)
	boup = BeautifulSoup(i)

	
	##i = boup.find('').getText()
	boup = re.sub('<[^<]*?/?>','',i)
	
	boup = re.sub('</title>','',i)
	return i

listIterator = []
webpage = urlopen("http://www.gizmodo.com/").read()

soup = BeautifulSoup(webpage)

print cleanHtml(soup)





