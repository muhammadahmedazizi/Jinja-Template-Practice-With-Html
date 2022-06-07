from jinja2 import Environment, FileSystemLoader
import csv
import os
from datetime import datetime

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')

fileloader = FileSystemLoader(templates_dir)
env = Environment(loader=fileloader)
template = env.get_template('blog-post-template.html')


with open('sample-blog-data.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        title=row[0]
        slug = row[1]
        category = row[2]
        body = row[3]
        date = row[4]
        labels = row[5]
        labels = labels.strip()
        labels = labels.split(",")

        filename=f'{slug}.html'
        filename = os.path.join(root, 'html', filename)
        with open(filename, 'w', encoding='utf-8') as fh:
            fh.write(template.render(
                title=title,
                slug=slug,
                category=category,
                body=body,
                date=date,
                labels=labels,
            ))


