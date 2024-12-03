from django.shortcuts import render
import requests

# Función para obtener los detalles del anime desde la API
def get_anime_data(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        anime_data = response.json().get('data', {})
    else:
        anime_data = {}
    
    return anime_data

def index(request):
    airing_anime = []  # Lista para almacenar los animes en emisión
    popularity_anime = []  # Lista para almacenar los animes populares

    # URLs para obtener los animes desde la API de Jikan
    url_airing = "https://api.jikan.moe/v4/top/anime?filter=airing"
    url_popularity = "https://api.jikan.moe/v4/top/anime"

    # Solicitudes a la API
    response_airing = requests.get(url_airing)
    response_popularity = requests.get(url_popularity)

    # Procesamos los animes en emisión
    if response_airing.status_code == 200:
        data = response_airing.json()
        anime_list = data.get('data', [])
        for anime in anime_list[:9]:
            youtube_id = anime.get('trailer', {}).get('youtube_id', '')
            banner_url = f"https://img.youtube.com/vi/{youtube_id}/maxresdefault.jpg" if youtube_id else ""
            truncated_desc = truncate_description(anime.get('synopsis'))
            airing_anime.append({
                'id': anime.get('mal_id'),
                'title': anime.get('title', 'No Title'),
                'image_url': anime.get('images', {}).get('jpg', {}).get('image_url', ''),
                'genres': [genre['name'] for genre in anime.get('genres', [])],
                'banner_url': banner_url or anime.get('images', {}).get('jpg', {}).get('image_url', ''),
                'desc': truncated_desc,
                "score": anime.get('score'),
                "rank": anime.get('rank'),
            })

    # Procesamos los animes populares
    if response_popularity.status_code == 200:
        data = response_popularity.json()
        anime_list = data.get('data', [])
        for anime in anime_list[:9]:
            youtube_id = anime.get('trailer', {}).get('youtube_id', '')
            banner_url = f"https://img.youtube.com/vi/{youtube_id}/maxresdefault.jpg" if youtube_id else ""
            popularity_anime.append({
                'id': anime.get('mal_id'),
                'title': anime.get('title', 'No Title'),
                'image_url': anime.get('images', {}).get('jpg', {}).get('image_url', ''),
                'banner_url': banner_url or anime.get('images', {}).get('jpg', {}).get('image_url', ''),
                "score": anime.get('score'),
                "rank": anime.get('rank'),
            })

    return render(request, 'core/index.html', {
        'airing_anime': airing_anime,
        'popularity_anime': popularity_anime,
    })

def truncate_description(description, word_limit=10):
    words = description.split()[:word_limit]  # Dividir en palabras y tomar las primeras `word_limit`
    return " ".join(words) + "..." if len(words) == word_limit else description

def anime_details(request, anime_id, anime_name):
    anime_data = get_anime_data(anime_id) 
    return render(request, 'core/anime-details.html', {'anime': anime_data})

def anime_trailer(request, anime_id):
    anime_data = get_anime_data(anime_id) 
    return render(request, 'core/anime-trailer.html', {'anime': anime_data})

def anime_search(request):
    query = request.GET.get('q', '')  # Obtener la consulta desde los parámetros GET
    anime_results = []  # Lista para almacenar los resultados procesados

    if query:
        url = f"https://api.jikan.moe/v4/anime?q={query}"
        response = requests.get(url)

        if response.status_code == 200: 
            data = response.json()  
            anime_list = data.get('data', [])  # Obtener los datos de la API

            # Procesar los resultados de la API
            for anime in anime_list:
                youtube_id = anime.get('trailer', {}).get('youtube_id', '')
                banner_url = f"https://img.youtube.com/vi/{youtube_id}/maxresdefault.jpg" if youtube_id else anime.get('images', {}).get('jpg', {}).get('image_url', '')

                anime_results.append({
                    'id': anime.get('mal_id'),
                    'title': anime.get('title', 'No Title'),
                    'image_url': anime.get('images', {}).get('jpg', {}).get('image_url', ''),
                    'banner_url': banner_url,
                    'score': anime.get('score'),
                    'synopsis': anime.get('synopsis', 'No synopsis available.'),
                })

    return render(request, 'core/anime_search.html', {'anime_results': anime_results, 'query': query})

def signup(request):
    return render(request, 'core/auth/signup.html')

def login(request):
    return render(request, 'core/auth/login.html')