import urllib2
import urllib
import urlparse
import BaseHTTPServer
import webbrowser
import requests

from local_settings import *


APP_ID = '487585751296259'
ENDPOINT = 'graph.facebook.com'
REDIRECT_URI = 'http://localhost:8080'
ACCESS_TOKEN = None
SCOPE = 'publish_stream,user_groups'
FB_TOKEN_FILE = 'fb_token'


def get_url(path, args=None):
    args = args or {}
    endpoint = "http://" + ENDPOINT
    return endpoint + path + '?' + urllib.urlencode(args)


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        global ACCESS_TOKEN
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if self.path == '/?':
            self.serve_file('index.html')
        elif self.path == '/jquery.js':
            self.serve_file('jquery.js')
        elif self.path[:6] == '/token':
            end_pos = self.path.index('&')
            token = self.path[19:end_pos]
            self.wfile.write(token)
            ACCESS_TOKEN = token
        else:
            pass

    def serve_file(self, file_name):
        with open(file_name, 'r') as ftr:
            html = ftr.read()
        self.wfile.write(html)


if __name__ == '__main__':
    print "Logging you in to facebook..."
    webbrowser.open(get_url('/oauth/authorize',
                            {'client_id': APP_ID,
                             'redirect_uri': REDIRECT_URI,
                             'type': 'user_agent',
                             'scope': SCOPE}))

    httpd = BaseHTTPServer.HTTPServer(('127.0.0.1', 8080), RequestHandler)
    while ACCESS_TOKEN is None:
        httpd.handle_request()

    group_ids = ['154602824748935']
    post_to_group_url_template = 'https://graph.facebook.com/{group_id}/' \
                                 'feed?access_token=%s' % ACCESS_TOKEN
    for gid in group_ids:
        url = post_to_group_url_template.format(group_id=gid)
        r = requests.post(url, data={"message": 'hello'})
        print r.text
