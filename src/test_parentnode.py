import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    basic_node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    def test_to_html_basic(self):
        self.assertEqual(self.basic_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_no_children(self):
        no_children = ParentNode("p", None)
        with self.assertRaises(ValueError):
            no_children.to_html()

    def test_to_html_nested(self):
        h2_node = ParentNode(
            "h2", 
            [
                LeafNode("b", "h2 bold text"),
                LeafNode("i", "h2 italic text")
            ]
        )

        nested_node = ParentNode("h1", [self.basic_node, h2_node])
        self.assertEqual(nested_node.to_html(), "<h1><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><h2><b>h2 bold text</b><i>h2 italic text</i></h2></h1>")


if __name__ == "__main__":
    unittest.main()