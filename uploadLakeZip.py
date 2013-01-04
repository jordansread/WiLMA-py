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
filePath = 'mendota_shape.zip'

if QA:
    pyGDP.WFS_URL    = 'http://cida-wiwsc-gdp2qa.er.usgs.gov:8082/geoserver/wfs'
    pyGDP.upload_URL = 'http://cida-wiwsc-gdp2qa.er.usgs.gov:8082/geoserver'
    pyGDP.WPS_Service    = 'http://cida.usgs.gov/qa/climate/gdp/utility/WebProcessingService'
    pyGDP.WPS_URL = 'http://cida.usgs.gov/qa/climate/gdp/process/WebProcessingService'

datasetURI    = 'dods://regclim.coas.oregonstate.edu:8080/thredds/dodsC/regcmdata/EH5/ena/Daily/RegCM3_Daily_ena_EH5.ncml'

# initialize pyGDP object
pyGDP 	   = pyGDP.pyGDPwebProcessing()


newName = d.choice(s.letters)+d.choice(s.letters)+d.choice(s.letters)+d.choice(s.letters)+d.choice(s.letters)+d.choice(s.letters)+'.zip'
print newName
os.rename(filePath,newName)
shpfile = pyGDP.uploadShapeFile(newName)
os.rename(newName,filePath)

URIs = pyGDP.getDataSetURI()
for u in URIs:
    print u


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
att = att[0]

val = pyGDP.getValues(shpfile,att)
val = val[0]

print 'Attribute search: passed'
print 'Value search: passed'

# time range
varID = pyGDP.getDataType(datasetURI)
varID = varID[0]
TR = pyGDP.getTimeRange(datasetURI,varID)
timeStart = TR[0]
timeEnd   = '1896'+timeStart[4:len(timeStart)]
print 'Time search: passed'


outputFile_handle = pyGDP.submitFeatureWeightedGridStatistics(
    shpfile,datasetURI,varID,timeStart,timeEnd,att,val)

print outputFile_handle

outputFile_handle = pyGDP.submitFeatureWeightedGridStatistics(
    shpfile,datasetURI,varID,timeStart,timeEnd,att,val)

print outputFile_handle
outputFile_handle = pyGDP.submitFeatureWeightedGridStatistics(
    shpfile,datasetURI,varID,timeStart,timeEnd,att,val)

print outputFile_handle
outputFile_handle = pyGDP.submitFeatureWeightedGridStatistics(
    shpfile,datasetURI,varID,timeStart,timeEnd,att,val)

print outputFile_handle
outputFile_handle = pyGDP.submitFeatureWeightedGridStatistics(
    shpfile,datasetURI,varID,timeStart,timeEnd,att,val)

print outputFile_handle
