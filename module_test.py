import unittest
import app

with open("uploads/result.mp3", 'rb') as f:
    res_en = app.stt.recognize(audio=f, content_type='audio/mp3',
                           model='en-US_BroadbandModel').get_result()
with open("uploads/result.mp3", 'rb') as f:
    res_fr = app.stt.recognize(audio=f, content_type='audio/mp3',
                           model='fr-CA_BroadbandModel').get_result()

voicetext_en = res_en['results'][0]['alternatives'][0]['transcript']
voicetext_fr = res_fr['results'][0]['alternatives'][0]['transcript']
if voicetext_fr == app.english_to_french(voicetext_fr):
    original = voicetext_fr
    result = app.french_to_english(voicetext_fr)

elif voicetext_en == app.french_to_english(voicetext_en):
    original = voicetext_en
    result = app.english_to_french(voicetext_en)

else:
    original = ''
    result = "It is not either french or english"
class TestMyModule(unittest.TestCase):
    def test_f2e(self):
        if voicetext_fr == app.english_to_french(voicetext_fr):
            self.assertEqual(app.french_to_english(original), result)
            self.assertNotEqual(app.french_to_english(original), original)
        elif voicetext_en == app.french_to_english(voicetext_en):
            self.assertEqual(app.english_to_french(original), result)
            self.assertNotEqual(app.english_to_french(original), original)



if __name__=='__main__':
    unittest.main()
