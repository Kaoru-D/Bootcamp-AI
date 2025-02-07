#Ejercicios
#1.Operaciones con Cadenas:
#-Crea dos variables de cadena llamadas
#cadena1 y cadena2.
cadena1 = "Estoy aprendiendo a programar"
cadena2 = "en el curso de Inteligencia Artificial"
#-Concatena las dos cadenas y guarda el
#resultado en una nueva variable.
cadenaCompleta = cadena1 + " " + cadena2
#-Imprime la longitud de la nueva cadena.
"""print(cadenaCompleta)
print(len(cadenaCompleta))
print(cadena1.__len__())
print(cadena2.__len__())"""

#Reto: Imprimir la longitud de la cadena Talento_Tech es MINTIC
cadena1="Talento_Tech"
cadena2=" es MINTIC"
cadenaCompleta = cadena1 + " " + cadena2
"""print(cadenaCompleta.__len__())
print(len(cadena1))
print(len(cadena2))"""

#Crea una varible con tu nombre
nombre = "Lupe"
#Utiliza el formato de cadena para imprimir un mensaje de bienvenida
#personalizado
#print(f"Hola a todos le presento a mi mascota se llama {nombre}")

#2.Subcadenas y Métodos:
#-Crea una cadena larga y utiliza el método split()
#para dividirla en una lista de palabras.
muchoTexto="Para la creación de un modelo de Machine Learning, es necesario tener un buen conjunto de datos, un algoritmo de aprendizaje y un modelo de evaluación"
textoDivididoXPalabras = muchoTexto.split()
textoDivididoXcomas= muchoTexto.split(",")
#-Encuentra e imprime la posición de una
#subcadena específica.
""" print(textoDivididoXPalabras[8])
print(textoDivididoXcomas[1])
print("Número de palabras: ",len(textoDivididoXPalabras.split()))
print("Número de caracteres: ",len(textoDivididoXPalabras)) """

#Métodos de Mayúsculas y Minúsculas:
#Crea una cadena en minúsculas y conviértela a
#mayúsculas usando los métodos upper() y
#lower().
texto="hola, soy Lupe"
textoMinusculas = texto.lower()
textoMayusculas = texto.upper()
""" print(textoMinusculas)
print(textoMayusculas) """

#Operaciones Aritméticas:
#-Crea dos variables, a y b, con valores numéricos.
a=5
b=3
#-Realiza operaciones aritméticas básicas (suma, resta, multiplicación, división,
#exponente) con estas variables e imprime los resultados.
print(f"{a} + {b} = {a+b}") #print(a+b)
print(f"{a} - {b} = {a-b}") #print(a-b)
print(f"{a} * {b} = {a*b}") #print(a*b)
print(f"{a} / {b} = {a/b}") #print(a/b)
print(f"{a} ** {b} = {a**b}") #print(a^b)


#División y Módulo:
#-Divide dos números enteros y guarda el resultado en una variable llamada resultado.
#-Utiliza el operador módulo (%) para obtener el residuo de la división e imprímelo.
division=8/3
residuo=8%3
print(f"La división de 8 entre 3 es {division} y el residuo es {residuo}")




#Presición de Flotantes:
#-Crea una variable c con un valor flotante.
c=3.14
#-Realiza operaciones aritméticas que involucren flotantes y enteros.
print(c*parseInt(c))
#-¿Cómo se manejan las operaciones mixtas
