import jsonlines
import json
from langdetect import detect
import re
import os.path


# f = open(os.path.dirname(__file__) + '/../data.yml')

Tuoitre = '"H:/Vietnamese word representations/Text_classification_data/Tuoitre/Tuoitre.json"'
Vnexpress = 'H:/Vietnamese word representations/Text_classification_data/Vnexpress/Vnexpress.json'
Thanhnien = 'H:/Vietnamese word representations/Text_classification_data/Thanhnien/Thanhnien.json'
Dantri = 'H:/Vietnamese word representations/Text_classification_data/Dantri/Dantri.json'
Vnn = 'H:/Vietnamese word representations/Text_classification_data/Vnn/Vnn.json'
Vtv = 'H:/Vietnamese word representations/Text_classification_data/Vtv/Vtv.json'


tuoitre_bad_title = ['Noname']

vnn_bad_tags = ['vnn', 'vietnamnet', 'vietnamnetvn', 'vietnamnetvn doc bao', 'vietnamnet.vn']
vnn_english = 'news'


def is_dup(obj, key=''):
    title = obj['title']
    tag = obj['tags'][0]
    title = title.strip()
    tag = tag.strip()
    if tag == title:
        return True
    elif tag != title:
        title = f'{title}{key}'
        if tag == title:
            return True
        else:
            return False


# write all duplicate data to file_data
def dup_data(infile, key=''):
    count_dup = 0
    count = 1
    count_write = 0
    file_name = infile.replace('.json', '')

    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_dup', 'w') as outfile:
            for obj in file:
                if len(obj['tags']) == 1:
                    if is_dup(obj, key) is True:
                        outfile.write(obj)

                        # json.dump(obj, outfile, indent=2, ensure_ascii=False)
                        count_dup += 1
                print('done line {0}'.format(count))
                count += 1
            outfile.write(f'{count_dup}')
            print(f"there are {count_dup} duplicates")
            print(f'wrote to {file_name}_dup')


# write all bad data to file_bad
def bad_data(infile, bad_key=None, dup_key=None):
    count_dup = 0
    count_line = 1
    count_write = 0
    count_bad = 0
    file_name = infile.replace('.json', '')

    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_bad', 'w') as outfile:
            for obj in file:
                if is_bad_dantri(obj, bad_key):
                    outfile.write(obj)
                    # json.dump(obj, outfile, indent=2, ensure_ascii=False)
                    count_bad += 1
                elif len(obj['tags']) == 1:
                    if is_dup(obj, dup_key):
                        outfile.write(obj)
                        # json.dump(obj, outfile, indent=2, ensure_ascii=False)
                        count_dup += 1
                print(f'done line {count_line}')
                count_line += 1
            outfile.write(f'\nthere are {count_bad} bad titles\nthere are {count_dup} duplicates')
            print(f"there are {count_bad} bad titles")
            print(f"there are {count_dup} duplicates")
            print(f'wrote to {file_name}_bad')


# don't pick any data that contain with '- VnExpress Đời sống'
def get_data_vnn(infile, bad_tag_list, english_key=''):
    count_line = 1

    file_name = infile.replace('.json', '')
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_data', 'w') as outfile:
            for obj in file:
                if len(obj['tags']) > 1:
                    new_obj = {}
                    tags = obj['tags']
                    new_obj['tags'] = []
                    for tag in tags:
                        if tag not in bad_tag_list:
                            new_obj['tags'].append(tag)

                    new_obj['title'] = obj.get('title')
                    outfile.write(obj)
                    # json.dump(new_obj, outfile, indent=2, ensure_ascii=False)

                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {file_name}_data')


def get_data_vnexpress(infile, bad_tag_list):
    count_line = 1

    file_name = infile.replace('.json', '')
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_data', 'w') as outfile:
            for obj in file:
                if len(obj['tags']) > 1:
                    new_obj = {}
                    tags = obj['tags']
                    new_obj['tags'] = []
                    for tag in tags:
                        if tag not in bad_tag_list:
                            new_obj['tags'].append(tag)

                    new_obj['title'] = obj.get('title')
                    outfile.write(obj)
                    # json.dump(new_obj, outfile, indent=2, ensure_ascii=False)

                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {file_name}_data')

