import unittest

from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter(self):
        text_code_single = TextNode("`this is a code block` text section", TextType.NORMAL)
        text_code_end = TextNode("testing `end of string code`", TextType.NORMAL)
        text_multiple = TextNode("testing `multiple` separate `code blocks`", TextType.NORMAL)
        ret = split_nodes_delimiter([text_code_single, text_code_end, text_multiple], "`", TextType.CODE)
        expected_value = [
            TextNode("this is a code block", TextType.CODE),
            TextNode(" text section", TextType.NORMAL),
            TextNode("testing ", TextType.NORMAL),
            TextNode("end of string code", TextType.CODE),
            TextNode("testing ", TextType.NORMAL),
            TextNode("multiple", TextType.CODE),
            TextNode(" separate ", TextType.NORMAL),
            TextNode("code blocks", TextType.CODE)
        ]
        self.assertEqual(ret, expected_value)

    def test_empty_string(self):
        empty_node = TextNode("", TextType.NORMAL)
        self.assertEqual(split_nodes_delimiter([empty_node], "**", TextType.BOLD), [])

    def test_bold_delimiter(self):
        bold_node = TextNode("this is **bold** text", TextType.NORMAL)
        expected_value = [
            TextNode("this is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_delimiter([bold_node], "**", TextType.BOLD), expected_value)

if __name__ == "__main__":
    unittest.main()