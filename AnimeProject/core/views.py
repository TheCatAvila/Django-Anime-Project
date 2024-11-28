from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def signup(request):
    return render(request, 'core/auth/signup.html')

def login(request):
    return render(request, 'core/auth/login.html')

def anime_search(request):
    query = request.GET.get('q', '')  # Obtener la consulta de búsqueda desde el parámetro de la URL
    anime_results = []  # Inicializamos una lista vacía para los resultados de la búsqueda
    
    if query:  # Solo realizamos la búsqueda si hay una consulta
        url = f"https://api.jikan.moe/v4/anime?q={query}"  # URL de la API con la consulta
        response = requests.get(url)  # Hacer la solicitud GET a la API
        
        if response.status_code == 200:  # Si la respuesta es exitosa
            data = response.json()  # Convertir la respuesta a formato JSON
            anime_results = data.get('data', [])  # Obtener los resultados desde la clave 'data'
    
    # Pasamos los resultados a la plantilla para que se muestren en la página
    return render(request, 'core/anime_search.html', {'anime_results': anime_results, 'query': query})