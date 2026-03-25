async def crear_audiolibro(cuento):
    
    comunicador = edge_tts.Communicate(cuento, voz_elegida)
    await comunicador.save(archivo_salida)


# Usamos pygame para reproducir el audio
def reproducir_audio(archivo):
    pygame.mixer.init()

    pygame.mixer.music.load(archivo)
    
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

