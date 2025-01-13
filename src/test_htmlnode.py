import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    #def __generate_node_string(self, tag, value, children, props):     

    def test_eq(self):
        node = HTMLNode("a", "test HTML node", None, {"href": "google.com"})
        node2 = HTMLNode("a", "test HTML node", None, {"href": "google.com"})
        self.assertEqual(str(node), str(node2))

    def test_not_eq(self):
        node = HTMLNode("h1", "test HTML node", None, {"href": "google.com"})
        node2 = HTMLNode("a", "test HTML node", None, {"href": "google.com"})
        self.assertNotEqual(str(node), str(node2))

    def test_props_to_html(self):
        node = HTMLNode("h1", "test HTML node", None, {"href": "google.com"})
        self.assertEqual(node.props_to_html(), 'href="google.com"')

if __name__ == "__main__":
    unittest.main()