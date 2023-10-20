import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os

# Configura tus credenciales aquí:
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost/'

scope = 'user-library-read playlist-read-private'

# Autenticación
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# Obtener todas las playlists del usuario
playlists = sp.current_user_playlists()['items']

for playlist in playlists:
    print(f"Explorando playlist '{playlist}' de  {len(playlists)} listas ... ")
    playlist_name = playlist['name']
    playlist_id = playlist['id']

    tracks = []
    offset = 0

    # Obtener las canciones de la playlist actual
    while True:
        results = sp.playlist_items(playlist_id, limit=50, offset=offset)
        if not results['items']:
            break

        for item in results['items']:
            track = item['track']
            tracks.append({
                'name': track['name'],
                'artist': track['artists'][0]['name'],  # toma solo el primer artista
                'album': track['album']['name'],
                'url': track['external_urls']['spotify']
            })

        offset += 50

    # Guardar en un archivo
    filename = f"{playlist_name}.json".replace("/", "_")  # Asegurarse de que el nombre es válido para un archivo
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tracks, f, ensure_ascii=False, indent=4)

    print(f"Backup de la playlist '{playlist_name}' completado! {len(tracks)} canciones guardadas en '{filename}'")