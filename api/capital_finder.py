from http.server import BaseHTTPRequestHandler
import requests 
class handler(BaseHTTPRequestHandler):
    base_url=f"http://api.geonames.org/searchJSON?q={country_name}&featureCode=PPLC&maxRows=1&username=abdulkareem98"
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "geonames" in data and len(data["geonames"]) > 0:
            capital = data["geonames"][0]["capital"]
            capital
    
    # return None    def do_GET(self):
    #     self.send_response(200)
    #     self.send_header('Content-type','text/plain')
    #     self.end_headers()
    #     self.wfile.write('Hello, world!'.encode('utf-8'))
    #     return