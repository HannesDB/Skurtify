from urllib2 import urlopen
from json import load

url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164"
#channel_id = "{{164}}"
#url += channel_id
url += "&format=json"

response = urlopen(url)
json_obj = load(response)

#Stringify. Shitty code.
str_obj = str(json_obj)
str_result = str_obj.split("'")
print str_result[19]


#Se JSONkod vid behov
mer_kod = raw_input("Se JSONkod? Y/N: ")
if mer_kod == "Y" or mer_kod == "y":
    print json_obj

