#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on 2017年6月28日

@author: x
'''
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import uuid

class MyHandler(BaseHTTPRequestHandler):
  
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Connection:keep-alive','close')
        self.end_headers()
        res='this is get method response uuid=%s'%uuid.uuid1()
        self.wfile.write(res)
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Connection:keep-alive','close')
        self.end_headers()
        res='{"name":"小明","age":"18","uuid":"%s"}'%uuid.uuid1()
        self.wfile.write(res)
    
def run():
    try:
        server=HTTPServer(('',80),MyHandler)
        server.timeout=1000
        print 'start'
        #server.handle_request()
        server.serve_forever()
    except KeyboardInterrupt:
        print 'stop'
        server.socket.close()
if __name__=='__main__':
    run()