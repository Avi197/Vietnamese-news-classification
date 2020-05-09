
file = 'H:/Vietnamese word representations/Text_classification_data/Tuoitre/Tuoitre_classification_data'
file_clean = 'H:/Vietnamese word representations/Text_classification_data/Tuoitre/Tuoitre_classification_data_no_noname'

bad_words = ['Noname']

with open(file, encoding='utf-8') as infile, open(file_clean, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if not any(bad_word in line for bad_word in bad_words):
            outfile.write(line)

