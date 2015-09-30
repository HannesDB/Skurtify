#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unicorns import storage
from unicorns.Unicorn import Unicorn
from bottle import *
import json


@route('/')
def start():
	storage.setup()

	unicorns = storage.fetchUnicorns()
	for unicorn in unicorns:
	    print str(unicorn.id) + ': ' + unicorn.name
	    print json.dumps(unicorn.toDict())
	print

@route('/<id>')
def bra(id):
	unicorn = storage.fetchUnicorn(id)
	print str(unicorn.id) + ': ' + unicorn.name
	print "reportedBy: " + unicorn.reportedBy
	return json.dumps(unicorn.toDict())

@route('/update/<id>', method=('PUT'))
def update(id):
	unicorn.reportedBy = u'Batman'
	storage.updateUnicorn(unicorn)
	unicorn = storage.fetchUnicorn(id)
	print str(unicorn.id) + ': ' + unicorn.name
	print "reportedBy: " + unicorn.reportedBy
	print

	unicorn = Unicorn()
	unicorn.name = u'Konstig enhörning'
	unicorn.description = u'Det här är ingen vacker enhörning'
	unicorn.reportedBy = u'Johan'
	unicorn.spottedWhere.name = u'Niagara'
	unicorn.spottedWhere.lat = 55.609183
	unicorn.spottedWhere.lon = 12.994875
	unicorn.spottedWhen = u'2015-09-22 20:14:00'
	unicorn.image = u'https://pbs.twimg.com/profile_images/512349801929650177/_hfDmaho.jpeg'
	storage.addUnicorn(unicorn)
	unicorn = storage.fetchUnicorn(5)
	print str(unicorn.id) + ': ' + unicorn.name
	print

	unicorns = storage.fetchUnicorns()
	print "Antal enhörningar: " + str(len(unicorns))
	storage.deleteUnicorn(5)
	unicorns = storage.fetchUnicorns()
	print "Antal enhörningar: " + str(len(unicorns))

run(host='localhost', port=8080, debug=True, reloader=True)