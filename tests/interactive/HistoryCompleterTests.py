import unittest

from modules.interactive.HistoryCompleter import HistoryCompleter


class HistoryCompleterTests(unittest.TestCase):
    def test_get_input(self):
        completer = HistoryCompleter()
        completer.get_input()
        self.assertEqual(True, True)

    def test_loop_input(self):
        completer = HistoryCompleter()
        completer.loop_input(print)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
