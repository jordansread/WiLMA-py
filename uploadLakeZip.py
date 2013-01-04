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

QA = True #if true, reset locations for services to QA servers
filePath = '/Volumes/projects/WiLMA/zippedLakes/'

if QA:
    pyGDP.WFS_URL    = 'http://cida-wiwsc-gdp2qa.er.usgs.gov:8082/geoserver/wfs'
    pyGDP.upload_URL = 'http://cida-wiwsc-gdp2qa.er.usgs.gov:8082/geoserver'
    pyGDP.WPS_Service    = 'http://cida.usgs.gov/qa/climate/gdp/utility/WebProcessingService'
    pyGDP.WPS_URL = 'http://cida.usgs.gov/qa/climate/gdp/process/WebProcessingService'

# initialize pyGDP object
pyGDP 	   = pyGDP.pyGDPwebProcessing()

for filename in os.listdir(filePath):
	print filename

shpNm = 'WiLMA_lake_100000'
try:
	shpfile = pyGDP.uploadShapeFile(filePath+shpNm+'.zip')
except Exception, msg:
	shpfile = shpNm
	print msg


# get attributes
att = pyGDP.getAttributes(shpfile)


val = pyGDP.getValues(shpfile,att[0])
for v in val:
	print v


