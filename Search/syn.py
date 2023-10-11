import os
 
# Указываем путь к директории
directory = "Synonymss"
 
# Получаем список файлов
files = os.listdir(directory)


def is_okay(word_list):
    for word in word_list:
        word_amount = len(word.split())
        if word_amount != 1 or len(word) <= 2 or len(word_list) < 4:
            return False
    return True


with open('synonyms.txt', mode='w', encoding='utf-8') as output_file:

    for file in files:
        with open(directory + '\\' + file, encoding='utf-8') as current_file:

            data = current_file.readlines()

            for line in data:
                string = line.strip()
                string = string.replace(",[", ", ").replace("[", "").replace("]", "")
                string = string.replace("'", "")
                word_list = string.split(", ")
                word_list = [word.lower() for word in word_list]
                if is_okay(word_list):
                    print(*word_list, sep=', ', file=output_file)