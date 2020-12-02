#!/usr/bin/env python3
# coding = utf-8
import os
import sys

from modules.DirectoryTraversal import DirectoryTraversal
from modules.FileEncodingTranslator import FileEncodingTranslator


def callback(path, *args, **kwargs):
    print("Now translate file {}".format(path))
    translator = FileEncodingTranslator(path)
    translator.translate_encoding("UTF-8", True)


def file2utf8(root_path):
    traversal = DirectoryTraversal(root_path, ['.idea', '.git'], ['A.java'])
    traversal.traverse(callback=callback)
    print(root_path)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file2utf8(sys.argv[1])
    else:
        print("Usage: ./java_file_utf8.py <path>")
