# coding = utf-8

import os


class DirectoryTraversal(object):
    """
    Directory traversal, it can walk all directory or recursively walk all sub-directories.
    """

    def __init__(self, root_path):
        """
        set current path.
        :param root_path: the root path to traverse.
        """
        self.__root_path = root_path

    def traverse(self, callback=None, *args, **kwargs):
        """
        do traverse the directory recursively.
        :param callback: if none, just print. The curr traversed file and args and kwargs will be pass to the callback.
        :param args: the parameters tuple passed to callback function.
        :param kwargs: the parameters dict passed to callback function.
        :return:
        """
        # os.walk will traverse directory recursively, there is no no need do yourself.
        for dir_name, sub_dirs, files in os.walk(self.__root_path):
            print("Now traverse path {}".format(dir_name))
            if callback is None:
                print(files)
            else:
                for file in files:
                    callback(file, args, kwargs)
