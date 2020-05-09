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

vnexpress_bad_tag = '- VnExpress Đời sống'


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


# check if tags contain '- VnExpress Đời sống'
# return True if tag is bad
def check_bad_tags(obj, bad_tags='- VnExpress Đời sống'):
    tags = obj['tags']
    if bad_tags is not None:
        for tag in tags:
            return bad_tags in tag


# write all bad data to file_bad
def bad_data(infile, bad_key=None, dup_key=None):
    count_dup = 0
    count_line = 1
    count_write = 0
    count_bad = 0
    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_bad', 'w') as outfile:
            for obj in file:
                if check_bad_tags(obj, bad_key):
                    outfile.write(obj)
                    count_bad += 1
                elif len(obj['tags']) == 1:
                    if is_dup(obj, dup_key):
                        outfile.write(obj)
                        count_dup += 1
                print(f'done line {count_line}')
                count_line += 1
            outfile.write(f'\nthere are {count_bad} bad titles\nthere are {count_dup} duplicates')
            print(f"there are {count_bad} bad titles")
            print(f"there are {count_dup} duplicates")
            print(f'wrote to {file_name}_bad')


def get_title_vnexpress(infile):
    count_line = 1
    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_data', 'w') as outfile:
            for obj in file:
                if len(obj['tags']) > 0:
                    new_obj = {}
                    tags = obj['tags']
                    new_obj['tags'] = tags
                    new_obj['title'] = obj.get('title')
                    outfile.write(new_obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {file_name}_data')
