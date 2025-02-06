# Запуск тестов: python test_task1 -v

# .assertEqual(a, b)	    a == b
# .assertTrue(x)	        bool(x) is True
# .assertFalse(x)	        bool(x) is False
# .assertIs(a, b)	        a is b
# .assertIsNone(x)	        x is None
# .assertIn(a, b)	        a in b
# .assertIsInstance(a, b)	isinstance(a, b)

import unittest
from task1 import array_diff

class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(array_diff([1, 2, 5, 6, 7, 8], [1,3,4]), [3,4], "Should be 1")
    
    def test_sum2(self):
        self.assertEqual(array_diff([1, 2], [1,3,4]), [4], "Should be 2")
    # описание тестов -->   

    # <--
if __name__ == '__main__':
    unittest.main()