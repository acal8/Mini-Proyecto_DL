import cv2
import numpy as np
from skimage.transform import resize

def deteccion_edad(img, modelo):
    imagen = 255 - img

    contornos, _ = cv2.findContours(imagen[:,:,0], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cajas_delimitadoras = []
    for c in contornos:
        x, y, w, h = cv2.boundingRect(c)
        
        if w > 10 and h > 10: # Filtramos contornos pequeños, posiblemente ruido o manchas accidentales al dibujar
            cajas_delimitadoras.append((x, y, w, h))

    cajas_delimitadoras = sorted(cajas_delimitadoras, key = lambda v: v[0])

    edad_predicha = ''

    for (x, y, w, h) in cajas_delimitadoras:
            # Recortar el dígito de la imagen original
            recorte = imagen[:,:,0][y:y+h, x:x+w]

            lado_maximo = max(w, h)
            
            # Calculamos cuánto margen (padding) negro añadir a cada lado
            pad_y = (lado_maximo - h) // 2
            pad_x = (lado_maximo - w) // 2

            # Añadimos un margen extra fijo para que el número no toque los bordes (como en MNIST)
            margen_extra = int(lado_maximo * 0.3)

            recorte_cuadrado = cv2.copyMakeBorder(
                    recorte, 
                    pad_y + margen_extra, 
                    lado_maximo - h - pad_y + margen_extra, 
                    pad_x + margen_extra, 
                    lado_maximo - w - pad_x + margen_extra, 
                    cv2.BORDER_CONSTANT, 
                    value = 0 # Queremos que el borde sea negro
            )

            imagen_28 = resize(recorte_cuadrado, (28, 28))
            imagen_res = imagen_28/imagen_28.max() 
            edad = imagen_res.reshape(1, 28, 28, 1)

            pred = modelo.predict(edad, verbose=0)

            edad_predicha += str(np.argmax(pred))

    return edad_predicha