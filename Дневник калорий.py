import csv,os
from datetime import date
from time import sleep
from colorama import Fore,init
init(autoreset=False)
listcsv=[]
def load():
    print(Fore.RED)
    global listcsv
    try:
        if not(os.path.exists("calories.csv")):
            listcsv=[]
        else:
            with open("calories.csv","r",encoding="utf-8") as f:
                reader=csv.DictReader(f)
                for row in reader:
                    listcsv.append(row)
    except Exception as e:
        print(f"Неудача, {e}\nНачинаем с нуля\n")
        listcsv=[]
def new_eat():
    while True:
        print(Fore.BLUE)
        try:
            data=date.today()
            category=input("Введите категорию еды: ")
            calories=float(input("Сколько это калорий: "))
            listcsv.append({"Дата":str(data),"Категория":category,"Калорийность":calories})
            save()
            return print("Успешно"), sleep(0.5)
        except ValueError:
            print("Ошибка ввода, попробуйте еще\n")
def save():
    with open("calories.csv","w", encoding="utf-8", newline="") as f:
        write=csv.DictWriter(f,fieldnames=["Дата","Категория","Калорийность"])
        write.writeheader()
        write.writerows(listcsv)
        sleep(0.5)
def show_all():
    print(Fore.GREEN)
    for i in listcsv:
        print(i)
        sleep(0.1)
def show_sum():
    try:
        sum_cal=0
        for i in listcsv:
            if i["Дата"]==str(date.today()):
                sum_cal+=float(i["Калорийность"])
            else:
                continue
        print(Fore.GREEN)
        print(sum_cal)
        sleep(0.5)
    except Exception as e:
        print(Fore.RED)
        print(f"Ошибка: {e}\n")
        sleep(0.5)
def remove():
    global listcsv
    listcsv=[]
    save()
load()
def menu():
    while True:
        sleep(0.5)
        try:
            print(Fore.YELLOW)
            otvet=int(input("1. Добавить запись\n2. Посмотреть записи\n3. Сумма калорий сегодня\n4. Удалить все записи\n5. Сохранить и выйти\nВведите цифру: "))
            if otvet==1:
                new_eat()
            elif otvet==2:
                show_all()
            elif otvet==3:
                show_sum()
            elif otvet==4:
                remove()
            elif otvet==5:
                save()
                break
            else:
                print(Fore.MAGENTA)
                print("!!! Введите цифру от 1 до 5 !!!")
        except ValueError:
            print(Fore.RED)
            print("Ошибка ввода\n")
            sleep(0.5)
        except Exception as e:
            print(Fore.RED)
            print(f"Ошибка: {e}\n")
            sleep(0.5)
if __name__=="__main__":
    menu()