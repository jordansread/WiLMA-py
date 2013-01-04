#!/usr/bin/env python
# encoding: utf-8
"""
uploadLakeZip.py

Created by Jordan Read on 2013-01-04.
Copyright (c) 2013 USGS. All rights reserved.
"""
# ---- importing libraries, initializing pyGDP processing object

import pyGDP
import os

QA = False #if true, reset locations for services to QA servers
filePath = '/Volumes/projects/WiLMA/LTER_donuts/'

if QA:
    print 'using QA servers and services'
    pyGDP.WFS_URL    = 'http://cida-wiwsc-gdp2qa.er.usgs.gov:8082/geoserver/wfs'
    pyGDP.upload_URL = 'http://cida-wiwsc-gdp2qa.er.usgs.gov:8082/geoserver'
    pyGDP.WPS_Service    = 'http://cida.usgs.gov/qa/climate/gdp/utility/WebProcessingService'
    pyGDP.WPS_URL = 'http://cida.usgs.gov/qa/climate/gdp/process/WebProcessingService'

# initialize pyGDP object
pyGDP 	   = pyGDP.pyGDPwebProcessing()

for filename in os.listdir(filePath):
	try:
		shpfile = pyGDP.uploadShapeFile(filePath+filename),
		print 'successfully uploaded %r' % (shpfile)
		# get attributes
		att = pyGDP.getAttributes('%s' % (shpfile))
		val = pyGDP.getValues('%s' % (shpfile),att[1])
		for v in val:
			print '%s has attribute %s and value %s' % (shpfile,att[1],v)
	except Exception, msg:
		shpfile = filename[0:len(filename)-4]
		print '%s %s' % (shpfile,msg)




