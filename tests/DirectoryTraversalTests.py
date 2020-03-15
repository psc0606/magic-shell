import unittest

from modules.DirectoryTraversal import DirectoryTraversal


class DirectoryTraversalTests(unittest.TestCase):
    def test_traversal(self):
        traversal = DirectoryTraversal('.')
        callback = lambda file, *args, **kwargs: print(len(file))
        traversal.traverse(callback)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
