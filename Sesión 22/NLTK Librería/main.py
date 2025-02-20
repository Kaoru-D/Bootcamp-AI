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
texto="""El Ahorro Energético: Pequeños Gestos, Grandes Impactos
En un mundo donde el consumo de energía no deja de aumentar, adoptar hábitos de ahorro energético se ha convertido en una responsabilidad compartida.
No solo reduce el impacto ambiental, sino que también alivia la economía familiar y contribuye a un futuro más sostenible. 
Aquí te contamos cómo pequeños cambios pueden marcar la diferencia.
¿Por qué ahorrar energía?
La producción de energía, especialmente la proveniente de combustibles fósiles, es una de las principales fuentes de emisiones de CO₂, acelerando el cambio climático. Además, el derroche energético aumenta facturas y agota recursos no renovables. 
Ahorrar energía no es solo un acto ecológico, sino también una forma de cuidar nuestro bolsillo.
Acciones Cotidianas para Reducir el Consumo
Iluminación inteligente:
Sustituye bombillas tradicionales por LED, que consumen hasta un 80% menos y duran más.
Aprovecha la luz natural: abre cortinas y pinta paredes con colores claros para reflejar mejor la luz.
Electrodomésticos eficientes:
Elige modelos con etiqueta A+++, los más eficientes del mercado.
Desconecta dispositivos en modo standby (como televisores o cargadores), ya que siguen consumiendo energía.
Climatización responsable:
Regula el termostato: 20°C en invierno y 25°C en verano son temperaturas ideales.
Mejora el aislamiento de puertas y ventanas para evitar fugas de calor o frío.
Agua caliente con conciencia:
Duchas cortas en lugar de baños reducen el uso de agua y energía.
Instala reguladores de caudal en grifos y duchas.
Transporte sostenible:
Camina, usa bicicleta o transporte público para trayectos cortos.
Si conduces, mantén una velocidad constante y revisa la presión de los neumáticos para ahorrar combustible.
Inversiones a Largo Plazo
Paneles solares: Genera tu propia energía renovable y reduce tu dependencia de la red eléctrica.
Sistemas de domótica: Programar el apagado automático de luces o la gestión de la calefacción optimiza el consumo.
Rehabilitación energética: Mejorar el aislamiento de techos y paredes puede reducir hasta un 30% el gasto en climatización.
El Poder de la Conciencia Colectiva
El ahorro energético no es solo una tarea individual. Las empresas, gobiernos y comunidades deben promover políticas de eficiencia, como incentivos fiscales para renovaciones o la expansión de energías limpias. 
Cada acción suma: desde apagar una luz hasta participar en campañas de reforestación.
Conclusión
Ahorrar energía no requiere sacrificios extremos, sino adoptar un estilo de vida más consciente. Pequeños ajustes en nuestro día a día no solo benefician al planeta, sino que también nos enseñan a vivir con lo esencial. Como dijo el físico Albert Einstein: "El mundo no está amenazado por las malas personas, sino por aquellos que permiten la maldad". 
Hoy, elegir la eficiencia es un acto de responsabilidad hacia las generaciones futuras.
"""

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