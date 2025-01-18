import re
from time import sleep

from textnode import TextNode, TextType
from markdown_extraction import extract_markdown_images, extract_markdown_links


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
    print(ret)
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

def get_indices_of_match(pattern, text):
    idx = 0
    idx_total = 0
    indices = []
    while idx_total < len(text) - 1:
        match = re.search(pattern, text[idx:])
        if not match:
            break
        indices.append((idx + match.start(), idx + match.end()))
        idx = match.end()
        idx_total += idx
    return indices

def split_nodes_regex(old_nodes, pattern, type):
    new_nodes = []
    for node in old_nodes:
        indices = get_indices_of_match(pattern, node.text)
        if len(indices) == 0:
            new_nodes.append(node)
            continue
        idx = 0
        for regex_index in indices:
            if regex_index[0] > 0:
                new_nodes.append(TextNode(node.text[idx:regex_index[0]], node.text_type))
            link = extract_markdown_links(node.text[idx:])[0]
            new_nodes.append(TextNode(link[0], type, link[1]))
            idx += regex_index[1]
        if indices[-1][1] < len(node.text):
            new_nodes.append(TextNode(node.text[indices[-1][1]:], node.text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes_regex(old_nodes, r"\!\[.*?\]\(.*?\)", TextType.IMAGES)

def split_nodes_link(old_nodes):
    return split_nodes_regex(old_nodes, r"\[.*?\]\(.*?\)", TextType.LINKS)

