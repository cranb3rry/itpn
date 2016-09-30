from HTMLParser import HTMLParser
from urllib2 import urlopen

response =  urlopen("http://example.com")

html = response.read()



class MyHTMLParser(HTMLParser):
		def handle_starttag(self, tag, attrs):
			print "Start tag", tag, attrs
			if tag == 'a':
				print attrs[0][0]
		def handle_endtag(self, tag):
			print "End tag", tag
		def handle_data(self, data):
			return

parser = MyHTMLParser()

parser.feed(html)

