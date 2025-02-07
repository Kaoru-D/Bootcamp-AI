#Importar la librería pandas
#esta librería es muy útil para el manejo de datos
import pandas as pd

#Cargar un archivo csv, se debe tener en cuenta la ruta y el nombre del archivo
#El archivo csv que se va a cargar es un archivo que contiene información de ventas
path='Online_Retail.csv'

#Leer el archivo csv y asignarlo a una variable
#se debe tener en cuenta el encoding, en este caso se utiliza latin1, que permite leer caracteres especiales
retail_data=pd.read_csv(path, encoding='latin1')

print(type(retail_data))

print(retail_data)
