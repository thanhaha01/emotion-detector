import unittest
from emotion_detector import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_happy(self):
        result = emotion_detector("I am happy")
        self.assertEqual(result['emotion'], 'joy')

    def test_sad(self):
        result = emotion_detector("I am sad")
        self.assertEqual(result['emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()
