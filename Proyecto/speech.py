import speech_recognition as sr


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Por favor, digame su pregunta")

        audio = r.listen(source)

        print("Reconociendo.... ")

        # recognize speech using google

        try:
            value = str(r.recognize_google(audio, language = 'es-ES'))
            print("Usted dijo? \n" + value)
            return  value

        except Exception as e:
            print("Error :  " + str(e))

        # write audio

        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()
