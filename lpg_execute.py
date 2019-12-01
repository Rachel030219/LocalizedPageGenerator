#!/usr/bin/env python3

import os
import re
import sys
import shutil
import config

arguments = sys.argv
languages_dir = os.path.join('sources','locales')
resources_dir = 'resources'


def main(arguments: list):
    print('Localized Page Generator version 0.1 BETA')
    # Make a clean output environment
    if os.path.exists(config.output_dir):
        print('INFO: Removing previously created files')
        removedir(config.output_dir)
    print('INFO: Creating output folder')
    os.mkdir(config.output_dir)
    if os.path.isdir(resources_dir):
        for file in listdir_fullpath(resources_dir):
            shutil.copy(file, config.output_dir)
    # Generate translated pages
    if len(arguments) is 1:
        if os.path.isfile(config.template_path) and os.path.isdir(languages_dir):
            translation_sources = [path for path in listdir_fullpath(languages_dir) if path.endswith('.lpgdb')]
            if len(translation_sources) is 0:
                print('ERROR: Please add at least one valid lpgdb file')
                return
            else:
                for source in translation_sources:
                    translation_dict = {}
                    source_content = [line for line in open(source).readlines() if line.strip()]
                    language = os.path.splitext(os.path.relpath(source, languages_dir))[0]
                    for line in source_content:
                        add_to_dict(line, translation_dict)
                    generate(config.template_path, translation_dict, language)
                    print('INFO: L10n for language ' + language + ' done')
        else:
            print('ERROR: Please check the paths in config.py')
            return


def add_to_dict(string: str, dictionary: dict):
    maps = string.split('>', 1)
    if len(maps) is not 1:
        dictionary[maps[0].strip()] = maps[1]


def generate(template: str, dictionary: dict, language: str):
    template = [line for line in open(config.template_path).readlines()]
    output_path = os.path.join(config.output_dir, language)
    os.makedirs(output_path)
    output = open(os.path.join(output_path, 'index.html'), 'w')
    regex = re.compile(r'(%locale/(\S+)%)')
    for line in template:
        regex_output = line.replace('\n', '').replace('\r', '')
        regex_match = regex.findall(line)
        for match in regex_match:
            if dictionary[match[1].strip()]:
                regex_output = regex_output.replace(match[0], dictionary[match[1].strip()]).replace('\n', '').replace('\r', '')
            else:
                print('ERROR: Key \'' + match[1] + '\' matches nothing')
                return
        output.write(regex_output + '\n')


def listdir_fullpath(dir: str):
    return [os.path.join(dir, f) for f in os.listdir(dir)]


def removedir(dir: str):
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('ERROR: Failed to delete %s. Reason: %s' % (file_path, e))
    os.rmdir(dir)


main(arguments)
