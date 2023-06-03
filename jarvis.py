import speech_recognition as sr

def ouvir_microfone():
    # Crie um objeto reconhecedor
    r = sr.Recognizer()

    # Use o microfone como fonte de áudio
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)

    try:
        # Use o reconhecedor para converter o áudio em texto
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")
    except sr.RequestError as e:
        print("Erro na solicitação ao serviço de reconhecimento de voz; {0}".format(e))

# Chame a função para iniciar o reconhecimento de voz
ouvir_microfone()
