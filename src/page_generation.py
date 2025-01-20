import os
import re
from markdown_blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == "heading":
            if re.match(r'^# ', block):
                return block[2:]
            
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} from {template_path}")
    with open(from_path, "r") as markdown:
        with open(template_path, "r") as template_file:
            markdown = markdown.read()
            content = template_file.read()
            new_html = content.replace("{{ Title }}", extract_title(markdown))
            new_html = new_html.replace("{{ Content }}", markdown_to_html_node(markdown).to_html())
            with open(dest_path, "w") as dest:
                print(dest_path)
                dest.write(new_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path=None):
    for dir in os.listdir(dir_path_content):
        current_path = f"{dir_path_content}/{dir}"
        print(current_path)
        if os.path.isfile(current_path) and current_path[-3:] == ".md":
            generate_page(current_path, template_path, current_path.replace("content", "public").replace("md", "html"))
        elif os.path.isdir(current_path):
            print(f"Directory: {current_path}")
            os.mkdir(current_path.replace("content", "public"))
            generate_pages_recursive(current_path + "/", template_path)

"""
def copy_static_to_public(current_directory="static/", refresh=True):
    if refresh:
        if os.path.exists("public"):
            shutil.rmtree("public")
        os.mkdir("public")
    for dir in os.listdir(current_directory):
        current_path = f"{current_directory}/{dir}"
        if os.path.isfile(current_path):
            shutil.copy(current_path, current_path.replace("static", "public"))
        else:
            os.mkdir(current_path.replace("static", "public"))
            copy_static_to_public(current_path + "/", False)
"""