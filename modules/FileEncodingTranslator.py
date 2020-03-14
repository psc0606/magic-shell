# coding=utf8
import os
import shutil

import cchardet as chardet

"""
Translate the file encoding to other.
"""


class FileEncodingTranslator:
    def __init__(self, path):
        """
        :param path: the path of file.
        """
        self.__path = path

    def detect_code(self):
        """
        Automatic detect encoding of file.
        :return: the encoding of source file.
        """
        with open(self.__path, 'rb') as f:
            msg = f.read()
            print(msg)
            dicts = chardet.detect(msg)
        return dicts["encoding"]

    def translate_encoding(self, encoding):
        """
        translate the file encoding to other, then save it to /tmp/file_name.
        :param encoding: to target encoding of the file.
        """
        # get the simple file name to generate a tmp file with the specified code.
        tmp_path = os.path.join(os.path.sep, "tmp", os.path.basename(self.__path))
        src_encoding = self.detect_code()
        if src_encoding == encoding:
            return

        with open(self.__path, 'r', encoding=src_encoding) as fr, open(tmp_path, 'w', encoding=encoding) as fw:
            for line in fr:
                content = str(line.encode(encoding), encoding)
                fw.write(content)
                print(content)
        fr.close()
        fw.close()
        self.__replace_file(tmp_path, self.__path)

    @staticmethod
    def __replace_file(src_path, target_path):
        shutil.move(src_path, target_path)
