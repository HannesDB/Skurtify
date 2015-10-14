from urllib2 import urlopen
from json import *
# IMPORT
from datetime import datetime

def song_time(json_obj):

    try:
        json_time = json_obj['playlist']['song']['starttimeutc'][6:19]
        int_time = int(json_time)
        py_time = datetime.fromtimestamp(int_time / 1e3)
        start_time = datetime.time(py_time)
        # change print to return
        return start_time

    except KeyError:
        try: 
            json_time = json_obj['playlist']['previoussong']['starttimeutc'][6:19]
            int_time = int(json_time)
            py_time = datetime.fromtimestamp(int_time / 1e3)
            start_time = datetime.time(py_time)
            # change print to return
            return start_time

        except KeyError:
            json_time = json_obj['playlist']['nextsong']['starttimeutc'][6:19]
            int_time = int(json_time)
            py_time = datetime.fromtimestamp(int_time / 1e3)
            start_time = datetime.time(py_time)
            # change print to return
            return start_time
