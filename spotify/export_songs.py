import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os

# Configura tus credenciales aquí:
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost/'

scope = 'user-library-read'

# Autenticación
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# Obtener canciones guardadas
offset = 0
songs = []
while True:
    results = sp.current_user_saved_tracks(limit=50, offset=offset)
    if not results['items']:
        break

    for item in results['items']:
        track = item['track']
        songs.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],  # toma solo el primer artista
            'album': track['album']['name'],
            'url': track['external_urls']['spotify']
        })

    offset += 50

# Guardar en un archivo
with open('spotify_backup.json', 'w', encoding='utf-8') as f:
    json.dump(songs, f, ensure_ascii=False, indent=4)

print(f"Backup completado! {len(songs)} canciones guardadas en 'spotify_backup.json'")
