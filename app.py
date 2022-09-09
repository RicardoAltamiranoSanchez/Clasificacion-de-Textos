import nltk

nltk.download()
# LEER TEXTO DESDE URL

from bs4 import BeautifulSoup
import urllib.request  
response = urllib.request.urlopen('https://librefinanciero.com') #Obtiene el contenido HTML de la página web http://librefinanciero.com/
html = response.read()
soup = BeautifulSoup(html,"html5lib") # Limpia el texto HTML capturado
text = soup.get_text(strip=True)
print (text)