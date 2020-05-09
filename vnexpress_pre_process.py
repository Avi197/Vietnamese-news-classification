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
Vnn has english titles, which we don't need
some tags are irrelevant to the title, e.g: vnn, vietnamnetvn doc bao,.... which is just to mark
the news source (???) 
some title are just 1 general text but with lots of usable tags, remove them
"""


"""
remove english news
remove all bad tags in bad_tags list
remove bad title
check if len(tags)>0
"""


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
                if len(obj['tags']) > 0
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