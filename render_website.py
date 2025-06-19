import json
import more_itertools
import os
import shutil
import math

from jinja2 import Environment, FileSystemLoader, select_autoescape

from livereload import Server


def load_json(file_name):
    with open(file_name, "r", encoding="utf-8") as my_file:
        received_json_file = json.load(my_file)
    return received_json_file

def main():
    folder = 'pages'
    shutil.rmtree(folder, ignore_errors=True)
    os.makedirs(folder, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']),
    )
    template = env.get_template('template.html')

    meta_data = load_json("meta_data.json")

    if meta_data:
        chunked_meta_data = more_itertools.chunked(meta_data, 10)
        number_pages = math.ceil(len(meta_data) / 10)
        
        for num_page, book  in enumerate(chunked_meta_data, 1):
            rendered_page = template.render(
                books=book,
                current_page=num_page,
                number_pages=number_pages,
            )

            filename = f"pages/index{num_page}.html"
            with open(filename, 'w', encoding='utf8') as file:
                file.write(rendered_page)

    else:
        print('Файл meta_data.json пуст.')

    server = Server()
    server.watch('template.html', main)
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == "__main__":
    main()
