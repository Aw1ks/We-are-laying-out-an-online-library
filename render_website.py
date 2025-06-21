import json
import more_itertools
import os
import shutil
import math
import argparse

from jinja2 import Environment, FileSystemLoader, select_autoescape

from livereload import Server


def load_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as my_file:
        received_json_file = json.load(my_file)
    return received_json_file


def main():
    folder_for_pages = 'pages'
    folder_download_info = 'meta_data.json'

    parser = argparse.ArgumentParser(
        prog='Online library',
        description='''This project receives data from the specified JSON file with books, 
        creates website pages using an HTML template, and starts the server.''')
    
    parser.add_argument('--info_folder',
                        type=str,
                        default=folder_download_info,
                        help='Path to the folder for downloading book information')
    
    parser.add_argument('--pages_folder',
                        type=str,
                        default=folder_for_pages,
                        help='Path to the folder for downloading pages')
    
    args = parser.parse_args()

    shutil.rmtree(folder_for_pages, ignore_errors=True)
    os.makedirs(folder_for_pages, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']),
    )
    template = env.get_template('template.html')

    meta_data = load_json(args.info_folder)

    number_books_per_page = 10
    chunked_meta_data = more_itertools.chunked(meta_data, number_books_per_page)
    number_pages = math.ceil(len(meta_data) / number_books_per_page)
    
    for num_page, book  in enumerate(chunked_meta_data, 1):
        rendered_page = template.render(
            books=book,
            current_page=num_page,
            number_pages=number_pages,
        )

        filename = f'pages/index{num_page}.html'
        with open(filename, 'w', encoding='utf8') as file:
            file.write(rendered_page)

    server = Server()
    server.watch('template.html', main)
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == '__main__':
    main()
