# -*- coding: utf-8 -*-
import os

INDEX = 'README.md'

markdown_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md') and not file == 'README.md':
            markdown_files.append((
                file,
                os.path.join(root, file),
            ))

with open(INDEX, 'w', encoding='utf-8') as index_file:
    for markdown_file in markdown_files:
        name = markdown_file[0][:-3]
        url = markdown_file[1][2:].replace('\\', '/')
        item = '* [{}]({})'.format(name, url)
        print(item)
        index_file.write(item + '\n')