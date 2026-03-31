import sqlite3,time
from datetime import datetime
from colorama import Fore
conn=sqlite3.connect("notes.db")
cur=conn.cursor()
def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT,
        created_at TEXT              
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE             
    )
    """)
    try:
        cur.execute("""ALTER TABLE notes ADD COLUMN user_id INTEGER REFERENCES users(id);""")
        conn.commit()
    except:
        pass
def add_note():
    try:
        cur.execute("""SELECT id,name FROM users;""")
        row=cur.fetchall()
        print(row)
        while True:
            print(Fore.CYAN)
            otvet=int(input("1. Добавить пользователя\n2. Выбрать пользователя по id\n3. Выйти\nВедите цифру: "))
            if otvet==1:
                print(Fore.BLUE)
                name_user=input("Введите имя: ")
                cur.execute("""INSERT INTO users (name) VALUES (?)""",(name_user,))
                conn.commit()
            elif otvet==2:
                cur.execute("""SELECT id,name FROM users;""")
                row=cur.fetchall()
                print(row)
                print(Fore.BLUE)
                number_user=int(input("Введите свой id: "))
                cur.execute("SELECT id FROM users WHERE id = ?", (number_user,))
                exists = cur.fetchone()
                if exists==None:
                    print(Fore.MAGENTA)
                    print("Вводите id правильно")
                    continue
                a=input("Введите заголовок: ")
                b=input("Введите текст: ")
                c=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cur.execute("INSERT INTO notes (title, content, created_at, user_id) VALUES (?,?,?,?)", (a, b, c, number_user))
                conn.commit()
                print(Fore.GREEN)
                print("Успешное добавление")
            elif otvet==3:
                break
            else:
                print(Fore.MAGENTA)
                print("Введите цифру от 1 до 3")
    except Exception as e:
        print(Fore.RED)
        print(f"Ошибка: {e}")
def get_all_notes():
    print(Fore.BLUE)
    cur.execute("SELECT notes.id, notes.title, notes.content, notes.created_at, users.name FROM notes JOIN users ON notes.user_id = users.id")
    row=cur.fetchall()
    print(row)
def remove_all():
    print(Fore.BLUE)
    otvet=input("Введите ДА, чтоб подтвердить удаление: ")
    if otvet.upper()=="ДА":
        cur.execute("""DELETE FROM notes;""")
        conn.commit()
        print(Fore.GREEN)
        print("Успешное удаление")
    else:
        print(Fore.GREEN)
        print("Успешная отмена")
def delete_id(id):
    try:
        cur.execute("""DELETE FROM notes WHERE id=?""",(id,))
        if cur.rowcount==0:
            print(Fore.MAGENTA)
            print("Запись не найдена")
        else:
            print(Fore.GREEN)
            print("Успешное удаление")
        conn.commit()
    except Exception as e:
        print(Fore.RED)
        print(f"Ошибка: {e}")
def update_db(new_id,new_title,new_content):
    try:
        cur.execute("""UPDATE notes SET title=?,content=? WHERE id=?""",(new_title,new_content,new_id))
        if cur.rowcount==0:
            print(Fore.MAGENTA)
            print("Запись не найдена")
        else:
            print(Fore.GREEN)
            print("Успешное обновление")
        conn.commit()
    except Exception as e:
        print(Fore.RED)
        print(f"Ошибка: {e}")
def menu():
    while True:
        time.sleep(1)
        try:
            print(Fore.CYAN)
            time.sleep(1)
            otvet=int(input("1. Новая запись\n2. Посмотреть заметки\n3. Удалить заметки\n4. Удалить по id\n5. Обновить значения по id\n6. Сохранить и выйти\nВведите цифру: "))
            if otvet==1:
                add_note()
            elif otvet==2:
                get_all_notes()
            elif otvet==3:
                remove_all()
            elif otvet==4:
                id=int(input("id: "))
                delete_id(id)
            elif otvet==5:
                id=int(input("id: "))
                new_title=input("Новый заголовок: ")
                new_content=input("Новый текст: ")
                update_db(id,new_title,new_content)
            elif otvet==6:
                conn.commit()
                conn.close()
                break
            else:
                print(Fore.MAGENTA)
                print("Вводите цифры от 1 до 6")
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
    create_table()
    menu()