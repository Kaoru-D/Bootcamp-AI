#Primer ejemplo de variables en Python
mensaje = "Hola Mundo"
print(mensaje)

# Segundo ejemplo: variable de tipo string, más, concatenación de strings
nombre = "Daniel"
apellido = "Pulgarin"
print("Mi nombre es: " + nombre)

# Tercer ejemplo: variable de tipo entero, más, parsear entero a string y concatenación de strings
edad = 28
print("Mi edad es: " + str(edad))

# Cuarto ejemplo: uso de f-string
print(f"Mi nombre es: {nombre} y mi edad es: {edad}")

# Quinto ejemplo: uso de end (fin de línea)
ingredient1="arroz"
ingredient2="ensalada"
ingredient3="pollo"
ingredient4="aguacate"
ingredient5="tajadas"
print("Almuerzo del día:",end=" ")

#Sexto ejemplo: uso de sep (separador)
print(ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, sep=" - ")

#Séptimo ejemplo: declaración y asignación de variables
mensaje = "Daniel"#variable de tipo string
edad = 28 #variable de tipo entero
estatura = 1.66#variable de tipo flotante
es_estudiante = True #variable de tipo booleano
print(f"Nombre: {mensaje}, Edad: {edad}, Estatura: {estatura}, ¿Es estudiante?: {es_estudiante}")

# Octavo ejemplo: Asiganación de variables en la declaración

cuidad="Pereira"
poblacion=482483
print(f"Actualmente vivo en: {cuidad} y su población es de:{poblacion}")

#Reasignación de variables

ciudad="Saitama"
poblacion=1300000
print(f"Deseo ir a la prefectura de: {ciudad} y su población es de:{poblacion}", end=" ")
temperatura=32
print(f"y su temperatura actual es de {temperatura} grados")