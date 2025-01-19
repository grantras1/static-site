import re
from itertools import takewhile, chain

from htmlnode import HTMLNode
from split_delimiter import text_to_textnodes

MARKDOWN_TYPE_CONVERSION = {
    "paragraph": "p",
    "italic": "em",
    "heading": "h1",
    "quote": "blockquote",
    "unordered_list": "ul",
    "ordered_list": "ol",
    "code": "code",
}

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n")
    new_blocks = []
    current_block = ""
    for block in blocks:
        if block == "":
            if current_block:
                new_blocks.append(current_block)
                current_block = ""
        else:
            if current_block:
                current_block += "\n"
            current_block += block
    if current_block:
        new_blocks.append(current_block)

    return new_blocks

def block_to_block_type(block):
    if re.search(r'^#{1,6} \S.*', block):
        return "heading"
    elif re.search(r'```.*```', block, re.DOTALL):
        return "code"
    elif block[0] == ">":
        for line in block.split("\n"):
            if line[0] != ">":
                return "paragraph"
        return "quote"
    elif block[0] == "*" or block[0] == "-":
        for line in block.split("\n"):
            if not re.search(r'^[*-] .+', line):
                return "paragraph"
        return "unordered_list"
    elif block[0:3] == "1. ":
        lines = block.split("\n")
        for i in range(0, len(lines)):
            if lines[i][0:3] != f"{i + 1}. ":
                return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    new_nodes = list(map(lambda node: node.convert_to_htmlnode(), text_nodes))
    return new_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    print(blocks)
    top_level_nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == "heading":
            header_level = sum(1 for _ in takewhile(lambda x: x == '#', block))
            child_nodes = text_to_children(block.replace("#", "").lstrip())
            top_level_nodes.append(HTMLNode(f"h{header_level}", None, child_nodes))
        elif type == "code":
            top_level_nodes.append(HTMLNode("pre", None, [HTMLNode("code", block)]))
        elif type == "quote":
            child_nodes = text_to_children(block.replace("> ", ""))
            top_level_nodes.append(HTMLNode("blockquote", None, child_nodes))
        elif type == "unordered_list":
            list_elements = []
            for element in block.split("\n"):
                list_elements.append(HTMLNode("li", None, text_to_children(element[2:])))
            top_level_nodes.append(HTMLNode("ul", None, list_elements))
        elif type == "ordered_list":
            list_elements = []
            for element in block.split("\n"):
                list_elements.append(HTMLNode("li", None, text_to_children(element[3:])))
            top_level_nodes.append(HTMLNode("ol", None, list_elements))
        else:
            child_nodes = text_to_children(block)
            top_level_nodes.append(HTMLNode("p", None, child_nodes))
    return HTMLNode("div", None, top_level_nodes)