# coding=utf8
import os
import shutil

import cchardet as chardet

"""
Translate the file encoding to other.
The cchardet support GB18030 encoding, this encoding is back compatible with gbk(gbk is also back compatible with gb2312).
If you use gb2312 or gbk encoding, cchardet will detect GB18030.

Dependencies:
https://pypi.org/project/cchardet/
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
            # print(msg)
            dicts = chardet.detect(msg)
        return dicts["encoding"]

    def translate_encoding(self, encoding, is_replace=True):
        """
        translate the file encoding to other, then save it to /tmp/file_name.
        :param encoding: to target encoding of the file.
        :param is_replace: whether to replace original file.
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
                # print(content)
        fr.close()
        fw.close()
        if is_replace:
            self.__replace_file(tmp_path, self.__path)

    @staticmethod
    def __replace_file(src_path, target_path):
        shutil.move(src_path, target_path)
