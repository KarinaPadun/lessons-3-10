from http.server import HTTPServer, CGIHTTPRequestHandler
server_data = ('localhost', 2079)
server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()