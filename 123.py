import speech_recognition as sr

r = sr.Recognizer()
while True:
    with sr.Microphone(device_index=0) as source:
        print('Скажи что-нибудь…')
        audio = r.listen(source)
    speech = r.recognize_google(audio, language='ru_RU'). lower()
    print('Вы сказали:', speech)
    if speech == 'привет':
        print('Привет')