alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_filename():
    fileName = input(f"Введите имя открываемого файла: ")

    return fileName + '.txt'


def filter_clean(text):
    list_text = text

    for i in range(len(text)):
        if (not list_text[i].isalpha()) and list_text[i] != ' ':
            text = text.replace(list_text[i], ' ')

    return text.lower()


def longest_word(list_):
    first_word = list_[0]
    count = 0

    for char in list_:
        if len(char) > len(first_word):
            first_word = char

    return


def list_is_EN(list_):

    return


def often_word(list_):
    list_ = less_3_letter(list_)
    countFirst = 0
    wordResult = ''

    for i in range(len(list_)):
        countTemp = 0
        first_world = list_[i]
        for char in range(i, len(list_)-1):
            if first_world == list_[i+1]:
                countTemp += 1
        if countTemp > countFirst:
            wordResult = first_world

    if countFirst:
        return 'Ни одно слово не встречается более одного раза.'
    else:
        return wordResult


def less_3_letter(list_):
    sortList = []

    for char in list_:
        if len(char) > 3:
            sortList.append(char)

    return sortList



with open(get_filename(), encoding='utf8') as f:
    wordList = filter_clean(f.read()).split()
    often_word(wordList)
    print(wordList)
    print(f'Наиболее часто встречающееся слово: {often_word(wordList)}')

''''
 
    line = line.replace('!', '')
    line = line.replace(',', '')
    line = line.replace('.', '')
    print(line)
    line.split()
    print(line.split())
    for n in len(fileList):
       print(fileList[n])
         text = text.replace(" ", "")
    text = text.replace("\n", "")

'''
