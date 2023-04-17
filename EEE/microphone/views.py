from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
import os
import speech_recognition as sr
# from google.cloud import speech
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

# def microphone(request):
#     # set environment variable for authentication
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Key.json'

#     # create a recognizer instance
#     r = sr.Recognizer()

#     # use the default microphone as the audio source
#     with sr.Microphone() as source:
#         print("Speak now...")
#         # listen for audio and convert it to speech
#         audio = r.listen(source)

#     # create a Speech-to-Text client
#     client = speech.SpeechClient()

#     # convert the audio data to a RecognitionAudio object
#     audio_data = audio.get_wav_data(convert_rate=16000, convert_width=2)
#     audio = speech.RecognitionAudio(content=audio_data)

#     # set the configuration for the audio file
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code='en-US',
#         model='default',
#     )

#     # recognize speech from the audio file
#     response = client.recognize(config=config, audio=audio)
#     text = ''
#         # print the transcribed text
#     for result in response.results:
#        text = format(result.alternatives[0].transcript)
#     return render(request, 'users/home.html', text)
@csrf_exempt
def microphone(request):
    recog = sr.Recognizer()
    text = dict()

    with sr.Microphone() as source:
        audio = recog.listen(source)
        try:

            text['text']  = recog.recognize_google(audio)
            print(text)
        except:
            print('Internet connectivity issue')
    return render(request, 'users/home.html', text)
