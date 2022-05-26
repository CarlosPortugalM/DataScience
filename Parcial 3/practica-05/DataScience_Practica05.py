import api_key
import requests
import pandas as pd

client_access_token = api_key.my_api_key
# Búsqueda básica.

search_term = "Roger Waters" 
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"

print(genius_search_url)
response = requests.get(genius_search_url)
json_data = response.json()
json_data

json_data['response']['hits'][0]

# titulos de canciones

for song in json_data['response']['hits']:
    print(song['result']['full_title'])
    
# Obtener mosaicos de canciones

for song in json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])
    
# Trnasformar a los titulos de las canciones y los recuentos de páginas vistas en un datadraframe4

missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']['pageviews']])
 
#Make a Pandas dataframe from a list
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views']
print("\n")
print(missy_df)

#Transforme títulos de canciones, recuentos de páginas vistas y portadas de álbumes en un marco de datos

from IPython.core.display import HTML

def get_image_html(link):
    image_html = f"<img src='{link}' width='500px'>"
    return image_html
missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']['pageviews'], song['result']['song_art_image_url']])
 
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views','album_cover_url']
#Use the function get_image_html()
missy_df['album_cover'] = missy_df['album_cover_url'].apply(get_image_html)
print("\n")
print(missy_df)
#guardar gráfico de las páginas vistas de las canciones HTML

HTML(missy_df.to_html())






