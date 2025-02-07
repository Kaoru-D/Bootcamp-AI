#Enteros
farenheit = 10
celsius = -12
print(f"La temperatura es de {farenheit} grados Farenheit. Esto equivale aproximadamente a {celsius} grados Celsius")

#Flotantes
gravedadEarth = 9.8
gravedadMars = 3.7
planetaPesado = gravedadEarth + farenheit
planetaLiviano = gravedadMars * celsius
print(f"Ahora vamos a inventar un plantea, sumando la gravedad de la Tierra con la temperatura Farenheit obtenemos {planetaPesado} m/s^2")
print(f"Y Si multiplicamos la gravedad de la Tierra y la temperatura Celsius, obtenemos {planetaLiviano} m/s^2")

#Cadenas
cadenaSimple= "Hola, soy Daniel"
cadenaDoble= "y tengo 28 años"
mensaje = cadenaSimple + " " + cadenaDoble
print(mensaje)

#Ejercicios
#Mis profes del Bootcamp son Juan, Duvan y Jheyson
profesor1 = "Juan"
profesor2 = "Duvan"
profesor3 = "Jheyson"
print("Mis profesores en el Bootcamp son",end=" ")
print(profesor1, profesor2, profesor3, sep=", ")

