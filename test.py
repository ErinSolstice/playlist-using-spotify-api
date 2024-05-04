import yaml
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

"""
export SPOTIPY_CLIENT_ID='b0fddbbc3bf34e24bce34252d0b65833'
export SPOTIPY_CLIENT_SECRET='a7dcab26e8e445ca94baabcc989db2f2'
export SPOTIPY_REDIRECT_URI='http://localhost:9000'
"""

#auth_manager = SpotifyClientCredentials()
#sp = spotipy.Spotify(auth_manager=auth_manager)

def load_config():
    global user_config
    stream = open('config.yaml')
    user_config = yaml.safe_load(stream)
    pprint(user_config)

def get_top_songs_for_artist(artist, song_count=1):
    song_ids = []
    artist_results = sp.search(q='artist:' + artist, type='artist', limit=1)
    # pprint(artist_results)
    if artist_results['artists']['total']:
        artist_id = artist_results['artists']['items'][0]['id']
        # pprint(artist_id)
        artist_top_tracks = sp.artist_top_tracks(artist_id)
        artist_top_tracks_length = len(artist_top_tracks['tracks'])
        for x in range(0, artist_top_tracks_length if song_count > artist_top_tracks_length else song_count ):
            song_ids.append(artist_top_tracks['tracks'][x]['id'])
            # pprint(artist_top_tracks['tracks'][x])
        print(str(len(song_ids)) + ' songs found - ' + artist)
    else:
        print('Artist not found - ' + artist)
    # pprint(song_ids)
    return song_ids

global user_config
load_config()

scope = "user-library-read,playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#client_id=user_config['client_id'], client_secret=user_config['client_secret'], redirect_uri=user_config['redirect_uri'])

playlists = sp.user_playlists('spotify')
"""while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None"""

artists = [
    '2Cellos',
    'Acoustic Steel',
    'Act of Defiance',
    'Aephanemer',
    'Alestorm',
    'Xenoblight',
    'Zeal & Ardor'
]
all_track_ids = []

for i, current_artist in enumerate(artists):
    api_track_add_limit = 100
    top_song_limit_per_artist = 2
    top_artist_songs = get_top_songs_for_artist(current_artist, top_song_limit_per_artist)
    if len(top_artist_songs):
        all_track_ids.extend(top_artist_songs)
        if len(all_track_ids)+ top_song_limit_per_artist > api_track_add_limit or (i == len(artists)-1 and len(all_track_ids)):
            sp.playlist_add_tracks(user=user_config['username'], playlist_id=user_config['playlist_id'], tracks=all_track_ids)
            all_track_ids = []