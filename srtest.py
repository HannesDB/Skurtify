from urllib2 import urlopen
from json import *

url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164"
#channel_id = user input here
#url += channel_id
url += "&format=json"

response = urlopen(url)
json_obj = load(response)
#'playlist' -> 'song' -> 'description'
try:
    json_song = json_obj['playlist']['song']['description']
    print json_song
#'playlist' -> 'nextsong' -> 'description'  
except KeyError:
    try:
        #'playlist' -> 'previoussong' -> 'description' 
        json_song = json_obj['playlist']['previoussong']['description']
        print json_song
    except KeyError:
        #'playlist' -> 'nextsong' -> 'description' 
        json_song = json_obj['playlist']['nextsong']['description']
        print json_song

#Se JSONkod vid behov
mer_kod = raw_input("Se JSONkod? Y/N: ")
if mer_kod == "Y" or mer_kod == "y":
    print json_obj



