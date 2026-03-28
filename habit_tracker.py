import json,time
import datetime
from colorama import Fore

def load_data():
    global habits
    habits=[]
    try:
        with open("habit.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
habits = load_data()

def add_t():
    print(Fore.BLUE)
    id=len(habits)+1
    name=input("Введите название привычки: ")
    time.sleep(0.3)
    created=datetime.date.today().isoformat()
    load=[]
    habit={"номер":id, "имя":name, "дата создания":created, "даты выполнения":load}
    habits.append(habit)
    save_t(habits)
def metka_t():
    print(Fore.BLUE)
    number=int(input("Введите номер привычки: "))
    time.sleep(0.3)
    new=datetime.date.today().isoformat()
    for habit in habits:
        time.sleep(0.2)
        if habit["номер"] == number:
            habit["даты выполнения"].append(new)
            break
    save_t(habits)
def menu():
    while True:
        time.sleep(1)
        print(Fore.CYAN)
        try:
            otvet=input("1. Добавить привычку\n2. Отметить привычку выполненной\n3. Показать все привычки со статусом на сегодня\nВыйти (с сохранением)\nЧто хотите сделать?\nУкажите номер: ")
            if otvet=="1":
                add_t()
            elif otvet=="2":
                metka_t()
            elif otvet=="3":
                print(habits)
            elif otvet=="4":
                save_t(habits)
                break
            else:
                print(Fore.MAGENTA)
                print("Вводите цифру от 1 до 4")
                time.sleep(1)
        except ValueError:
            print(Fore.RED)
            print("Ошибка ввода")
            time.sleep(1)
        except Exception as e:
            print(Fore.RED)
            print(f"Ошибка: {e}")
            time.sleep(1)
def save_t(habits):
    with open("habit.json","w", encoding="utf-8") as f:
        json.dump(habits, f, ensure_ascii=False, indent=4)
while True:
    menu()