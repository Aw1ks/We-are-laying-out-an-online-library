import json

from pprint import pprint
from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    with open("meta_data.json", "r", encoding="utf-8") as my_file:
        meta_data_json = my_file.read()

    meta_data = json.loads(meta_data_json)

    rendered_page = template.render(
        books=meta_data,
    )

    filename = "index.html"
    with open(filename, 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()