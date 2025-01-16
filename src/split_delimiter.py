from textnode import TextNode

def generate_split_text(text, delimiter):
    ret = []
    prepend_delimiter = text.split(delimiter)[0] == ''
    for block in text.split(delimiter):
        if block == '':
            continue
        ret.append(block)
        ret.append(delimiter)
    if prepend_delimiter:
        ret.insert(0, delimiter)
    return ret

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Unmatched delimiter")
        split_text = generate_split_text(node.text, delimiter)
        in_delimiter = False
        prev_text = None
        for text in split_text:
            if text == delimiter:
                if in_delimiter:
                    new_nodes.append(TextNode(prev_text, text_type))
                    prev_text = None
                else:
                    if prev_text != None:
                        new_nodes.append(TextNode(prev_text, node.text_type))
                in_delimiter = not in_delimiter
            else:
                prev_text = text
    return new_nodes