import re
import nltk
from nltk.corpus import stopwords
from pprint import pprint
import os


def remove_stopwords(text):
    stop_words = stopwords.words('spanish')
    stop_words_capitalized = [word.capitalize() for word in stop_words]
    words = [w for w in text.split(' ') if not w in stop_words]
    words = [w for w in words if not w in stop_words_capitalized]
    return ' '.join(words)


def remove_3_char_words(text):
    words = [w for w in text.split(' ') if len(w) > 3]
    return ' '.join(words)


raw_texts = os.listdir('raw_texts')
main_word_list = []
for text in raw_texts:
    with open(os.path.join('raw_texts', text), 'r', encoding="utf8") as text_file:
        data = text_file.read()
    a, b = "áéíóúÁÉÍÓÚ", "aeiouAEIOU"
    trans = str.maketrans(a, b)
    new_string = data.translate(trans)
    letters_regex = r"[^a-zñA-ZÑ]"
    new_string = re.sub(letters_regex, " ", new_string)

    new_string = remove_stopwords(new_string)
    new_string = remove_3_char_words(new_string)
    word_list = [w.lower() for w in new_string.split()]
    main_word_list.extend(word_list)

with open('words_list.txt', 'w', encoding="utf8") as file:
    file.write('\n'.join(set(main_word_list)))
