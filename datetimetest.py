from urllib2 import urlopen
from json import *
# IMPORT
from datetime import datetime

url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164"
#channel_id = user input here
#url += channel_id
url += "&format=json"

response = urlopen(url)
json_obj = load(response)

try:
    json_time = json_obj['playlist']['song']['starttimeutc'][6:19]
    int_time = int(json_time)
    py_time = datetime.fromtimestamp(int_time / 1e3)
    start_time = datetime.time(py_time)
    # change print to return
    print "Now playing", start_time

except KeyError:
    try: 
        json_time = json_obj['playlist']['previoussong']['starttimeutc'][6:19]
        int_time = int(json_time)
        py_time = datetime.fromtimestamp(int_time / 1e3)
        start_time = datetime.time(py_time)
        # change print to return
        print "Last song started", start_time

    except KeyError:
        json_time = json_obj['playlist']['nextsong']['starttimeutc'][6:19]
        int_time = int(json_time)
        py_time = datetime.fromtimestamp(int_time / 1e3)
        start_time = datetime.time(py_time)
        # change print to return
        print "Next song will start", start_time

#Se JSONkod vid behov
mer_kod = raw_input("Se JSONkod? Y/N: ")
if mer_kod == "Y" or mer_kod == "y":
    print json_obj
