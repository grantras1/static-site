from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.children == None:
            raise ValueError("Parent node does not contain child node(s)")
        if self.tag == None:
            raise ValueError("Parent node does not contain a tag")
        
        ret = f"<{self.tag} {self.props_to_html()}>" if self.props else f"<{self.tag}>"

        for child_node in self.children:
            ret += str(child_node.to_html())

        return ret + f"</{self.tag}>"