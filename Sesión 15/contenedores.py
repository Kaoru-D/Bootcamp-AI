#-------------------------------------Página 3-----------------------------------------------------------------#
# contenedores
# listas
# las listas van entre corchetes []
rudeus_Greyrat = ["Magia de Agua","Magia de Fuego","Magia de Curación","Magia de Tierra","Magia de Desplazamiento","Espadachín","Magia sin Cánticos"]
print(f"El protagonista de la serie Mushoku no Tensei es Rudeus Greyrat, y las habilidades que sabe son: {rudeus_Greyrat}")
""" print(rudeus_Greyrat[0]) """

#índices y acceso a elementos: Los elementos de una lista se enumeran desde 0 en adelante.
primera_Magia = rudeus_Greyrat[0]
print(f"La primera habilidad que Rudeus Greyrat aprendió fue la {primera_Magia}")
#Crea una variable llamada segunda habilitad y asignale el valor de la segunda habilidad de Rudeus Greyrat
segunda_Habilidad = rudeus_Greyrat[6]
print(f"Luego, aprendio la habilidad {segunda_Habilidad}, algo nunca visto en la serie")#Magia sin Cánticos, aunque está al final de la lista, es la segunda habilidad de Rudeus Greyrat

#-------------------------------------Página 4---------------------------------------------------------------------#
#Longitud de una lista: Puedes obtener la longitud de una lista con la función len().

#La loongitud es el número de elementos en la lista
longitud = len(rudeus_Greyrat)
print(f"La cantidad de habilidades que Rudeus conoce son: {longitud}")

#modificar elementos de una lista
#Para modificar un elemento de una lista, accede a él y asigna un nuevo valor.
rudeus_Greyrat[6] = "Magia de Barro"
print(f"La segunda habilidad de Rudeus Greyrat es: {rudeus_Greyrat[-1]}")

#-------------------------------------Página 5---------------------------------------------------------------------#
#Agregar elementos a una lista: Puedes agregar elementos a una lista con la función append().
#append() agrega un elemento al final de la lista.
rudeus_Greyrat.append("Magia de Hielo")
print(f"La habilidad que Rudeus no aprendió al graduarse es la  {rudeus_Greyrat[-1]}")

#Eliminar elementos de una lista: Puedes eliminar elementos de una lista con la función remove().
#remove() elimina el primer elemento con el valor especificado.
rudeus_Greyrat.remove("Magia de Hielo")
print(f"Las habilidades de Rudeus Greyrat son: {rudeus_Greyrat}")

#Extender una lista: Puedes agregar los elementos de una lista a otra lista con la función extend().
#extend() agrega los elementos de una lista al final de otra lista.
pocoUsado = ["Magia de Viento","Previsión","Comportamiento de etiqueta"] 
rudeus_Greyrat.extend(pocoUsado)
print(f"Las habilidades de Rudeus Greyrat son: {rudeus_Greyrat}")


#-------------------------------------Página 6---------------------------------------------------------------------#
#Rebanar una lista: Puedes obtener una parte de una lista con la función slice.
sylphiette=rudeus_Greyrat[0:3]
print(f"Las habilidades que Sylphiette aprendió de Rudeus son: {sylphiette}")
existe='Magia de Viento' in rudeus_Greyrat
print(existe)

