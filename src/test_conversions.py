import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
from node_transform import text_node_to_html_node

class TestNodeConversions(unittest.TestCase):
    def test_node_conversion(self):
        text_node = TextNode("basic text", TextType.NORMAL)
        leaf_comp_node = LeafNode(None, "basic text")
        new_leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(new_leaf_node, leaf_comp_node)


if __name__ == "__main__":
    unittest.main()