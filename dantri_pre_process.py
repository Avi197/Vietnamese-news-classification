import jsonlines
import json
import re
import os.path


# f = open(os.path.dirname(__file__) + '/../data.yml')

Tuoitre = 'Tuoitre/Tuoitre'
tuoitre_key = ''
Vnexpress = 'Vnexpress/Vnexpress'
vnexpress_key = ' - VnExpress Đời sống'
Thanhnien = 'Thanhnien/Thanhnien'
thanhnien_key = ''
Dantri = 'Dantri/Dantri'
dantri_key = ''
Vnn = 'Vnn/Vnn'
Vtv = 'Vtv/Vtv'

tuoitre_bad_title = ['Noname']


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


def is_bad(obj, key=None):
    title = obj['title']
    title = title.strip()
    if key is not None:
        return title in key


def dup_data(infile, key=''):
    count_dup = 0
    count = 1
    count_write = 0
    with jsonlines.open(infile + '.json') as file:
        with open(f'{infile}_dup', 'w', encoding='utf-8') as outfile:
            for obj in file:
                if len(obj['tags']) == 1:
                    if is_dup(obj, key) is True:
                        json.dump(obj, outfile, indent=2, ensure_ascii=False)
                        count_dup += 1
                print('done line {0}'.format(count))
                count += 1
            outfile.write(f'{count_dup}')
            print(f"there are {count_dup} duplicates")


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
            outfile.write(f'\nthere are {count_bad} bad titles\nthere are {count_dup} duplicates')
            print(f"there are {count_bad} bad titles")
            print(f"there are {count_dup} duplicates")


def get_data(infile):
    count_line = 1

    with jsonlines.open(infile + '.json') as file:
        with open(f'{infile}_data_1', 'w', encoding='utf-8') as outfile:
            for obj in file:
                # tags = obj['tags']
                if len(obj['tags']) > 0:
                    json.dump(obj, outfile, indent=1, ensure_ascii=False)

                print('done line {0}'.format(count_line))
                count_line += 1


def get_tags(infile):
    count_line = 1
    clean_tags = []
    with jsonlines.open(infile + '.json') as file:
        with open(f'{infile}_data_1', 'w', encoding='utf-8') as outfile:
            for obj in file:
                if len(obj['tags']) > 1:
                    new_obj = {}
                    tags = obj.get('tags')
                    new_obj['tags'] = []
                    # print(tags)
                    for tag in tags:
                        t = tag.get('text')
                        # print(t)
                        new_obj['tags'].append(t)
                    new_obj['title'] = obj.get('title')
                    json.dump(new_obj, outfile, indent=2, ensure_ascii=False)

                print('done line {0}'.format(count_line))
                count_line += 1


def what_the_fuck_is_wrong_with_this_shit(infile):
    count_line = 1
    count_write = 0
    clean_tags = []
    with jsonlines.open(infile + '.json') as file:
        with open(f'{infile}_tag_in_title', 'w', encoding='utf-8') as outfile:
            with open(f'{infile}_tag_not_in_title', 'w', encoding='utf-8') as outfile2:
                for obj in file:
                    if len(obj['tags']) > 1:
                        dump_it = False
                        new_obj = {}
                        tags = obj.get('tags')
                        new_obj['tags'] = []
                        new_obj['title'] = obj.get('title')
                        for tag in tags:
                            t = tag.get('text')
                            new_obj['tags'].append(t)
                            if t in new_obj['title']:
                                dump_it = True
                                print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

                        if dump_it:
                            json.dump(new_obj, outfile, indent=2, ensure_ascii=False)
                            count_write += 1
                        else:
                            json.dump(new_obj, outfile2, indent=2, ensure_ascii=False)
                    print(f'done line {count_line}')
                    count_line += 1
                print(f'dump {count_write} objects')


what_the_fuck_is_wrong_with_this_shit(Dantri)
