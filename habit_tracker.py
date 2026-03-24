import json
import datetime
habits=[]
def load_data():
    try:
        with open("habit.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
habits = load_data()

def add_t():
    id=len(habits)+1
    name=input("Введите название привычки: ")
    created=datetime.date.today().isoformat()
    load=[]
    habit={"номер":id, "имя":name, "дата создания":created, "даты выполнения":load}
    habits.append(habit)
    save_t(habits)
def metka_t():
    number=int(input("Введите номер привычки: "))
    new=datetime.date.today().isoformat()
    for habit in habits:
        if habit["номер"] == number:
            habit["даты выполнения"].append(new)
            break
    save_t(habits)
def menu():
        otvet=input("1. Добавить привычку\n2. Отметить привычку выполненной\n3. Показать все привычки со статусом на сегодня\nВыйти (с сохранением)\nЧто хотите сделать?\nУкажите номер: ")
        if otvet=="1":
            add_t()
        elif otvet=="2":
            metka_t()
        elif otvet=="3":
            print(habits)
        elif otvet=="4":
            save_t(habits)
            exit()
        else:
            menu()
def save_t(habits):
    with open("habit.json","w", encoding="utf-8") as f:
        json.dump(habits, f, ensure_ascii=False, indent=4)
while True:
    menu()