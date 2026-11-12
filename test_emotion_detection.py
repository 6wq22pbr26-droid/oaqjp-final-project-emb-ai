"""Integration checks for the live Skills Network Watson emotion model."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Check the five required emotion examples and invalid text."""

    def test_required_emotions(self):
        """The Watson endpoint should identify each required emotion."""
        examples = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for text, expected in examples.items():
            with self.subTest(text=text):
                result = emotion_detector(text)
                self.assertEqual(result["dominant_emotion"], expected)
                for emotion in ("anger", "disgust", "fear", "joy", "sadness"):
                    self.assertGreaterEqual(result[emotion], 0)
                    self.assertLessEqual(result[emotion], 1)

    def test_empty_text(self):
        """Invalid text should produce None values, not invented scores."""
        self.assertTrue(all(value is None for value in emotion_detector("").values()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
