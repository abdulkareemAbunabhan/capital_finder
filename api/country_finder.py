from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
     def do_GET(self):
        path= self.path
        url_components=parse.urlsplit(path)
        query_string_list=parse.parse_qsl(url_components.query)
        params=dict(query_string_list)
        capital_name=params.get("capital_name")
        if(capital_name):
            url=f"http://api.geonames.org/searchJSON?q={capital_name}&featureCode=PPLC&maxRows=1&username=abdulkareem98"
            resp=requests.get(url)
            data=resp.json()
            country_name=data["geonames"][0]["countryName"]
        else:
            country_name="Nothing"
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(country_name.encode('utf-8'))
        return