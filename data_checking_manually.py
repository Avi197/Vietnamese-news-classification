import jsonlines
import json
import os.path


"""
write bad data, dup data, just title/ tags to a new file
manually checking for some faulty data that might affect the outcome
"""


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


# check if tags appear in title
# for Dantri only
# Dantri has lots of title with wrong tags
def is_bad(obj, key=None):
    title = obj['title']
    title = title.strip()
    if key is not None:
        return title in key


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


bad_data(Dantri)
