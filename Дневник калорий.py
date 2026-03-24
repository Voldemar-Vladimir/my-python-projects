import csv,os
from datetime import date, timedelta
from time import sleep
from colorama import Fore,init
import matplotlib.pyplot as plt
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
def show_sum_week():
    try:
        show_graph()
        time_week=date.today()-timedelta(days=7)
        sum_cal=0
        for i in listcsv:
            if str(time_week)<=i["Дата"]<=str(date.today()):
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

def remove_csv():
    print(Fore.CYAN)
    otvet=input("Введите << ОГУРЧИК >> для подтверждения удаления: ")
    if otvet=="ОГУРЧИК":
        global listcsv
        listcsv=[]
        save()
        print("Успешно удалено")
        sleep(1)
    else:
        print(Fore.MAGENTA)
        print("Успешная отмена")
        sleep(1)
def calc_calories():
    while True:
        try:
            print(Fore.GREEN)
            MW=input("Введите пол: М или Ж\nВведите пол: ")
            if MW not in ("М", "Ж", "M"):
                print(Fore.RED + "Неверно указан пол")
                sleep(1)
                continue
            M=float(input("Введите вес: "))
            H=float(input("Введите рост: "))
            age=int(input("Введите возраст: "))
            A=float(input("1.1---Без активности , 1.2---минимальная активность ,\n1.375---от 1 до 3 тренеровок в неделю ,\n1.55---от 3 до 5 тренеровок в неделю, \n1.725---6 или 7 тренеровок в неделю\n1.9---экстримальная активность\nВыберите от 1.1 до 1.9\nВведите свой коэфициэнт активности: "))
            if MW=="М" or MW=="M":
                bmr = 10 * M + 6.25 * H - 5 * age + 5
            elif MW=="Ж":
                bmr = 10 * M + 6.25 * H - 5 * age - 161
            else:
                print(Fore.RED)
                print("Неверно указан пол")
            print(f"Калории для поддержания формы: {int(bmr*A)}")
            print(f"Калории для похудения(дифицита 15%): {int(bmr*A*0.85)}")
            print(f"Калории для набора(профицита 15%): {int(bmr*A*1.15)}")
            sleep(2.5)
            break
        except ValueError:
            print(Fore.RED)
            print("Ошибка ввода")
            sleep(0.7)
def show_graph():
    dates = []
    calories = []
    time_week = date.today() - timedelta(days=7)
    daily_calories = {}
    for i in listcsv:
        if str(time_week) <= i["Дата"] <= str(date.today()):
            date_str = i["Дата"]
            cal = float(i["Калорийность"])
            daily_calories[date_str] = daily_calories.get(date_str, 0) + cal
    for date_str in sorted(daily_calories.keys()):
        dates.append(date_str)
        calories.append(daily_calories[date_str])
    plt.plot(dates, calories, marker='o')
    plt.title('Калории за неделю')
    plt.xlabel('Дата')
    plt.ylabel('Калории')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
load()
def menu():
    while True:
        sleep(0.5)
        try:
            print(Fore.YELLOW)
            otvet=int(input("1. Добавить запись\n2. Посмотреть записи\n3. Сумма калорий сегодня\n4. Сколько нужно калорий?\n5. Калории за неделю\n6. Удалить данные\n7. Сохранить и выйти\nВведите цифру: "))
            if otvet==1:
                new_eat()
            elif otvet==2:
                show_all()
            elif otvet==3:
                show_sum()
            elif otvet==4:
                calc_calories()
            elif otvet==5:
                show_sum_week()
            elif otvet==6:
                remove_csv()
            elif otvet==7:
                save()
                break
            else:
                print(Fore.MAGENTA)
                print("!!! Введите цифру от 1 до 6 !!!")
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