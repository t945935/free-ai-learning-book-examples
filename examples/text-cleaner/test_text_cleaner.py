import unittest

from text_cleaner import clean_text


class CleanTextTests(unittest.TestCase):
    def test_trims_edges_and_removes_blank_lines(self):
        self.assertEqual(clean_text("  alpha  \n\n  beta\t\n"), "alpha\nbeta")

    def test_empty_input_returns_empty_string(self):
        self.assertEqual(clean_text(""), "")

    def test_whitespace_only_input_returns_empty_string(self):
        self.assertEqual(clean_text(" \t\n  \n"), "")

    def test_preserves_internal_spaces_and_unicode(self):
        self.assertEqual(clean_text("  hello  world  \n  繁體中文  \n"), "hello  world\n繁體中文")


if __name__ == "__main__":
    unittest.main()
