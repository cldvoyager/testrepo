import unittest
import translator

class TestTranslation(unittest.TestCase):
    def test_french_to_english_is_null(self):
        # assertIsNone() to check that if input value is none
        french_text = 'Bonjour'
        english_text = translator.french_to_english(french_text)
        self.assertIsNone(english_text, 'Not None')
                
    def test_french_to_english(self):
        # assertIsNone() to check that if input value is none
        french_text = 'Bonjour'
        english_text = translator.french_to_english(french_text)
        print(english_text)
       
    def test_english_to_french_is_null(self):
        # assertIsNone() to check that if input value is none
        english_text = 'Hello'
        french_text = translator.english_to_french(english_text)
        self.assertIsNone(french_text)
       
    def test_english_to_french(self):
        # assertIsNone() to check that if input value is none
        english_text = 'Hello'
        french_text = translator.english_to_french(english_text)
        print(french_text)
      
if __name__ == '__main__':
    unittest.main()
    