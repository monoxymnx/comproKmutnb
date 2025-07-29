import unittest

def format_string(*args):
    text = " ".join(args)
    return text.replace(" ", "").upper()

result = format_string("hello", "world","howareyou?")
print(result)  

result = format_string("python", "is", "fun")
print(result)

result = format_string("this", "is", "a", "test")
print(result)


def upper_nospace(text):
    return text.replace(" ", "").upper()

if __name__ == "__main__":
    print(upper_nospace("Hello World How are you?"))
    print(upper_nospace("Python is fun"))
    print(upper_nospace("This is a test"))



class TestFormatStr(unittest.TestCase):
    def test_upper_nospace(self):
        self.assertEqual(upper_nospace("abc def"), "ABCDEF")
        self.assertEqual(upper_nospace("hello world!"), "HELLOWORLD!")
        self.assertEqual(upper_nospace("python programming"), "PYTHONPROGRAMMING")