import s as sr

# Importar lib correta para execução da fala

r = sr.Recognizer()
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    while True:
        audio = r.listen(s)

        speech = r.recongnize_google(audio, language='pt')

        print('Você disse: ', speech)