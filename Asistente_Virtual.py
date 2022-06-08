import pyttsx3 as voz  
import speech_recognition as sr
import subprocess as sub   
from datetime import datetime

#Configuración de voz
voice = voz.init()

voices= voice.getProperty('voices')
voice.setProperty('voice', voices[0].id)
voice.setProperty('rate', 140)

def say(text):
    voice.say(text)
    voice.runAndWait()
    
    
while True:
    recognizer = sr.Recognizer()
    #para activar el microfono
    with sr.Microphone() as source:
        print('Escuchando...')
        audio=recognizer.listen(source, phrase_time_limit=5)


    try:
        comando=recognizer.recognize_google(audio, language='es-MX')
        print(f'Creo que dijiste "{comando}"')
        #comando=comando.lower()
        #comando=comando.split('')
        if 'yarbiss' in comando or 'Yarbiis' in comando or 'javis':

            if 'abre' in comando or 'abrir' in comando or 'Abre' in comando:

                sites={
                    'Google': 'https://www.google.com',
                    'google': 'https://www.google.com',
                    'youtube':'https://www.youtube.com',
                    'twitch':'https://www.twitch.tv',
                    'Twitch':'https://www.twitch.tv',
                    'WhatsApp': 'https://web.whatsapp.com'
                }
                for i in list(sites.keys()):
                    if i in comando:
                        sub.call(f'start Opera.exe {sites[i]}', shell=True)
                        say(f'Abriendo {i}')
            elif 'dame la hora' in comando or 'Dame la hora' in comando:
                time=datetime.now().strftime('%H:%M')
                say(f'Son las {time}')
            elif 'No entendí' in comando or 'No entendi' in comando or 'no entendi' in comando:
                say('Yo tampoco')
            elif 'Dime un chiste negro' in comando or 'dime un chiste negro' in comando:
                say('¿Que diferencia hay entre el amor y el sida? Que el sida es para toda la vida')
            elif 'Dime un chiste'in comando or 'dime un chiste' in comando:
                say('¿Cómo se dice disparo en árabe? Ahí-va-la-bala.')
            elif 'Chinga tu madre' in comando or 'chinga tu madre' in comando or 'chingatumadre' in comando:
                say('La tuya en vinagre')
            elif 'Como estas' in comando or 'como estas' in comando:
                say('Bien, gracias por preguntar, y tu?')
            elif 'Eres humano' in comando or 'eres humano' in comando:
                say('No, pero me gustaría llegar a tener sentimientos o reacciones humanas, son muy interesantes')
            elif 'quieres ser mi novia' in comando or 'Quieres ser mi novia' in comando:
                say('Apenas nos acabamos de conocer, y yo simplemente soy una asistente virtual, lo lamento')
        for i in['termina','terminar','término','salir','bye','adios','adiós','hablamos luego', 'Bye']:
            if i in comando:
                say('Sesión Finalizada, Que tenga un buen día')
                break
    except:
        say('No entendi lo que dijiste, ¿Puedes repetirlo porfavor?')
