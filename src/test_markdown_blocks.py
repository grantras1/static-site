import unittest

from markdown_blocks import markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_blocks(self):
        raw_markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        ordered_list = """* This is the first list item in a list block
* This is a list item
* This is another list item"""

        expected_blocks = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", ordered_list]

        self.assertEqual(markdown_to_blocks(raw_markdown), expected_blocks)

if __name__ == "__main__":
    unittest.main()