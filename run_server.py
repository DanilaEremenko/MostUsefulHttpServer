from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys
import json


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.command == 'GET' and self.path[0:7] == '/?year=':
            try:
                year = int(self.path[7:])
            except:
                self._send_all(404, "BAD YEAR NUMBER")
                return

            if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                self._send_all(404, "12/09/%d" % year)
            else:
                self._send_all(404, "13/09/%d" % year)
        else:
            self._send_all(404, "BAD REQUEST")

    def _send_all(self, response, dataMessage):
        self.send_response(response)
        self.send_header('content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps({"errorCode": response, "dataMessage": dataMessage}).encode())


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
