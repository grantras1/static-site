class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        ret = ""
        for key in self.props.keys():
            ret += f'{key}="{self.props[key]}" '
        return ret.rstrip()
    
    def __repr__(self):
        return f"tag: {self.tag}\n" + \
               f"value: {self.value}\n" + \
               f"children: {self.children}\n" + \
               f"props: {self.props}"
    
    def __eq__(self, node):
        return self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props