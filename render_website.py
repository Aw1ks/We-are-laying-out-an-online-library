import json

from pprint import pprint
from jinja2 import Environment, FileSystemLoader, select_autoescape

from livereload import Server


def load_json(file_name):
    with open(file_name, "r", encoding="utf-8") as my_file:
        meta_data_json = my_file.read()

    return json.loads(meta_data_json)


def rebuild():
    ...
    print("Rebuild")


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    meta_data = load_json("meta_data.json")

    rendered_page = template.render(
        books=meta_data,
    )

    filename = "index.html"
    with open(filename, 'w', encoding='utf8') as file:
        file.write(rendered_page)

    rebuild()

    server = Server()
    server.watch('template.html', main)
    server.serve(root='.')


if __name__ == "__main__":
    main()