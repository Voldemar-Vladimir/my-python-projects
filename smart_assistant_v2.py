from password import pasgen as generator_password, pasinfo as info_password
from analizatorSTR import g_str, len_str, set_str
from notes import add_note, show_notes, clear_notes
import time
from colorama import Fore, Back, Style, init
def menu():
    while True:
        print(Fore.WHITE)
        time.sleep(0.5)
        choise=input("Впишите номер: \n1. Заметки\n2. Генератор паролей\n3. Анализатор текста\n4. Выход\nВаш выбор: ")
        if choise=="1":
            time.sleep(0.5)
            notes_asistant()
        elif choise=="2":
            time.sleep(0.5)
            generator_password()
        elif choise=="3":
            time.sleep(0.5)
            info_str()
        elif choise=="4":
            break
        else:
            menu()
def notes_asistant():
    print(Fore.MAGENTA)
    time.sleep(0.5)
    otvet=input("Что хотите сделать?\n1.Добавить заметку\n2.Прочитать заметки\n3.Удалить заметки\n: ")
    if otvet == "1":
        time.sleep(0.5)
        add_note()
    elif otvet == "2":
        time.sleep(0.5)
        show_notes()
    elif otvet == "3":
        time.sleep(0.5)
        clear_notes()
    else:
        menu()
def info_str():
    print(Fore.CYAN)
    time.sleep(0.5)
    l=input("Введите строку: ")
    a=len_str(l)
    b=set_str(l)
    c=g_str(l)
    time.sleep(0.5)
    return print(f'\nДлинна строки: {a}\n{b}\n{c}\n')
if __name__=="__main__":
    menu()