import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

scope = "user-library-read,playlist-modify-public"
client_id = "b0fddbbc3bf34e24bce34252d0b65833"
client_secret = "a7dcab26e8e445ca94baabcc989db2f2"
redirect_uri="http://localhost:9000"

username = "riverrats1120"
playlist_id = "4E4NJlRciqeAjdyvk0A3b3"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:9000", scope=scope))

def get_artist_ids(artist, song_count=1):
    artists = [
        "The Maine",
        "The Teskey Brothers",
        "Jon Batiste",
        "Cage the Elephant",
        "Red Hot Chili Peppers",
    ]

    for idx, artist in enumerate(artists):
        artist_results = sp.search(q='artist:' + artist, type='artist', limit=1)
        print("'" + artist_results['artists']['items'][0]['id'] + "', # " + artist_results['artists']['items'][0]['name'])

artists_what_stage = [
    '4o0pNHbyj36LPvukNqEug0', # The Maine
    '2nTjd2lNo1GVEfXM3bCnsh', # The Teskey Brothers
    '0eRbECAGCLLiTyVXPBRexU', # Jon Batiste
    '26T3LtbuGT1Fu9m0eRq5X3', # Cage the Elephant
    '0L8ExT028jH3ddEcZwqJJ5' # Red Hot Chili Peppers
]

artists_which_stage = [
    '60NNvDqsif0u40CXMV6jDQ', # Ryan Beatty
    '5y8tKLUfMvliMe8IKamR32', # d4vd
    '4XquDVA8pkg5Lx91No1JxB', # Brittany Howard
    '2hUYKu1x0UZQXvzCmggvSn', # Reneé Rapp
    '1QAJqy2dA3ihHBFIHRphZj', # Cigarettes After Sex
    '63yrD80RY3RNEM2YDpUpO8', # Melanie Martinez
]

artists_the_other_stage = [
    '4fIPBdK4awAR1W14u3v1J5', # LOVRA
    '2rdSCmWgrIWA8pmwhS1T2k', # Vandelux
    '587PA35pRGL1JwQr6idJbb', # NEIL FRANCES
    '297Z0teiCkp5s9eneWROpI', # Kasablanca
    '6ziQKWMuCe0unfDXoqyVdt', # Whyte Fang
    '6mmSS7itNWKbapgG2eZbIg', # Knock2
    '5fMUXHkw8R8eOP2RNVYEZX', # Diplo
    '4iVhFmG8YCCEHANGeUUS9q', # Pretty Lights
]

artists_this_tent = [
    '26DvqLYszG0oIOeelTF5kE', # Trousdale
    '3FMcVBx2TMq2f5gEPcUieC', # Josiah and the Bonnevilles
    '3K2Srho6NCF3o9MswGR76H', # Bakar
    '3Isy6kedDrgPYoTS1dazA9', # Sean Paul
    '4ERtgeBbWRkFzIz6LaFCeY', # Dashboard Confessional - on schedule as Dashboard Confessional Emo Superjam,
    '3oKRxpszQKUjjaHz388fVA', # Parcels
]

artists_that_tent = [
    '3ceQN2NVlLg1hgTzljDE4n', # Half Moon Run
    '1ZGVS1OWpdvELiQyx3vkO7', # Tanner Usrey
    '0avMDS4HyoCEP6RqZJWpY2', # Ethel Cain
    '0fGcIStdT1OpFFhOC7Wp36', # Teezo Touchdown
    '5sXaGoRLSpd7VeyZrLkKwt', # Gregory Alan Isakov
    '3qMPgMBrbaUZH9EdVV0fXM', # Garden Therapy
    '75mafsNqNE1WSEVxIKuY5C', # IDLES
]

artists_all_stages = artists_what_stage + artists_which_stage + artists_the_other_stage + artists_this_tent + artists_that_tent
playlist_size = 0
artists_all_stages = ['4o0pNHbyj36LPvukNqEug0'] # The Maine
for idx, artist in enumerate(artists_all_stages):
    offset = 0
    artist_albums = []
    for idx in range(20):
        results = sp.artist_albums(artist_id=artist, album_type='album', limit=20, offset=offset)
        if len(results['items']) == 20:
            artist_albums = artist_albums + results['items']
            offset = offset + 20
        else:
            artist_albums = artist_albums + results['items']
            break

    offset = 0
    for idx in range(20):
        results = sp.artist_albums(artist_id=artist, album_type='single', limit=20, offset=offset)
        if len(results['items']) == 20:
            artist_albums = artist_albums + results['items']
            offset = offset + 20
        else:
            artist_albums = artist_albums + results['items']
            break

    for idx, album in enumerate(artist_albums):
        album_tracks = sp.album_tracks(album['id'])
        all_track_ids = []
        for idx, track in enumerate(album_tracks['items']):
            pprint('    ' + track['name'] + ' - '+ track['id'])
            all_track_ids.append(track['id'])
        playlist_size = playlist_size + len(all_track_ids)
        pprint(album['name'] + ' - '+ album['id'] + ' - ' + str(playlist_size))
        #sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=all_track_ids)

"""
def get_top_songs_for_artist(artist, song_count=1):
    song_ids = []
    artist_results = sp.search(q='artist:' + artist, type='artist', limit=1)
    pprint(artist_results)
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
            sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=all_track_ids)
            all_track_ids = []
"""