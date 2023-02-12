import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def test_val(self):
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs"), 'mercurial')
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs", "git"), 'mercurial')
        self.assertEqual(dicts.get_val({}, "vcs", 'git'), 'git')
        self.assertEqual(dicts.get_val({}, "vcs", "bazaar"), "bazaar")