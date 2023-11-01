import unittest
from game.dictionary import Dictionary
class TestDictionary(unittest.TestCase):
    def test_dictionary(self):
        dictionary = Dictionary('dictionary/dictionary.txt')
        self.assertTrue(dictionary.has_word('duda'))

    def test_word_false(self):
        dictionary = Dictionary('dictionary/dictionary.txt')
        self.assertFalse(dictionary.has_word('aaae'))
        
    def test_word_true_caps_lock(self):
        dictionary = Dictionary('dictionary/dictionary.txt')
        self.assertTrue(dictionary.has_word('AUTO'))
if __name__ == '__main__':
    unittest.main()