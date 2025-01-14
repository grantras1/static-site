from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node doesn't have a value")
        if self.tag == None:
            return self.value
        
        start_tag = f"<{self.tag} {self.props_to_html()}>" if self.props else f"<{self.tag}>"
        return f"{start_tag}{self.value}</{self.tag}>"