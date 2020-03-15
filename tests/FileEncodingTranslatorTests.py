# coding = utf-8
import unittest

from modules.FileEncodingTranslator import FileEncodingTranslator


class MyTestCase(unittest.TestCase):
    def test_translate_encoding(self):
        file_name = 'test_file_gb18030.txt'
        encoder = FileEncodingTranslator(file_name)
        encoder.translate_encoding("utf-8", is_replace=False)
        self.assertEqual("GB18030", encoder.detect_code())

        # encoder.translate_encoding("utf-8", is_replace=True)
        # self.assertEqual("UTF-8", encoder.detect_code())


if __name__ == '__main__':
    unittest.main()
