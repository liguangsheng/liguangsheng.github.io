# -*- coding: utf-8 -*-
import os
import yaml

INDEX = 'README.md'


class MarkdownFile(object):
    def __init__(self, path):
        self.path = path[2:].replace('\\', '/')
        self.name_ext = os.path.split(path)[-1]
        self.name = self.name_ext[:-3]
        self._load_metadata()

    def _load_metadata(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.read()
        metadata = content.split('\n\n', 1)[0].split('\n')
        if metadata[0] == '---':
            metadata = metadata[1:]
        if metadata[-1] == '---':
            metadata = metadata[:-1]
        metadata = '\n'.join(metadata)
        self.metadata = {i[0].lower(): i[1] for i in yaml.load(metadata).items()}
        if 'modified' not in self.metadata:
            self.metadata['modified'] = self.metadata['date']

        self.title = self.metadata['title']
        self.date = self.metadata['date']
        self.modified = self.metadata['modified']
        self.top = self.metadata.get('top') or False


def markdown_files():
    md_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md') and not file == 'README.md':
                md_files.append(MarkdownFile(os.path.join(root, file)))
    return sorted(md_files, key=lambda x:x.metadata['modified'], reverse=True)


def generate():
    with open(INDEX, 'w', encoding='utf-8') as index_file:
        for markdown_file in markdown_files():
            item = '* [{}]({})'.format(markdown_file.title, markdown_file.path)
            print(item)
            index_file.write(item + '\n')

generate()