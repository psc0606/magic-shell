# coding = utf-8

import os


class DirectoryTraversal(object):
    """
    Directory traversal, it can walk all directory or recursively walk all sub-directories.
    """

    def __init__(self, root_path, paths_exclude=[], files_exclude=[]):
        """
        set current path.
        :param root_path: the root path to traverse.
        """
        self.__root_path = root_path
        self.__paths_exclude = paths_exclude
        self.__files_exclude = files_exclude

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
            # exclude path by modify sub_dirs itself.
            sub_dirs[:] = [d for d in sub_dirs if d not in self.__paths_exclude]
            print("Now traverse path {}".format(dir_name))
            if callback is None:
                print(files)
            else:
                # files[:] = [f for f in files if f not in self.__files_exclude]
                for file in files:
                    # skip blacklist file by suffix
                    hit = False
                    for suffix in self.__files_exclude:
                        if file.endswith(suffix):
                            hit = True
                            break
                    if hit:
                        continue
                    callback(os.path.join(dir_name, file), args, kwargs)
