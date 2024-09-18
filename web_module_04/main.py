import mimetypes
import urllib.parse 
import json
import logging
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = Path()

class GoItFrameWork(BaseHTTPRequestHandler):

    def do_GET(self):
      route = urllib.parse.urlparse(self.path)
      print(route.query)
      if route.path == "/index":
         self.send_html('index.html')
      elif route.path == "/message":
         self.send_html('message.html')
      else:
         file = BASE_DIR.joinpath(route.path[1:])
         if file.exists():
            self.send_static(file)
         else:
            self.send_html('error.html', 404)

    def do_POST(self):
        size = self.headers.get('Content-Length')
        data = self.rfile.read(int(size))
        print(data)
        parse_data = urllib.parse.unquote_plus(data.decode())
        print(parse_data)
        try:
            parse_dict = {key: value for key, value in [el.split('=') for el in parse_data.split('&')]}
            print(parse_dict)
            with open ('storage/data.json', 'w', encoding='utf-8') as file:
                json.dump(parse_dict, file, ensure_ascii=False, indent=4)
        except ValueError as err:
            logging.error(err)
        except OSError as err:
            logging.error(err)
        self.send_response(302)
        self.send_header('Location', '/message')
        self.end_headers()

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def send_static(self, filename, status_code=200):
        self.send_response(status_code)
        mime_type, *_ = mimetypes.guess_type(filename)
        if mime_type:
            self.send_header('Content-Type', mime_type)
        else:
            self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

def run_server():
    address = ('localhost', 3000)
    http_server = HTTPServer(address, GoItFrameWork)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()

if __name__ == '__main__':
    run_server()