import unittest
import app
class TestMyModule(unittest.TestCase):

    def test_f2e(self,input1):
        self.assertEqual(app.french_to_english(input1), "hello world")
        self.assertNotEqual(app.french_to_english(input1), input1)
    def test_e2f(self,input1):
        self.assertEqual(app.english_to_french(app.voicetext), "monde de bonjour ")
        self.assertNotEqual(app.english_to_french((app.voicetext), "hello world"))


if __name__=='__main__':
    unittest.main()
