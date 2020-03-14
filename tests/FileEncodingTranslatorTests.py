import unittest

from modules.FileEncodingTranslator import FileEncodingTranslator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

        file_name = '/Users/psc/develop/projects/git/autoaudit-core/src/main/java/com/sogou/adm/bizdev/audit/autoaudit/core/util/StringUtils.java'
        encoder = FileEncodingTranslator(file_name)
        encoder.translate_encoding("utf-8")


if __name__ == '__main__':
    unittest.main()
