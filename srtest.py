from urllib2 import urlopen
from json import load

def test_sr():
	'''testar sr:s api'''
	url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164&format=json"
	response = urlopen(url)
	json_obj = load(response)
	print json_obj
	for t in json_obj['playlist']['song']['description']:
		t[0]


test_sr()