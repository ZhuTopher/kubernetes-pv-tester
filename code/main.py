#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
from bs4 import BeautifulSoup as Soup
import datetime

PORT = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/res/index.html"

		if self.path=="/res/index.html":
			f = open(self.path, "r")
			html = f.read()
			f.close()

			soup = Soup(html)

			lastUpdated = soup.find(id="lastUpdated")
			lastUpdated.clear()
			lastUpdated.insert(0, str(datetime.datetime.now()))

			print(soup)

			# "w" overwrite file contents
			f = open(self.path, "w")
			f.write(soup.prettify())
			f.close()


		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			data = None 
			if self.path.endswith(".html"):
				mimetype='text/html'
				f = open(self.path)
				data = bytes(f.read(), 'UTF-8')
				f.close()
				sendReply = True

			if self.path.endswith(".png"):
				mimetype='image/png'
				f = open((self.path), "rb")
				data = f.read()
				f.close()
				sendReply = True

			if self.path.endswith(".jpeg") or self.path.endswith(".jpg"):
				mimetype='image/jpeg'
				f = open((self.path), "rb")
				data = f.read()
				f.close()
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				self.send_response(200)
				self.send_header('Content-type', mimetype)
				self.end_headers()
				self.wfile.write(data)
			else:
				#Return error message
				self.send_error(400,'Unsupported Endpoint: %s' % self.path)

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)


if __name__ == '__main__':
	print("============ Main Python script ============")
	try:
		#Create a web server and define the handler to manage the
		#incoming request
		server = HTTPServer(('0.0.0.0', PORT), myHandler)
		print('Started httpserver on port ' , PORT)
		
		#Wait forever for incoming htto requests
		server.serve_forever()

	except KeyboardInterrupt:
		print('^C received, shutting down the web server')
		server.socket.close()
