import jsonlines
import json
from langdetect import detect
import re
import os.path


"""
some records have 1 tag, which is also in bad_tag_list
some records have tag that is a link
"""


Tuoitre = '"H:/Vietnamese word representations/Text_classification_data/Tuoitre/Tuoitre.json"'
Vnexpress = 'H:/Vietnamese word representations/Text_classification_data/Vnexpress/Vnexpress.json'
Thanhnien = 'H:/Vietnamese word representations/Text_classification_data/Thanhnien/Thanhnien.json'
Dantri = 'H:/Vietnamese word representations/Text_classification_data/Dantri/Dantri.json'
Vnn = 'H:/Vietnamese word representations/Text_classification_data/Vnn/Vnn.json'
Vtv = 'H:/Vietnamese word representations/Text_classification_data/Vtv/Vtv.json'


tuoitre_bad_title = ['Noname']

vnn_bad_tags = ['vnn', 'vietnamnet', 'vietnamnetvn', 'vietnamnetvn doc bao', 'vietnamnet.vn',
                'tin nong', 'tin moi', 'doc bao']
vnn_english = 'news'
vnn_bad_title = ['Những hình ảnh ấn tượng trong tuần', 'Bản tin thời sự VTV', 'http://']

"""
many tags are just copy of the titles, some time add an extra string - VnExpress Đời sống
some tags are just copy of the titles, but randomly split into smaller string and then add - VnExpress Đời sống to the last smaller string, and those smaller string become tags for the title
some title are just broken, contain half a word, or a single character, ...
titles are cut off after '-', good thing they leave a ' ' space character so we can filter them out
"""


"""

"""


# return true if tag is the same as title
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


# clean up data
# write to file_data
def get_data_vnexpress(infile, bad_tag_list, bad_title_list, english_keys=''):
    count_line = 1

    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_data', 'w') as outfile:
            for obj in file:
                if len(obj['tags']) > 0:
                    if not obj['title'].endswith(' '):
                        outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {file_name}_data')


def get_dash_title(infile):
    count_line = 1
    count_1_tag = 0
    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_dash_title', 'w') as outfile:
            for obj in file:
                # if low < len(obj['title']) < high:
                if not obj['title'].endswith(' '):
                    outfile.write(obj['title'])
                print(f'done line {count_line}')
                count_line += 1