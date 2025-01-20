import os
import shutil

from page_generation import generate_page, generate_pages_recursive

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

def main():
    #generate_page("content/index.md", "template.html", "public/index.html")
    copy_static_to_public()
    generate_pages_recursive("content", "template.html")

if __name__ == "__main__":
    main()