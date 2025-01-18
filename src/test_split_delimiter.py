import unittest

from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL
        )
        node2 = TextNode(
            "[google link](google.com) and normal text",
            TextType.NORMAL
        )
        node3 = TextNode(
            "there are no links here",
            TextType.NORMAL
        )
        expected_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),
            TextNode("google link", TextType.LINKS, "google.com"),
            TextNode(" and normal text", TextType.NORMAL),
            TextNode("there are no links here", TextType.NORMAL)
        ]
        self.assertEqual(split_nodes_link([node, node2, node3]), expected_nodes)

    def test_split_images(self):
        self.maxDiff = None
        node = TextNode(
            "This is the boot.dev logo ![boot.dev logo](https://www.boot.dev/img/bootdev-logo-full-small.webp) python logo ![python logo](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            TextType.NORMAL
        )
        node2 = TextNode(
            "![c logo](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/leiue6x.png) and normal text",
            TextType.NORMAL
        )
        node3 = TextNode(
            "there are no images here",
            TextType.NORMAL
        )
        expected_nodes = [
            TextNode("This is the boot.dev logo ", TextType.NORMAL),
            TextNode("boot.dev logo", TextType.IMAGES, "https://www.boot.dev/img/bootdev-logo-full-small.webp"),
            TextNode(" python logo ", TextType.NORMAL),
            TextNode("python logo", TextType.IMAGES, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode("c logo", TextType.IMAGES, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/leiue6x.png"),
            TextNode(" and normal text", TextType.NORMAL),
            TextNode("there are no images here", TextType.NORMAL)
        ]

        self.assertEqual(split_nodes_image([node, node2, node3]), expected_nodes)
    
    def test_text_to_testnodes(self):
        nodes = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)
if __name__ == "__main__":
    unittest.main()