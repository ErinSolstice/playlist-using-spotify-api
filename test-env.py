import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
client_id = "b0fddbbc3bf34e24bce34252d0b65833"
client_secret = "a7dcab26e8e445ca94baabcc989db2f2"
redirect_uri="http://localhost:9000"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:9000", scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])