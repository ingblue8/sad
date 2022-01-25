import unittest
import translator

with open("uploads/result.mp3", 'rb') as f:
    res_en = translator.stt.recognize(audio=f, content_type='audio/mp3',
                                      model='en-US_BroadbandModel').get_result()
with open("uploads/result.mp3", 'rb') as f:
    res_fr = translator.stt.recognize(audio=f, content_type='audio/mp3',
                                      model='fr-CA_BroadbandModel').get_result()

voicetext_en = res_en['results'][0]['alternatives'][0]['transcript']
voicetext_fr = res_fr['results'][0]['alternatives'][0]['transcript']
if voicetext_fr == translator.english_to_french(voicetext_fr):
    original = voicetext_fr
    result = translator.french_to_english(voicetext_fr)

elif voicetext_en == translator.french_to_english(voicetext_en):
    original = voicetext_en
    result = translator.english_to_french(voicetext_en)

else:
    original = ''
    result = "It is not either french or english"
class TestMyModule(unittest.TestCase):
    def test_f2e(self):
        if voicetext_fr == translator.english_to_french(voicetext_fr):
            self.assertEqual(translator.french_to_english(original), result)
            self.assertNotEqual(translator.french_to_english(original), original)
        elif voicetext_en == translator.french_to_english(voicetext_en):
            self.assertEqual(translator.english_to_french(original), result)
            self.assertNotEqual(translator.english_to_french(original), original)



if __name__=='__main__':
    unittest.main()
