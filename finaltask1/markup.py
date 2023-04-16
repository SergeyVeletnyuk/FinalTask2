markup_file = r'/Users/sergejveletnuk/Desktop/final work/markup.txt'


def append_mark(markup_file):
    mark = input('Добавьте заметку: ')
    with open(markup_file, 'a', encoding="utf-8") as f:
        f.write(f'\n{mark}')
    print ('Заметка добавлена')
 
    
def read_file(markup_file):
    with open(markup_file, 'r', encoding="utf-8") as f:
        print(f.read())

def search_mark(markup_file):
    search_by = input("Поиск по ключевому слову: ")
    with open(markup_file, 'r', encoding="utf-8") as f:
        for line in f:
            if search_by in line:
                print(line)
        

def delete_mark():
    f = open("markup.txt","r")
    lines = f.read()
    print(lines)
    mark = input('Введите заметку которую хотите удалить:-->')
    f = open("markup.txt","r")
    lines = f.readlines()
    if mark != '':
        f = open("markup.txt","w")
        for line in lines:
            if line.find(mark) == -1:
            # if line!= mark +"\n":
                f.write(line)
    print('заметка удалена!')
        
    
       
            


def change_mark():
    with open ('markup.txt', 'r') as f:
        old_data = f.read()
        print(old_data)
    new_data = old_data.replace(input('Искать заметку '), input('введите на что вы хотите заменить -->'))
    print('Готово!')
    with open ('markup.txt', 'w') as f:
        f.write(new_data)
        print(new_data)
    print ('Добро пожаловать!',
        '\n1) Вывести все заметки',
        '\n2) Добавить заметку',
        '\n3) Найти заметку по ключевым словам',
        '\n4) Удалить заметку',
        '\n5) Заменить заметку')


def marks_action():
    print ('Добро пожаловать!',
        '\n1) Вывести все заметки',
        '\n2) Добавить заметку',
        '\n3) Найти заметку по ключевым словам',
        '\n4) Удалить заметку',
        '\n5) Заменить заметку')
    while (input1:= int(input('Выберите действие с заметками (0 = выход):'))) != 0:
        if input1 == 1:
            read_file(markup_file)
        elif input1 == 2:
            append_mark(markup_file)
        elif input1 == 3:
            search_mark(markup_file)
        elif input1 == 4:
            delete_mark()
        elif input1 == 5:
            change_mark()
        else:
            print("Некорректный ввод")

marks_action()
