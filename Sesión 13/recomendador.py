#Importar la librería CSV para trabajar con archivos de este formato      
import csv

#Leer los datos del archivo CSV
with open('videos.csv', 'r') as file:
    reader = csv.DictReader(file)
    videos = list(reader)
    
# Encontrar el video con mayor calificación
mejor_video = max(videos, key=lambda x: float(x['Calificación']))

# Mostrar el video recomendado
print("🎥 Video Recomendado:")
print(f"Nombre: {mejor_video['Video']}")
print(f"Calificación: {mejor_video['Calificación']}")
