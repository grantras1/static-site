import unittest

from markdown_extraction import extract_markdown_links, extract_markdown_images
from page_generation import extract_title

class TestMarkdownExtraction(unittest.TestCase):
    def test_link_extraction(self):
        links = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_image_extraction(self):
        images = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extraction_nonconsecutive(self):
        images = extract_markdown_images("[This] shouldn't be detected as an image (https://i.imgur.com/aKaOqIh.gif)")
        self.assertEqual(images, [])

    def test_extraction_empty(self):
        images = extract_markdown_images("")
        self.assertEqual(images, [])

    def test_extract_title(self):
        markdown = "```this is some code```\n\nwith some regular paragraphs\n\n# real header"
        self.assertEqual(extract_title(markdown), "real header")

if __name__ == "__main__":
    unittest.main()