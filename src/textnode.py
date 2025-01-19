from enum import Enum

from htmlnode import HTMLNode


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        return self.text == node.text and self.text_type == node.text_type and self.url == node.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def convert_to_htmlnode(self):
        match self.text_type:
            case TextType.NORMAL:
                return HTMLNode(None, self.text)
            case TextType.BOLD:
                return HTMLNode("b", self.text)
            case TextType.ITALIC:
                return HTMLNode("i", self.text)
            case TextType.CODE:
                return HTMLNode("code", self.text)
            case TextType.LINKS:
                return HTMLNode("a", self.text, None, {"href": self.url})
            case TextType.IMAGES:
                return HTMLNode("img", None, None, {"src": self.url, "alt": self.text})
            case _:
                raise ValueError(f"Invalid text type for TextNode: {self.text_type}")