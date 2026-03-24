# notes.py
from datetime import datetime
def __init__():
    pass
def add_note():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_note=input("Новая запись: ")
    with open("notes.txt", "a") as f:
        f.write(f"{current_time}\n{new_note}\n")
def show_notes():
    try:
        with open("notes.txt","r") as f:
            for s in f:
                print(s)
    except:
        print("Заметок пока нет")
    finally:
        pass
def clear_notes():
    pdtvr=input("Ответьте ДА если хотите очистить\nОчистить?\n: ")
    if pdtvr.upper() == "ДА":
        with open("notes.txt","w") as f:
            f.write("")
if __name__=="__main__":
    pass