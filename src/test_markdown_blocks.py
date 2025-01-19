import unittest

from htmlnode import HTMLNode
from markdown_blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node

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

    def test_markdown_to_html_node_multiple_blocks(self):
        multiple_blocks = "```test this is some code\nwith multiple lines\nand *fake* inline markdown```\n\n1. first element\n2. second element\n3. *third* element"
        expected_result = HTMLNode("div", None, [
            HTMLNode("pre", None, [
                HTMLNode("code", "```test this is some code\nwith multiple lines\nand *fake* inline markdown```")
            ]),
            HTMLNode("ol", None, [
                HTMLNode("li", None, [
                    HTMLNode(None, "first element")
                ]),
                HTMLNode("li", None, [
                    HTMLNode(None, "second element")
                ]),
                HTMLNode("li", None, [
                    HTMLNode("i", "third"),
                    HTMLNode(None, " element")
                ])
            ])
        ])
        self.assertEqual(markdown_to_html_node(multiple_blocks), expected_result) 

    def test_markdown_to_html_node_header(self):
        header_markdown = "## **My** *Programming* Journey"
        expected_result = HTMLNode("div", None, [
                            HTMLNode("h2", None, [
                                HTMLNode("b", "My"),
                                HTMLNode(None, " "),
                                HTMLNode("i", "Programming"),
                                HTMLNode(None, " Journey")
                            ])
                        ])
        self.assertEqual(markdown_to_html_node(header_markdown), expected_result)

    def test_markdown_to_html_node_paragraph(self):
        paragraph_markdown = "I started learning Python because it's **really beginner-friendly**. Here's what I've learned:"
        expected_result = HTMLNode("div", None, [
            HTMLNode("p", None, [
                HTMLNode(None, "I started learning Python because it's "),
                HTMLNode("b", "really beginner-friendly"),
                HTMLNode(None, ". Here's what I've learned:")
            ])
        ])
        self.assertEqual(markdown_to_html_node(paragraph_markdown), expected_result)

    def test_markdown_to_html_node_code(self):
        code_markdown = "```this is some code\nwith multiple lines\nand *fake* inline markdown```"
        expected_result = HTMLNode("div", None, [
            HTMLNode("pre", None, [
                HTMLNode("code", "```this is some code\nwith multiple lines\nand *fake* inline markdown```")
            ])
        ])
        self.assertEqual(markdown_to_html_node(code_markdown), expected_result)

    def test_markdown_to_html_node_quote(self):
        quote_markdown = "> be me\n> writing tests longer *than* writing actual code\n> test **fails**"
        expected_result = HTMLNode("div", None, [
            HTMLNode("blockquote", None, [
                HTMLNode(None, "be me\nwriting tests longer "),
                HTMLNode("i", "than"),
                HTMLNode(None, " writing actual code\ntest "),
                HTMLNode("b", "fails")
            ])
        ])
        self.assertEqual(markdown_to_html_node(quote_markdown), expected_result)
    
    def test_markdown_to_html_node_unordered_list(self):
        ul_markdown = "* first element\n- second element\n* *third* element"
        expected_result = HTMLNode("div", None, [
            HTMLNode("ul", None, [
                HTMLNode("li", None, [
                    HTMLNode(None, "first element")
                ]),
                HTMLNode("li", None, [
                    HTMLNode(None, "second element")
                ]),
                HTMLNode("li", None, [
                    HTMLNode("i", "third"),
                    HTMLNode(None, " element")
                ])
            ])
        ])
        self.assertEqual(markdown_to_html_node(ul_markdown), expected_result)

    def test_markdown_to_html_node_unordered_list(self):
        ol_markdown = "1. first element\n2. second element\n3. *third* element"
        expected_result = HTMLNode("div", None, [
            HTMLNode("ol", None, [
                HTMLNode("li", None, [
                    HTMLNode(None, "first element")
                ]),
                HTMLNode("li", None, [
                    HTMLNode(None, "second element")
                ]),
                HTMLNode("li", None, [
                    HTMLNode("i", "third"),
                    HTMLNode(None, " element")
                ])
            ])
        ])
        self.assertEqual(markdown_to_html_node(ol_markdown), expected_result)


if __name__ == "__main__":
    unittest.main()