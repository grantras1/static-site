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
markdown = """# This is a heading" 

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

print(markdown_to_blocks(markdown))