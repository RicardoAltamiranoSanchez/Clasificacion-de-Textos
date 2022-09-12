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

#! El paquete stop-words se utiliza para eliminar 
#! palabras vacías del texto en Python. Este paquete contiene 
#! palabras vacías de muchos idiomas como inglés, danés, francés, español y más.
from nltk.corpus import stopwords

#!obtenemos sinonimos con la libreria wordnet
#!WordNet es un diccionario de inglés, similar a un tesauro 
#!tradicional que NLTK incluye en inglés WordNet. Podemos 
#!usarlo como referencia para obtener el significado de las palabras, 
#!ejemplo de uso y definición. Una colección de palabras similares se llama lemas. 
#!Las palabras en WordNet están organizadas y los nodos y los bordes donde los nodos 
#!representan el texto de la palabra y los bordes representan las relaciones entre 
#!las palabras. A continuación veremos cómo podemos utilizar el módulo WordNet.
from nltk.corpus import wordnet
 

def App():
   # ?LEER TEXTO DESDE URL
   # ?Beautiful Soup es una biblioteca de Python para analizar documentos
   # ?HTML (incluyendo los que tienen un marcado incorrecto).
   # ?Esta biblioteca crea un árbol con todos los elementos del documento y
   # ?puede ser utilizado para extraer información. 
   # ?Por lo tanto, esta biblioteca es útil para realizar web scraping 
    from bs4 import BeautifulSoup
    import urllib.request  
    #*hacemos una peticion al url que indicamos con urllib.request
    response = urllib.request.urlopen('https://es.wikipedia.org/wiki/Wikipedia:Portada') #Obtiene el contenido HTML de la página web http://librefinanciero.com/
    print(response)
    #*leemos la respuesta que nos dio el servidor o la pagina osea nos traer el html de la pagina
    html = response.read()
    #*hacemos una limpieza del html de la pagina
    soup = BeautifulSoup(html,"html.parser") # Limpia el texto HTML capturado
    #*extraemos solo el texto de soup
    text = soup.get_text(strip=True)
    print(text)
#*Creamos los tokens
#*indicamos que  con wordl que el objeto es español y de ponemos el texto que queremos tokenizar
    tokens = word_tokenize(text,"spanish")
    #*removemos todos los signos de puntacion y que solamente se quede solo lo que son alfanumericos
    tokens=[word.lower() for word in tokens if word.isalpha()] # Remover los signos de puntuación
    print(tokens)
#*Verificar frecuencia de palabras con FreqDist de nltk
#*freq va ser un diccionario y va tener la clave y llave de cada palabra
#*y va indicar el numero de frecuencia que se repita la palabra
    freq = nltk.FreqDist(tokens)
    #*solo iteramos el valor para poder visualizarlo
    #*de llave y valor con un foreach
    for key,val in freq.items():
        print (str(key) + ':' + str(val))    
    
    #*Visualizar Tokens
    #*solo hacemos la visualizacion de forma de una grafica
    sns.set()
    #*hacermos que las palabras de mayor frecuencia esten al inicio con plot
    freq.plot(30, cumulative=False)        
#*Hacemos limpieza de palabras
#*hacemos una copida de los tokens para elimnar las palabras vacias    
    clean_tokens = tokens[:]
    #*iteramos el token  o los valores que ya obtuvimos anterior mente
    for token in tokens:
        #*verficamos si esta en el listado de words en español de la palabras separada
        if token in stopwords.words('spanish'):
            #*si esta lo revomvemos el nuevo arreglo para que no se repita la palabra     
            clean_tokens.remove(token)
    print(clean_tokens)
    #*Verificar frecuencia de palabras 
    #*volvemos a vericar pero ya con el nuevo arreglo sin las palabras de espacio con la de etc
    freq_clean = nltk.FreqDist(clean_tokens)
    for key,val in freq_clean.items():
        print (str(key) + ':' + str(val))
    #*Visualizar Tokens
    sns.set()
    freq_clean.plot(30, cumulative=False)    
    
#*Obtenemos los sinonimos para agrupar los grupos y antonimos igual para agruapar wornet solo opera con el lenguaje ingles    
    #*creamos una lista de sinonimos  vacio
    sinonimos = []
#*iteramo con wornet para que nos de todos los sinonimos con el resultado de investement
    for syn in wordnet.synsets('investment'):#investmente es inversion
#*hacemos que nos de todos los lemas que tenga de sinonimo esa palabra    
        for lemma in syn.lemmas():
#*y lo guardamos en el arreglo que de pusimos sinonimos     
            sinonimos.append(lemma.name())
#*imprimos los sinonimos de wornet     
    print(sinonimos)
    #*Reemplazar tokens sinónimos
    for ind,sin in enumerate(sinonimos):
     clean_tokens_sin = [word.replace(sinonimos[ind],'investment') for word in clean_tokens]


if __name__ == "__main__":
    try:
     App()
    except Exception as error:
     print("Cierre de la aplicion")
     print(f"Motivo de error {error}")
    