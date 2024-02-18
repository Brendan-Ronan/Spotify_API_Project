import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
client_id = '***'
client_secret = '***'

# Set up Spotipy with client credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# User input
artist_name = input("Enter artist name: ")

# Search for the artist
results = sp.search(q=artist_name, type='artist', limit=1)

# Check results
if results['artists']['items']:
    # Extract info
    artist_info = results['artists']['items'][0]
    artist_id = artist_info['id']

    # Retrieve top tracks
    top_tracks = sp.artist_top_tracks(artist_id)

    # Display top tracks information
    print(f"Top Tracks for {artist_info['name']}:")
    for idx, track in enumerate(top_tracks['tracks']):
        print(f"{idx + 1}. {track['name']}")

else:
    print(f"No information found for the artist '{artist_name} on Spotify.")


