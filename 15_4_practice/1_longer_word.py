alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_filename():
    fileName = input(f"Введите имя открываемого файла: ")

    return fileName + '.txt'


def filter_clean(list_):
    list_text = list_

    for i in range(len(list_)):
        if (not list_text[i].isalpha()) and list_text[i] != ' ':
            list_ = list_.replace(list_text[i], ' ')

    return list_.lower()


def longest_word(list_):
    firstWord = ''
    listEN = []
    list_en_filter = []

    for word_ in list_:
        if word_is_en(word_):
            listEN.append(word_)
    listEN = sorted(listEN, key=len)[::-1]
    i = 0
    list_en_filter.append(listEN[i])
    while len(listEN[i]) == len(listEN[i+1]):
        if listEN[i+1] not in list_en_filter:
            list_en_filter.append(listEN[i + 1])
        i += 1

    return ', '.join(list_en_filter)




def word_is_en(word_):
    for i in range(0, len(word_)):
        for char in word_[i]:
            if char not in alphabet:
                return False

    return True


def often_word(list_):
    list_ = less_3_letter(list_)
    countFirst = 0
    wordResult = ''

    for i in range(len(list_)):
        countTemp = 0
        first_world = list_[i]
        for word_ in range(i, len(list_) - 1):
            if first_world == list_[i + 1]:
                countTemp += 1
        if countTemp > countFirst:
            wordResult = first_world

    if countFirst:
        return 'Ни одно слово не встречается более одного раза.'
    else:
        return wordResult


def less_3_letter(list_):
    sortList = []

    for word_ in list_:
        if len(word_) > 3:
            sortList.append(word_)

    return sortList


with open(get_filename(), encoding='utf8') as f:
    wordList = filter_clean(f.read()).split()
    often_word(wordList)
    print(f'Наиболее часто встречающееся слово:\n{often_word(wordList)}')
    print(f'Наиболее длинное слово на английском:\n {longest_word(wordList)}')
