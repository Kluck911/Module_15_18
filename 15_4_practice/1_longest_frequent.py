alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

'получаем имя файла'


def get_filename():
    fileName = input(f"Введите имя открываемого файла: ")

    return fileName + '.txt'


'очищаем список от символов'


def filter_clean(list_):
    list_text = list_

    'заменяем все символы кроме букв на пробелы'
    for pos in range(len(list_)):
        if not list_text[pos].isalpha():
            list_ = list_.replace(list_text[pos], ' ')
    'переводим в один регистр, чтобы слова воспринимались одинаково с буквами в разных регистрах'
    return list_.lower()


'список самых длинных слов'


def longest_word(list_):
    listEN = []
    list_en_filter = []
    'создаем список из английских слов'
    for word_ in list_:
        'проверка, является ли слово английским'
        if word_is_en(word_):
            listEN.append(word_)
    'сортируем от большего к меньшему'
    listEN = sorted(listEN, key=len)[::-1]
    i = 0
    'записываем в список list_en_filter все элементы списка начиная с нулевого с одинаковой длинной (все самые длинные слова)'
    list_en_filter.append(listEN[i])
    while len(listEN[i]) == len(listEN[i + 1]):
        if listEN[i + 1] not in list_en_filter:
            list_en_filter.append(listEN[i + 1])
        i += 1

    return list_en_filter


def word_is_en(word_):
    for i in range(0, len(word_)):
        for char in word_[i]:
            if char not in alphabet:
                return False

    return True


def often_word(list_):
    list_ = less_3_letter(list_)
    mostOften = []
    countWord = 0

    for word in list_:
        tempCountWord = list_.count(word)
        if tempCountWord > countWord:
            countWord = tempCountWord
            mostOften = [word]
        elif tempCountWord == countWord:
            mostOften.append(word)

    return list(set(mostOften))


def less_3_letter(list_):
    sortList = []

    for word_ in list_:
        if len(word_) > 3:
            sortList.append(word_)

    return sortList


with open(get_filename(), encoding='utf8') as f:
    wordList = filter_clean(f.read()).split()
    print(wordList)
    print('Наиболее часто встречающееся слово:\n', ', '.join(often_word(wordList)))
    print('Наиболее длинное слово на английском:\n', ', '.join(longest_word(wordList)))
