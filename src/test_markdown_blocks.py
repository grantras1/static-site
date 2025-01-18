import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_blocks(self):
        raw_markdown = """

# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        ordered_list = """* This is the first list item in a list block
* This is a list item
* This is another list item"""

        expected_blocks = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", ordered_list]

        self.assertEqual(markdown_to_blocks(raw_markdown), expected_blocks)

    def test_block_to_block_type(self):
        tests = [
            # Basic cases
            ("Regular paragraph text", "paragraph"),
            ("# Heading 1", "heading"),
            ("### Heading 3", "heading"),
            
            # Edge cases
            ("####### Not a heading", "paragraph"),  # too many #'s
            ("### ", "paragraph"),  # heading with no text
            
            # Lists
            ("* First item\n* Second item", "unordered_list"),
            ("* First\n- Second", "unordered_list"),
            ("1. First\n2. Second", "ordered_list"),
            ("1. First\n3. Second", "paragraph"),  # invalid ordered list (skipped 2)
            
            # Quotes
            ("> Single quote", "quote"),
            (">Multiple\n>lines", "quote"),
            
            # Code blocks
            ("```\ncode here\n```", "code"),
        ]

        for test in tests:
            self.assertEqual(block_to_block_type(test[0]), test[1])

if __name__ == "__main__":
    unittest.main()