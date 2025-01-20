import unittest

from page_generation import extract_title

class TestPageGeneration(unittest.TestCase):

    def test_extract_title(self):
        markdown = "```this is some code```\n\nwith some regular paragraphs\n\n# real header"
        self.assertEqual(extract_title(markdown), "real header")

if __name__ == "__main__":
    unittest.main()