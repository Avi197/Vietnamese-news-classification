import jsonlines
import json
import os.path


"""
write bad data, dup data, just title/ tags to a new file
manually checking for some faulty data that might affect the outcome
"""


Tuoitre = '"H:/Vietnamese word representations/Text_classification_data/Tuoitre/Tuoitre.json"'
Vnexpress = 'H:/Vietnamese word representations/Text_classification_data/Vnexpress/Vnexpress.json'
Thanhnien = 'H:/Vietnamese word representations/Text_classification_data/Thanhnien/Thanhnien.json'
Dantri = 'H:/Vietnamese word representations/Text_classification_data/Dantri/Dantri.json'
Vnn = 'H:/Vietnamese word representations/Text_classification_data/Vnn/Vnn.json'
Vtv = 'H:/Vietnamese word representations/Text_classification_data/Vtv/Vtv.json'
Vnn_no_english = 'H:/Vietnamese word representations/Text_classification_data/Vnn/Vnn_no_english'
Vnn_data = 'H:/Vietnamese word representations/Text_classification_data/Vnn/Vnn_data'


vnn_bad_title = ['Những hình ảnh ấn tượng trong tuần', 'Bản tin thời sự VTV', 'http']


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


# check if tags appear in title
# for Dantri only
# Dantri has lots of title with wrong tags
def is_bad(obj, key=None):
    title = obj['title']
    title = title.strip()
    if key is not None:
        return title in key


def check_bad_title(obj, bad_title_list=None):
    title = obj['title']
    title = title.strip()
    if bad_title_list is not None:
        count = 0
        for bad_title in bad_title_list:
            if bad_title in title:
                count += 1
        return count > 0


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
                if is_bad(obj, bad_key):
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


def get_data_with_1_tag(infile):
    count_line = 1
    count_1_tag = 0
    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_1_tag', 'w') as outfile:
            for obj in file:
                if len(obj['tags']) == 1:
                    outfile.write(obj)
                    count_1_tag += 1
                print(f'done line {count_line}')
                count_line += 1
            outfile.write(f'\n there are {count_1_tag} records with 1 tag')
            print(f'there are {count_1_tag} records with 1 tag')
            print(f'wrote to {file_name}_1_tag')


def get_only_title(infile):
    count_line = 1
    count_1_tag = 0
    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_title', 'w') as outfile:
            for obj in file:
                outfile.write(obj['title'])
                print(f'done line {count_line}')
                count_line += 1


def get_bad_title(infile, bad_title_list=None):
    count_line = 1
    count_1_tag = 0
    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_bad_title', 'w') as outfile:
            for obj in file:
                if check_bad_title(obj, bad_title_list):
                    print('aaaaaaaaaaaaaaaaaaaaaa')
                    outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1


def get_short_title(infile, low, high):
    count_line = 1
    count_1_tag = 0
    if 'json' in infile:
        file_name = infile.replace('.json', '')
    else:
        file_name = infile
    with jsonlines.open(infile) as file:
        with jsonlines.open(f'{file_name}_short_title', 'w') as outfile:
            for obj in file:
                if low < len(obj['title']) < high:
                    outfile.write(obj['title'])
                print(f'done line {count_line}')
                count_line += 1


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


# get_data_with_1_tag(Vnn_data)
# get_only_title(Vnn_data)

# test = 'H:/Vietnamese word representations/Text_classification_data/Vnn/test'
#
# get_bad_title(test, vnn_bad_title)

# text = 'http://gamesao.vietnamnet.vn/giai-tri/nhung-em-be-noi-tieng-dang-so-nhat-trong-phim-kinh-di-17821.html'
#
# print('http://' in text)


# get_only_title(Vnexpress)
# get_short_title(Vnexpress, 20, 30)
# get_dash_title(Vnexpress)
get_bad_title(Vnn)
"""
Putin 
F

"""


