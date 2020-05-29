import jsonlines
import json
from langdetect import detect
import re
import os.path

Vnn = 'H:/Vietnamese word representations/Raw news data (no dupplicate)/word_vectors/vnn.json'
Vnn_data = 'H:/Vietnamese word representations/Word_vector_data/Vnn/vnn_data.json'

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


# check if title is in bad_title list
def check_bad_title(obj, bad_title_list=None):
    title = obj['title']
    title = title.strip()
    if bad_title_list is not None:
        count = 0
        for bad_title in bad_title_list:
            if bad_title in title:
                count += 1
        return count > 0


def check_english(tags, english_keys):
    for tag in tags:
        count = 0
        if english_keys not in tag:
            count += 1
        if count == 0:
            return True


# clean up data
# write to file_data
# get only tags and title from raw json
# also get rid of some bad tags
# this one is for vnn only
# Vnn has some tags that are irrelevant
# e.g: vnn, vietnamnet, ...
def get_data_vnn(infile, bad_title_list, english_keys=''):
    count_line = 1

    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(Vnn_data, 'w') as outfile:
            for obj in file:
                title = obj['title']
                if detect(title) == 'vi':
                    if not check_bad_title(obj, bad_title_list):
                        outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {Vnn_data}')


get_data_vnn(Vnn, bad_title_list=vnn_bad_title)


#


#


#


#


#


# TESTING SECTION
# ------------------------------------------------------------------------------------------------------
# get_data_vnn(Vnn, vnn_bad_tags)

# name = Vnn.replace('.json', '')
# name = f'{name}_data'
# remove_english_news(f'{name}_data', vnn_english)
# Vnn_vi = 'H:/Vietnamese word representations/Text_classification_data/Vnn/Vnn_vi_1'

# check_english_news(Vnn, vnn_english)
# check_vi_news(Vnn, vnn_english)


# 1
# remove_english_news(Vnn, vnn_english)

# 2
# remove_english_news(Vnn, vnn_english, '3')


# QUARANTINE SECTION
# PURPOSE UNKNOWN
# ------------------------------------------------------------------------------------------------------
# # Vnn has some english news
# # what for?
# def remove_english_news(infile, english_keys, num=''):
#     count_line = 1
#
#     if 'json' in infile:
#         file_name = infile.replace('.json', '')
#     else:
#         file_name = infile
#     with jsonlines.open(infile) as file:
#         with jsonlines.open(f'{file_name}_no_english_{num}', 'w') as outfile:
#             for obj in file:
#                 tags = obj['tags']
#                 title = obj['title']
#                 if not check_english(tags, english_keys):
#                     if detect(title) == 'vi':
#                         outfile.write(obj)
#                 # title = obj['title']
#                 # if detect(title) != 'en':
#                 #     outfile.write(obj)
#                     # json.dump(obj, outfile, indent=2, ensure_ascii=False)
#
#                 print(f'done line {count_line}')
#                 count_line += 1
#             print(f'wrote to {file_name}_no_english')
#
#
# def check_vi_news(infile, num=''):
#     count_line = 1
#
#     if 'json' in infile:
#         file_name = infile.replace('.json', '')
#     else:
#         file_name = infile
#     with jsonlines.open(infile) as file:
#         with jsonlines.open(f'{file_name}_vi_{num}', mode='w') as outfile:
#             for obj in file:
#                 title = obj['title']
#                 if detect(title) == 'vi':
#                     outfile.write(obj)
#                 print(f'done line {count_line}')
#                 count_line += 1
#             print(f'wrote to {file_name}_vi')
#
#
# def check_english_news(infile, english_keys):
#     count_line = 1
#     if 'json' in infile:
#         file_name = infile.replace('.json', '')
#     else:
#         file_name = infile
#     with jsonlines.open(infile) as file:
#         with jsonlines.open(f'{file_name}_english', mode='w') as outfile:
#             for obj in file:
#                 title = obj['title']
#                 if detect(title) == 'en':
#                     outfile.write(obj)
#                     # json.dump(obj, outfile, indent=2, ensure_ascii=False)
#
#                 print(f'done line {count_line}')
#                 count_line += 1
#             print(f'wrote to {file_name}_english')
# --------------------------------------------------------------------------------------------------------




