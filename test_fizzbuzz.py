import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    #def test1(self):
     #   string = """1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100"""
      #  self.assertEqual(fizzbuzz.fizzbuzz(), string)
    #def test2(self):
     #   string = """1, 2, Fizz, 4, 5, Fizz, 7, 8, Fizz, 10, 11, Fizz, 13, 14, Fizz, 16, 17, Fizz, 19, 20, Fizz, 22, 23, Fizz, 25, 26, Fizz, 28, 29, Fizz, 31, 32, Fizz, 34, 35, Fizz, 37, 38, Fizz, 40, 41, Fizz, 43, 44, Fizz, 46, 47, Fizz, 49, 50, Fizz, 52, 53, Fizz, 55, 56, Fizz, 58, 59, Fizz, 61, 62, Fizz, 64, 65, Fizz, 67, 68, Fizz, 70, 71, Fizz, 73, 74, Fizz, 76, 77, Fizz, 79, 80, Fizz, 82, 83, Fizz, 85, 86, Fizz, 88, 89, Fizz, 91, 92, Fizz, 94, 95, Fizz, 97, 98, Fizz, 100"""
      #  self.assertEqual(fizzbuzz.fizzbuzz(), string)
    #def test3(self):
     #   string = """1, 2, Fizz, 4, 5, Fizz, 7, 8, Fizz, 10, 11, Fizz, 13, 14, 15, 16, 17, Fizz, 19, 20, Fizz, 22, 23, Fizz, 25, 26, Fizz, 28, 29, 30, 31, 32, Fizz, 34, 35, Fizz, 37, 38, Fizz, 40, 41, Fizz, 43, 44, 45, 46, 47, Fizz, 49, 50, Fizz, 52, 53, Fizz, 55, 56, Fizz, 58, 59, 60, 61, 62, Fizz, 64, 65, Fizz, 67, 68, Fizz, 70, 71, Fizz, 73, 74, 75, 76, 77, Fizz, 79, 80, Fizz, 82, 83, Fizz, 85, 86, Fizz, 88, 89, 90, 91, 92, Fizz, 94, 95, Fizz, 97, 98, Fizz, 100"""
      #  self.assertEqual(fizzbuzz.fizzbuzz(), string)
    #def test4(self):
     #   string = """1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Buzz, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, 41, Fizz, 43, 44, Buzz, 46, 47, Fizz, 49, Buzz, Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, Buzz, 61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, Buzz, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, Buzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz"""
      #  self.assertEqual(fizzbuzz.fizzbuzz(), string)
    def test5(self):
        string = """1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, 15, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, 30, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, Fizz, Buzz, 41, Fizz, 43, 44, 45, 46, 47, Fizz, 49, Buzz, Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, 60, 61, 62, Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, 75, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, Fizz, 88, 89, 90, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, Fizz, Buzz"""
        self.assertEqual(fizzbuzz.fizzbuzz(), string)

if __name__ == '__main__':
    unittest.main()