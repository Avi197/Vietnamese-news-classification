import jsonlines
import json
import re

from vncorenlp import VnCoreNLP
import time


# Tuoitre = 'Tuoitre/Tuoitre'
# tuoitre_key = ''
# Vnexpress = 'Vnexpress/Vnexpress'
# vnexpress_key = ' - VnExpress Đời sống'
# Thanhnien = 'Thanhnien/Thanhnien'
# thanhnien_key = ''
# Dantri = 'Dantri/Dantri'
# dantri_key = ''
# Vnn = 'Vnn/Vnn'
# Vtv = 'Vtv/Vtv'

Tuoitre = 'Tuoitre'
tuoitre_key = ''
Vnexpress = 'Vnexpress'
vnexpress_key = ' - VnExpress Đời sống'
Thanhnien = 'Thanhnien'
thanhnien_key = ''
Dantri = 'Dantri'
dantri_key = ''
Vnn = 'Vnn'
Vtv = 'Vtv'

tuoitre_bad_title = ['Noname']

# data = 'Vnexpress'
# # output = data + '_data'
# output = data + '_test'
#
# count = 0
#
# with jsonlines.open(data + '.json') as file:
#     with open(output, 'w', encoding='utf-8') as out:
#         for obj in file:
#             # tags = obj['tags']
#             if len(obj['tags']) < 2:
#                 for tag in obj['tags']:
#                     tag = tag.strip()
#                     # if len(tag) > 1:
#                     #     print("NOPE")
#                     #     for t in tag:
#                     #         label = ' '.join(t)
#                     # else:
#                     #     label = ' '.join(tag[0])
#                     label = re.sub(r' ', '-', tag)
#                     # out.write('__label__%s ' % label)
#                     out.write(f'__label__{label} ')
#                 out.write('\n')
#             print('done line {0}'.format(count))
#             count += 1

# for obj in file:
#     tags = obj['tags']
#     if tags[0]:
#         for tag in tags:
#             tag = tag.strip()
#             tag = re.sub(r' ', '-', tag)
#             print(tag)


def is_bad(obj, key=None):
    title = obj['title']
    title = title.strip()
    if key is not None:
        return title in key


def is_dup(obj, key=''):
    title = obj['title']
    tag = obj['tags'][0]
    title = title.strip()
    tag = tag.strip()
    if tag == title:
        return True
    elif tag != title:
        title = f'{title}{key}'
        return tag == title


def bad_data(infile, bad_key=None, dup_key=None):
    count_dup = 0
    count_line = 1
    count_write = 0
    count_bad = 0

    with jsonlines.open(infile + '.json') as file:
        with open(f'{infile}_bad', 'w', encoding='utf-8') as outfile:
            for obj in file:
                if is_bad(obj, bad_key):
                    json.dump(obj, outfile, indent=2, ensure_ascii=False)
                    count_bad += 1
                elif len(obj['tags']) == 1:
                    if is_dup(obj, dup_key):
                        json.dump(obj, outfile, indent=2, ensure_ascii=False)
                        count_dup += 1
                print('done line {0}'.format(count_line))
                count_line += 1
            outfile.write(f'there are {count_bad} bad titles\nthere are {count_dup} duplicates')
            print(f"there are {count_bad} bad titles\n")
            print(f"there are {count_dup} duplicates")


bad_data(Thanhnien)

# def test_is_bad(title, key=None):
#     # title = obj['title']
#     # title = title.strip()
#     if key is not None:
#         return title in key
#
#
# print(test_is_bad('concho', ['con cho', 'sucvat']))



