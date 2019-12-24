from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys
from datetime import datetime


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.command == 'GET' and self.path[0:7] == '/?year=':
            try:
                year = int(self.path[7:])
            except:
                self.wfile.write(b'BAD REQUEST')
                return

            self.send_header('content-type', 'text/xml')
            self.end_headers()
            self.send_response(200)

            if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                self.wfile.write("12/09/%d" % year)
            else:
                self.wfile.write("13/09/%d" % year)
        else:
            self.send_header('content-type', 'text/xml')
            self.end_headers()
            self.send_response(404)


def signal_handler(sig, frame):
    print('Exiting server')
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    print("Setting SIGINT handler")

    serv = HTTPServer(('', 8080), HttpProcessor)
    print("Running server")
    serv.serve_forever()


if __name__ == '__main__':
    main()
