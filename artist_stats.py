import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '2daa30aa21c04a1fa7fa4424491de852'
client_secret = 'b578dff804a64790a84cc4a299196a7a'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = input("Enter an artist: ")
results = sp.search(q=artist_name, type='artist')

# check results
if results['artists']['items']:
    # extract relevant information
    artist_info = results['artists']['items'][0]

    print(f"Artist Name: {artist_info['name']}")
    print(f"Followers: {artist_info['followers']['total']}")
    print(f"Genres: {', '.join(artist_info['genres'])}")
    print(f"Popularity: {artist_info['popularity']}")
    print(f"External URL: {artist_info['external_urls']['spotify']}")

else:
    print(f"No information found for the artist '{artist_name} on Spotify")

