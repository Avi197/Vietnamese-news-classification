import jsonlines
import json
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
    # if title in key:
    #     return True
    if key is not None:
        return title in key


def clean_data(infile, key='', dup_key=None):

    count_dup = 0
    count = 1
    count_write = 0

    with jsonlines.open(f'{infile}.json') as file:
        with open(f'{infile}_clean', 'w', encoding='utf-8') as outfile:
            for obj in file:
                if len(obj['tags']) == 1:
                    if not is_dup(obj, key):
                        json.dump(obj, outfile, indent=2, ensure_ascii=False)
                elif not is_bad(obj, dup_key):
                    json.dump(obj, outfile, indent=2, ensure_ascii=False)

                print('done line {0}'.format(count))
                count += 1
            outfile.write(f'{count_dup}')
            print(f"there are {count_dup} duplicates")


def clean_bad_data():
    return


clean_data(Vnexpress, vnexpress_key)
# dup_data(Thanhnien)
