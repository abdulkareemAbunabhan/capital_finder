from http.server import BaseHTTPRequestHandler
import requests 
class handler(BaseHTTPRequestHandler):
 
    request=requests.get(f"http://api.geonames.org/searchJSON?q={capital_city_name}&featureCode=PPLC&maxRows=1&username=abdulkareem98")
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return