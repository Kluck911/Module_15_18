def get_filename():
    name = input(f"Введите имя открываемого файла: ")
    return name + '.txt'

def clean_text(text):
    list_text = text
    for i in range(len(text)):
        if (list_text[i].isalpha() == False) and list_text[i] != ' ':
            text = text.replace(list_text[i], ' ')
    return text.lower()


def filer_less_3_letter(word_)





with open(get_filename(), encoding='utf8') as f:
    line = clean_text(f.read()).split()
    print(line)

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

