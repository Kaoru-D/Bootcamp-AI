import nltk #importamos la libreria nltk

#desde nltk importamos el modulo stopwords, que son las palabras mas comunes en un lenguaje
from nltk.corpus import stopwords

#Descargamos la lista de palabras vacias(stopwords) si no esta descargada
nltk.download('stopwords')

#Guardamos la lista en español en una variable
stopWordsSpanish = stopwords.words('spanish')

#mostramos en pantalla la lista de palabras en español
print(stopWordsSpanish)