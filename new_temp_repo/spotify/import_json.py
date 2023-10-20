import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os

# Configura tus credenciales aquí:
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost/'

scope = 'playlist-modify-public playlist-modify-private'

# Autenticación
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# Leer el archivo JSON
with open('nombre_de_tu_playlist.json', 'r', encoding='utf-8') as f:
    tracks = json.load(f)

# Extraer solo las URLs de las canciones
track_uris = [track['url'] for track in tracks]

# Crear una nueva playlist en la cuenta destino
user_id = sp.current_user()['id']
playlist_name = 'nombre_de_tu_playlist'  # puedes cambiar esto si lo prefieres
new_playlist = sp.user_playlist_create(user_id, playlist_name, public=True)

# Añadir las canciones a la nueva playlist
# Debido a las limitaciones de la API, solo podemos añadir 100 canciones a la vez.
for i in range(0, len(track_uris), 100):
    sp.playlist_add_items(new_playlist['id'], track_uris[i:i+100])

print(f"¡Playlist '{playlist_name}' creada y canciones importadas con éxito!")