import unittest
import main
class TestMyModule(unittest.TestCase):

    def test_f2e(self):
        self.assertEqual(main.french_to_english(main.voicetext), "hello world")
        self.assertNotEqual(main.french_to_english(main.voicetext), "monde de bonjour")
    def test_e2f(self):
        self.assertEqual(main.english_to_french(main.voicetext),"monde de bonjour ")
        self.assertNotEqual(main.english_to_french((main.voicetext),"hello world"))


if __name__=='__main__':
    unittest.main()
