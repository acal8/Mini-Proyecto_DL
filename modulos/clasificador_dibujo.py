import torch
import numpy as np
from PIL import Image
from transformers import AutoModelForImageClassification, AutoImageProcessor

modelo_hf = "kmewhort/beit-sketch-classifier"
procesador = AutoImageProcessor.from_pretrained(modelo_hf)
modelo = AutoModelForImageClassification.from_pretrained(modelo_hf)

def clasificar_dibujo(matriz_imagen):
    # Transformamos la matriz del dibujo a una imagen PIL
    imagen = Image.fromarray(matriz_imagen.astype('uint8')).convert("RGB")
    
    # Preprocesamos la imagen
    entrada = procesador(images=imagen, return_tensors="pt")

    # Predecimos con el modelo
    with torch.no_grad():
        salida = modelo(**entrada)
        preds = salida.logits

    # Nos quedamos con el índice con la probabilidad más alta
    categoria_predicha = np.argmax(preds).item()
    
    # Dado el identificador de la categoria predicha, buscamos la etiqueta correspondiente
    animal_predicho = modelo.config.id2label[categoria_predicha]
    
    return animal_predicho

