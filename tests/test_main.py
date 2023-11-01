import unittest
from unittest.mock import patch, Mock
from game.main import main  

class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=["2", "Juan", "Marcos", "N", "9", "Y", "9", "Y"])
    @patch('builtins.print')
    def test_main_function(self, mock_input, mock_print): 
        main()
    
if __name__ == '__main__':
    unittest.main()