import json
import more_itertools
import os
import shutil
import math

from pprint import pprint
from jinja2 import Environment, FileSystemLoader, select_autoescape

from livereload import Server


def load_json(file_name):
    with open(file_name, "r", encoding="utf-8") as my_file:
        json_file = my_file.read()

    received_json_file = json.loads(json_file)
    # genres = set()

    # for book in received_json_file:
    #     genres.update(book.get('genres', '').split(', '))

    # return received_json_file, list(genres)
    return received_json_file


def rebuild():
    ...
    print('REBUILD')


def main():
    characters_folder = 'pages'
    if os.path.exists(characters_folder):
        shutil.rmtree(characters_folder)
    os.makedirs(characters_folder)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']),
    )
    template = env.get_template('template.html')

    meta_data = load_json("meta_data.json")

    if meta_data:
        chunked_meta_data = more_itertools.chunked(meta_data, 10)
        number_pages = math.ceil(len(meta_data) / 10)
        
        print(number_pages)

        for num_page, book  in enumerate(chunked_meta_data, 1):
            # for genres in book:
            #     genres_str = genres.get('genres', '')
            #     genres_list = [genre.strip() for genre in genres_str.split(',')]
            #     print(f"Жанры книги '{genres['title']}': {genres_list}")

            rendered_page = template.render(
                books=book,
                current_page=num_page,
                number_pages=number_pages,
                # genres=genres_list
            )

            filename = f"pages/index{num_page}.html"
            with open(filename, 'w', encoding='utf8') as file:
                file.write(rendered_page)

    else:
        print('Файл meta_data.json пуст.')

    rebuild()

    server = Server()
    server.watch('template.html', main)
    server.serve(root='.', default_filename='pages/index1.html')


if __name__ == "__main__":
    main()