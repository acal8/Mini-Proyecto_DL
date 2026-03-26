import edge_tts
import asyncio
import pygame

voz_elegida = "es-ES-AlvaroNeural" 

async def crear_audiolibro(cuento, archivo_salida = "cuento.mp3"):
    
    comunicador = edge_tts.Communicate(cuento, voz_elegida)
    await comunicador.save(archivo_salida)


# Usamos pygame para reproducir el audio
def reproducir_audio(archivo):
    pygame.mixer.init()

    pygame.mixer.music.load(archivo)
    
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.stop() 

    pygame.mixer.music.unload()

    pygame.mixer.quit()

