from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.write_response(b'')

	def do_POST(self):
		content_length = int(self.headers.get('content-length', 0))
		body = self.rfile.read(content_length)
		self.write_response(body)

	def write_response(self, content):
		self.send_response(200)

		self.end_headers()
		# print(self.headers)
		print("-- ENTER YOUR COMMAND --")
		command = input()
		self.wfile.write(command.encode())
		print(content.decode('utf-8'))

def main():
	PORT = 5000
	server_address = ('', PORT)
	server = HTTPServer(server_address, SimpleRequestHandler)
	print("server running on %s : %s" % (server_address,PORT) )
	server.serve_forever()

if __name__ == "__main__":
	main() 
