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

QA = True
filePath = '/Volumes/projects/WiLMA/zippedLakes/'

if QA:
    pyGDP.WFS_URL    = 'http://cida-wiwsc-gdp2qa.er.usgs.gov:8082/geoserver/wfs'
    pyGDP.upload_URL = 'http://cida-wiwsc-gdp2qa.er.usgs.gov:8082/geoserver'
    pyGDP.WPS_Service    = 'http://cida.usgs.gov/qa/climate/gdp/utility/WebProcessingService'
    pyGDP.WPS_URL = 'http://cida.usgs.gov/qa/climate/gdp/process/WebProcessingService'

datasetURI    = 'dods://regclim.coas.oregonstate.edu:8080/thredds/dodsC/regcmdata/EH5/ena/Daily/RegCM3_Daily_ena_EH5.ncml'

# initialize pyGDP object
pyGDP 	   = pyGDP.pyGDPwebProcessing()

shpfile = pyGDP.uploadShapeFile(filePath+'WiLMA_lake_10000.zip')


# query geoserver
shp = pyGDP.getShapefiles()
fileFound = False
for s in shp:
    if s == shpfile:
        fileFound = True

if not fileFound:
    print 'file %s not found on geoserver' % shpfile
else:
    print 'file upload: passed'
    print 'file query: passed'

# get attributes
att = pyGDP.getAttributes(shpfile)
for a in att:
	print a

val = pyGDP.getValues(shpfile,att)
for v in val:
	print v


