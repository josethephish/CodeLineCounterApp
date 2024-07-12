import unittest
from app import CodeLineCounter

class TestApp(unittest.TestCase):
    def test_should_count_code_lines(self):
        code = "int a = 0;\n# this is a comment\n\nint b = 1;"
        counter = CodeLineCounter()
        result = counter.count(code)
        self.assertEqual(result, 2)  # Solo las líneas de código reales deben contarse

if __name__ == '__main__':
    unittest.main()
