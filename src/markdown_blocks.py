import re

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