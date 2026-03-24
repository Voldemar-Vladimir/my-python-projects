from datetime import datetime, date, timedelta
from colorama import Fore
import json
from pathlib import Path
events=[]
def load():
    file = Path("events.json")
    if file.exists():
        with open("events.json","r", encoding="utf-8") as f:
            for i in f:
                events.append(i)
    else:
        print("Файла нет")
def new_event():
    try:
        print(Fore.CYAN)
        name_event = input("Введите название события: ")
        data_event = input("Введите дату события\nв формате ДД.ММ.ГГГГ : ")
        data_event = datetime.strptime(data_event, "%d.%m.%Y")
        events.append({"name":name_event, "date":data_event})
    except:
        print(Fore.RED)
        return "ПОТРАЧЕНО"
def view_events():
    try:
        print(events)
    except:
       print(Fore.RED)
       return "ПОТРАЧЕНО"
def view_days():
    name = input("Введите название события: ")
    found = False
    for event in events:
        if event['name'] == name:
            delta = event['date'] - datetime.now()
            days = delta.days
            if days > 0:
                print(f"До события {days} дней")
            elif days == 0:
                print("Событие сегодня!")
            else:
                print(f"Событие было {-days} дней назад")
            found = True
            break  # нашли — можно выйти из цикла
    if not found:
        print(Fore.RED + "ПОТРАЧЕНО")
def menu():
        print(Fore.GREEN)
        otvet=int(input("1. Добавить\n2. Посмотреть все\n3. Посмотреть сколько осталось\n4. Выйти (с сохранением)\nЧто хотите сделать?\nУкажите номер: "))
        if otvet==1:
            new_event()
        elif otvet==2:
            view_events()
        elif otvet==3:
            view_days()
        elif otvet==4:
            exit()
        else:
            menu()
while True:
    try:
        menu()
    except:
        break
if __name__=="__main__":
    pass