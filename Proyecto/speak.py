from gtts import gTTS
from playsound import playsound 

def reproducirTexto(texto):
    #Nombro la pista de audio que voy a generar
    nombrePista = 'sonido.mp3'
    #Le envio el texto a la libreria, junto con el lenguaje con el que me respondera
    tts = gTTS(texto, lang= 'es-us')
    #abro la pista y la nombre archivo 
    with open(nombrePista, 'wb') as archivo:
        #Escribo el valor que tendra la pista 
        tts.write_to_fp(archivo)
    #reproduzco la pista de audio
    playsound(nombrePista)