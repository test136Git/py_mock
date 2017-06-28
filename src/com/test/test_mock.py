#!/bin/env/python
#-*- coding:UTF-8 -*-
'''
Created on 2017年6月25日

@author: x
'''
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import time
import logging
import random
from pip._vendor.distlib._backport.tarfile import filemode
from pip._vendor.requests.api import request
import uuid

i=1
log_filename="pymock.log"
logging.basicConfig(filename=log_filename,filemode='w',level=logging.DEBUG)
class FormPage(Resource):
    def render_GET(self,request):
        return '<html><body>this is get method response . <br>uuid=%s</body></html>'%(uuid.uuid1())
    
    def render_POST(self,request):
        request.responseHeaders.addRawHeader("Content-Type", "application/json; charset=utf-8")
        name = request.args['name'][0]
        print 'name=',name
        global i
        print 'post:[',i,']'
        i=i+1
        result = '{"result":"ok","getString":"%s","uuid":"%s"}'%(name,uuid.uuid1())
        return result
        #return name
logging.debug('begin:[%s]',time.ctime())
root=Resource()
root.putChild('', FormPage())
factory = Site(root)
reactor.listenTCP(80,factory)
reactor.run()

        