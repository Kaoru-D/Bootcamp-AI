import nltk#importamos la libreria nltk (natural language toolkit), que nos permite trabajar con lenguaje natural

#definir la ruta donde se almacenan los datos descargados de la libreria nltk
nltk.data.path.append('C:/Users/danys/AppData/Local/Programs/Python/Python312/Lib/site-packages/nltk')

#descargamos el modulo stopwords, que son las palabras mas comunes en un lenguaje
nltk.download('stopwords')

#importamos la función que divide el texto en palabras
from nltk.tokenize import word_tokenize

#descargamos el modulo stopwords, la lista de palabras en español
from nltk.corpus import stopwords

#Importamos la herramienta que calcula la frecuencia de las palabras
from nltk.probability import FreqDist

#definimos un texto en español al que queremos analizar
texto="""El perro corre rápido, pero no se mueve. Ibamos a la playa y el perro se quedó quieto; Decidimos llevarlo al veterinario. El veterinario nos dijo que el perro estaba enfermo, necesitaba una vacuna, el problema era el costo de la vacuna, preguntamos si había otra vacuna que no costara tanto o alguna manera de pagarlo a cuotas. El veterinario nos dijo que no habia otra vacuna que no costara tanto, pero, al ver la angustia en nuestros ojos, decidió darnos una facilidad de pago para pagar la vacuna. Después de que el veterinario le aplicara la vacuna el perro ya se encuentra mejor y puede seguir corriendo."""

#dividimos el texto en palabras
palabras=word_tokenize(texto,language="spanish")

#mostramos en pantalla el texto dividido en palabras
print(palabras)

#Obtenemos la lista de palabras vacias en español
#es decir, cargamos stopwords en español, aquí estan las palabras mas comunes en español que normalmente no necesitamos para analizar el texto
stopwordsSpanish = set(stopwords.words('spanish'))

#Filtramos las palabras: eliminamos las stopwords y los signos de puntuación
#Recorremos la lista de palabras, palabra por palabra. Si la palabra no está en la lista de stopwords y es una palabra real(sin numeros ni caracteres especiales), la guardamos en una nueva lista
palabrasFiltradas=[palabra for palabra in palabras if palabra.lower() not in stopwordsSpanish and palabra.isalpha()]

#mostramos en pantalla las palabras filtradas
#Nos deberá mostrar solo las palabras importantes
print(palabrasFiltradas)

#Calculamos la frecuencia de cada palabra en la lista filtrada
contemosPalabras=FreqDist(palabrasFiltradas)

#mostramos las 10 palabras mas comunes y la cantidad de veces que aparecen
print(contemosPalabras.most_common(10))