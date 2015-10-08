import spotipy

def spotip(input_search):
	sp = spotipy.Spotify()
	
	results = sp.search(q=input_search, limit=20)
	return results