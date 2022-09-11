# ! dividir el texto en tokens es decir,piezas mas pequeñas
# !(se puede tokenizar por palabras o por sentencias)
# !eso se de llamar tokenizar
# !ejemplo la casa de juan es blanca
# !la-casa-de-juan-es-blanca (6 tokens)
import nltk as nltk
#!Crear tokens por palabras
#!Función nltk.word_tokenize():
#!El método "nltk.word_tokenize()"
#!se utilizará para tokenizar oraciones y palabras con NLTK.
#!word_tokenize – Para tokenizar palabra
from nltk.tokenize import word_tokenize
    
#Visualizar Tokens
import matplotlib.pyplot as plt
#!Como se mencionó anteriormente, la biblioteca Python Seaborn 
#!se utiliza para facilitar la desafiante tarea de visualización de 
#!datos y se basa en.Seaborn permite 
#!la creación de gráficos estadísticos a través de las siguientes funcionalidades:
#!la libreria la usamos para mostrarlo en grafica o en una grafica
import seaborn as sns

def App():
   # ?LEER TEXTO DESDE URL
   # ?Beautiful Soup es una biblioteca de Python para analizar documentos
   # ?HTML (incluyendo los que tienen un marcado incorrecto).
   # ?Esta biblioteca crea un árbol con todos los elementos del documento y
   # ?puede ser utilizado para extraer información. 
   # ?Por lo tanto, esta biblioteca es útil para realizar web scraping 
    from bs4 import BeautifulSoup
    import urllib.request  
    # hacemos una peticion al url que indicamos con urllib.request
    response = urllib.request.urlopen('https://github.com/RicardoAltamiranoSanchez') #Obtiene el contenido HTML de la página web http://librefinanciero.com/
    print(response)
    #leemos la respuesta que nos dio el servidor o la pagina osea nos traer el html de la pagina
    html = response.read()
    #hacemos una limpieza del html de la pagina
    soup = BeautifulSoup(html,"html.parser") # Limpia el texto HTML capturado
    #extraemos solo el texto de soup
    text = soup.get_text(strip=True)
    print(text)
#*Creamos los tokens
#*indicamos que  con wordl que el objeto es español y de ponemos el texto que queremos tokenizar
    tokens = word_tokenize(text,"spanish")
    #removemos todos los signos de puntacion y que solamente se quede solo lo que son alfanumericos
    tokens=[word.lower() for word in tokens if word.isalpha()] # Remover los signos de puntuación
    print(tokens)
#*Verificar frecuencia de palabras con FreqDist de nltk
#*freq va ser un diccionario y va tener la clave y llave de cada palabra
#*y va indicar el numero de frecuencia que se repita la palabra
    freq = nltk.FreqDist(tokens)
    #solo iteramos el valor para poder visualizarlo
    #de llave y valor con un foreach
    for key,val in freq.items():
        print (str(key) + ':' + str(val))    
    
    #Visualizar Tokens
    #solo hacemos la visualizacion de forma de una grafica
    sns.set()
    #hacermos que las palabras de mayor frecuencia esten al inicio con plot
    freq.plot(30, cumulative=False)        
if __name__ == "__main__":
    try:
     App()
    except Exception as error:
     print("Cierre de la aplicion")
     print(f"Motivo de error {error}")
    