from ibm_watson import SpeechToTextV1, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


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



with open('helloworld.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-AU_NarrowbandModel').get_result()
voicetext = res['results'][0]['alternatives'][0]['transcript']
def english_to_french(input1):
    translation = lt.translate(text=input1, model_id='en-fr-CA').get_result()
    translatedtext = translation['translations'][0]['translation']

    return translatedtext
def french_to_english(input1):
    translation = lt.translate(text=input1, model_id='fr-en').get_result()
    translatedtext = translation['translations'][0]['translation']
    return translatedtext
print(english_to_french(voicetext))
