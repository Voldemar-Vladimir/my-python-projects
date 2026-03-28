from colorama import Fore
import time
from datetime import datetime
def add_note():
    print(Fore.CYAN)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_note=input("Новая запись: ")
    time.sleep(1)
    with open("notes.txt", "a") as f:
        f.write(f"{current_time}\n{new_note}\n")
        print(Fore.GREEN)
        print("Успешное добавление")
        time.sleep(1)
def show_notes():
    try:
        with open("notes.txt","r") as f:
            for s in f:
                time.sleep(0.1)
                print(s)
    except:
        print("Заметок пока нет")
        time.sleep(1)
    finally:
        pass
def clear_notes():
    print(Fore.CYAN)
    pdtvr=input("Ответьте ДА если хотите очистить\nОчистить?\n: ")
    time.sleep(1)
    if pdtvr.upper() == "ДА":
        with open("notes.txt","w") as f:
            f.write("")
            print(Fore.GREEN)
            print("Успешное удаление")
            time.sleep(1)
def menu():
    while True:
        time.sleep(1)
        try:
            print(Fore.CYAN)
            time.sleep(1)
            otvet=int(input("1. Новая запись\n2. Посмотреть заметки\n3. Удалить заметки\n4. Сохранить и выйти\nВведите цифру: "))
            if otvet==1:
                add_note()
            elif otvet==2:
                show_notes()
            elif otvet==3:
                clear_notes()
            elif otvet==4:
                break
            else:
                print(Fore.MAGENTA)
                print("Вводите цифры от 1 до 4")
                time.sleep(1)
        except ValueError:
            print(Fore.RED)
            print("Ошибка ввода")
            time.sleep(1)
        except Exception as e:
            print(Fore.RED)
            print(f"Ошибка: {e}")
            time.sleep(1)
if __name__=="__main__":
    menu()