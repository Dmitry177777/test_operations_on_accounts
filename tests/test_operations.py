import unittest
from data import operations


class TestOperations(unittest.TestCase):

    def test_check(self):
        self.assertEqual(operations.check_list({"vcs": "mercurial"}, "vcs"), 'mercurial')
        self.assertEqual(operations.check_list({"vcs": "mercurial"}, "vcs", "git"), 'mercurial')
        self.assertEqual(operations.check_list({}, "vcs", 'git'), 'git')
        self.assertEqual(operations.check_list({}, "vcs", "bazaar"), "bazaar")

    def test_x(self):
        self.assertEqual(operations.x_list({"vcs": "mercurial"}, "vcs"), 'mercurial')
        self.assertEqual(operations.x_list({"vcs": "mercurial"}, "vcs", "git"), 'mercurial')
        self.assertEqual(operations.x_list({}, "vcs", 'git'), 'git')
        self.assertEqual(operations.x_list({}, "vcs", "bazaar"), "bazaar")

