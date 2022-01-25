import unittest
import app
class TestMyModule(unittest.TestCase):

    def test_f2e(self):
        self.assertEqual(app.french_to_english(app.voictext), "hello world")
        self.assertNotEqual(app.french_to_english(app.voicetext), "mon de bonjour")
    def test_e2f(self):
        self.assertEqual(app.english_to_french(app.voicetext), "monde de bonjour ")
        self.assertNotEqual(app.english_to_french((app.voicetext), "hello world"))


if __name__=='__main__':
    unittest.main()
