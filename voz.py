import speech_recognition as sr
import subprocess

def abrir_operagx():
    # Configurar reconhecimento de voz
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga, qual é o comando?")
        audio = r.listen(source)

    try:
        # Reconhecer comando de voz
        comando = r.recognize_google(audio, language='pt-BR')
        if comando == "abrir Opera GX":
            # Executar o aplicativo
            subprocess.Popen(r"C:\Users\mathe\AppData\Local\Programs\Opera GX\launcher.exe")
            print("Opera GX foi aberto!")
        elif comando =="música":
            subprocess.Popen(r"C:\Users\mathe\AppData\Local\Programs\Opera GX\launcher.exe")
            print('divirta-se!')
        else:
            print("Comando não reconhecido.")
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o comando de voz.")
    except sr.RequestError as e:
        print("Erro ao obter resultados do serviço de reconhecimento de voz; {0}".format(e))

if __name__ == '__main__':
    abrir_operagx()
