#-----------------------------Página 7----------------------------------
# Tuplas
#Las tuplas son secuencias inmutables, lo que significa que no se pueden cambiar después de que se crean.
#Las tuplas se crean utilizando paréntesis, en lugar de corchetes.
#Puedes crear una tupla con la palabra reservada tupla o tuple.

herramientas_kratos = ('Espadas del Caos', 'Hacha Leviatán ', 'Espadas del Exilio',"Lanza de Esparta","Guantelete de Zeus","Arco de Apolo")

# Índices y acceso a elementos
# Los elementos de una tupla también se enumeran desde 0 en adelante.
# Puedes acceder a los elementos de una tupla utilizando sus índices.

armaPrincipal = herramientas_kratos[0]
""" print(armaPrincipal) """
armaSecundaria = herramientas_kratos[1]
""" print(armaSecundaria) """

#---------------------------------Página 8----------------------------------
# Longitud de una tupla
# Puedes obtener la longitud de una tupla utilizando la palabra reservada len.
#La longitud de una tupla es la cantidad de elementos que contiene.
inventario=len(herramientas_kratos)
""" print(f"El inventario de Kratos tiene {inventario} armas") """

#Inmutabilidad
#Las tuplas son inmutables, lo que significa que no se pueden cambiar después de que se crean.
#Si intentas cambiar un elemento de una tupla, obtendrás un error.
""" print(herramientas_kratos)
herramientas_kratos[0] = "Espada de Zeus"
print(herramientas_kratos) """

#Empaquetado y desempaquetado de tuplas
#Puedes empaquetar varios valores en una tupla y luego desempaquetarlos en variables separadas.
#print(herramientas_kratos)
#asignación de valores a variables
""" espada, hacha, espada2, lanza, guantelete, arco = herramientas_kratos
print(espada , hacha, espada2, lanza, guantelete, arco) """

""" PD: El número de variables debe coincidir con el número de elementos en la tupla.
Si el número de variables es menor que el número de elementos, obtendrás un error """
#Solución
#Si desconoces el número de elementos en una tupla, puedes usar un asterisco * para recopilar los elementos restantes en una lista.
armaPrincipal, *otrasArmas = herramientas_kratos
""" print(herramientas_kratos, otrasArmas, sep='\n') """

#---------------------------------Página 9----------------------------------
#Tupla anidada
#Puedes anidar tuplas dentro de otras tuplas.
poderes_kratos = ("Ira del espartano","Regeneración de vida")
habilidades_kratos=(herramientas_kratos,("Fuerza","Agilidad","Resistencia","Inteligencia"),poderes_kratos)
print(habilidades_kratos) 
