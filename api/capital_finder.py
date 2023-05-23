from http.server import BaseHTTPRequestHandler
import requests 
from urllib import parse
class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        path= self.path
        url_components=parse.urlsplit(path)
        query_string_list=parse.parse_qsl(url_components)
        params=dict(query_string_list)
        country_name=params.get("country_name")
        if(country_name):
            url=f"http://api.geonames.org/searchJSON?q={country_name}&featureCode=PPLC&maxRows=1&username=abdulkareem98"
            resp=requests.get(url)
            data=resp.json()
            capital_name=data["geonames"][0]["name"]
        else:
            capital_name="Nothing"
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(capital_name.encode('utf-8'))
        return