import requests
from bs4 import BeautifulSoup
import re
from bs4 import Comment

# Definir la URL de la página a rastrear
url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extraer los enlaces
links = [a["href"] for a in soup.find_all("a", href=True)]
print("Enlaces encontrados:")
print(links)

# Extraer comentarios HTML
comentarios = soup.find_all(string=lambda text: isinstance(text, Comment))
print("\nComentarios encontrados:")
for comentario in comentarios:
    print(comentario)

# Extraer direcciones de correo electrónico usando expresiones regulares
correo_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
correos = re.findall(correo_pattern, soup.text)
print("\nCorreos electrónicos encontrados:")
for correo in correos:
    print(correo)
