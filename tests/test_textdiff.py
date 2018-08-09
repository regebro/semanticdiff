import unittest

from semanticdiff import diff_text, format_diff

class TestTextDiff(unittest.TestCase):

    def test_simple(self):
        old = "This is sample text"
        new = "Those are samples boxes"
        diff = diff_text(old, new)
        res = format_diff(diff, old, new)
        self.assertEqual(
            res,
            '= Th\n- is is sample text\n+ ose are samples boxes'
        )
