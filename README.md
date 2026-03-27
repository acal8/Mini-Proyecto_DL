# Mini-Proyecto_DL

### Adrián Carrasco Alcalá y Clara Montalvá Barcenilla

Mini proyecto de una start-up basada en IA para la asignatura de Deep Learning del Máster Universitario en Ciencia de Datos de la Universitat de València.

## Descripción

La idea de la Start-Up es la creación de una aplicación infantil de dibujo y generación de cuentos.

El usuario dibuja su edad y un animal en pantallas interactivas. Se genera la primera parte de un cuento infantil que tiene al animal como protagonista, teniendo en cuenta sus características en el dibujo y utilizando un vocabulario adaptado a la edad del lector. Se acompaña a la historia con la voz de un narrador y una ilustración de la misma.

La primera parte del cuento acaba con la aparición de un segundo animal misterioso, y una pregunta al lector sobre cuál es este nuevo personaje. El usuario dibuja este segundo protagonista en una nueva pantalla interactiva y se genera la segunda y parte final del cuento, con su narrador e ilustración correspondiente.

## Metodología

#### <u>Inputs proporcionados por el usuario</u>
- Dibujo con la edad del niño
- Dibujo del primer animal
- Dibujo del segundo animal

#### <u>Modelos</u>
- Red Neuronal Convolucional (CNN) entrenada con el conjunto MNIST: Identifica la edad dibujada.
- Qwen3-VL: Detecta el animal a partir del dibujo o garabato y genera una pequeña descripción del mismo.
- API Gemini: Genera las partes de la historia a partir de los animales y su descripción. Plantea una pregunta al final de la primera parte y presenta una moraleja al final de la segunda.
- Edge TTS: Genera la voz del narrador que lee la historia.
- Nano Banana 2: Crea las ilustraciones a partir de cada una de las partes de la historia.

#### <u>Outputs</u>
- Texto con la historia completa divida en partes, con la pregunta al final de la primera parte y la moraleja al final de la segunda.
- Audio con la voz del narrador contando la historia.
- Imágenes con las ilustraciones a partir del cuento.
