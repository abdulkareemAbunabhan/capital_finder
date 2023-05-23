from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
     def do_GET(self):
        path= self.path
        url_components=parse.urlsplit(path)
        query_string_list=parse.parse_qsl(url_components)
        params=dict(query_string_list)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(params.encode('utf-8'))
        return