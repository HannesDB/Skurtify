#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from json import *
from datetime import datetime

def song_time(sr_json):
    '''Gets the time the song started playing'''
    try:
        start_time = sr_json['playlist']['song']['starttimeutc'][6:19]
        start_time = int(start_time)
        start_time = datetime.fromtimestamp(start_time / 1e3)
        start_time = datetime.time(start_time)
        return str(start_time)[0:8]

    except KeyError:
        try:
            start_time = sr_json['playlist']['previoussong']['starttimeutc'][6:19]
            start_time = int(start_time)
            start_time = datetime.fromtimestamp(start_time / 1e3)
            start_time = datetime.time(start_time)
            return str(start_time)[0:8]

        except KeyError:
            start_time = sr_json['playlist']['nextsong']['starttimeutc'][6:19]
            start_time = int(start_time)
            start_time = datetime.fromtimestamp(start_time / 1e3)
            start_time = datetime.time(start_time)
            return str(start_time)[0:8]
