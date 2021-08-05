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
    list_ = less_3_letter(list_)
    print(list_)
    return


def often_word(word_):
    return


def less_3_letter(list_):
    sortList = []
    for char in list_:
        if len(char) > 3:
            sortList.append(char)
    return sortList

def list_is_EN(list_):
    return


with open(get_filename(), encoding='utf8') as f:
    wordList = filter_clean(f.read()).split()
    longest_word(wordList)
    print(wordList)

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
