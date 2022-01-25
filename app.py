from flask import Flask, render_template, request,redirect,jsonify, make_response
from datetime import datetime
from werkzeug.utils import secure_filename
import os
from ibm_watson import SpeechToTextV1, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import unittest
from time import sleep
result = "this is result"
app=Flask(__name__)
app.config["AUDIO_UPLOADS"] = "uploads"
app.config["ALLOWED_AUDIO_EXTENSIONS"] = ["MP3","mp3"]



ltapikey= '_RARCESdZRuZdmFhAoAdY93bofmohDO4mrZ9OzY-qAiB'
lturl='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c0d9a93c-454b-4181-819b-5ed96dc30c52'
sttapikey='V_a4rIwPDrdbZQjeH0HNvpAPJRObhfneRmxlQ5AQ1bEW'
stturl='https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/4b085963-f968-4043-8454-0695a813d6af'
ltauthenticator = IAMAuthenticator(ltapikey)
lt= LanguageTranslatorV3(version='2018-05-01', authenticator=ltauthenticator)
lt.set_service_url(lturl)
sttauthenticator = IAMAuthenticator(sttapikey)
stt = SpeechToTextV1(authenticator=sttauthenticator)
stt.set_service_url(stturl)



def english_to_french(input1):
    translation = lt.translate(text=input1, model_id='en-fr-CA').get_result()
    translatedtext = translation['translations'][0]['translation']
    return translatedtext
def french_to_english(input1):
    translation = lt.translate(text=input1, model_id='fr-CA-en').get_result()
    translatedtext = translation['translations'][0]['translation']
    return translatedtext

def allowed_audio(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_AUDIO_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/', methods=["GET", "POST"])
def upload_audio():
    result="this is result"
    original=''
    if request.method == "POST":

        if request.files:

            audio = request.files["audio"]

            if audio.filename == "":
                print("No filename")
                return redirect(request.url)


            if allowed_audio(audio.filename):
                filename = secure_filename(audio.filename)
                audio.save(os.path.join(app.config["AUDIO_UPLOADS"], filename))

                with open("uploads/"+filename, 'rb') as f:
                    res_en = stt.recognize(audio=f, content_type='audio/mp3',
                    model='en-US_BroadbandModel').get_result()
                with open("uploads/" + filename, 'rb') as f:
                    res_fr = stt.recognize(audio=f, content_type='audio/mp3',
                    model='fr-CA_BroadbandModel').get_result()

                voicetext_en = res_en['results'][0]['alternatives'][0]['transcript']
                voicetext_fr=res_fr['results'][0]['alternatives'][0]['transcript']
                if voicetext_fr == english_to_french(voicetext_fr):
                   original=voicetext_fr
                   result = french_to_english(voicetext_fr)

                elif voicetext_en == french_to_english(voicetext_en):
                    original=voicetext_fr
                    result = english_to_french(voicetext_en)

                else:
                    original=''
                    result = "It is not either french or english"
                print(result)



                print("audio saved")
                return render_template("public/upload_audio.html", original=original ,result=result)


            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("public/upload_audio.html" , result="result",original=original)





if __name__ =="__main__":
    app.run(debug=True)
