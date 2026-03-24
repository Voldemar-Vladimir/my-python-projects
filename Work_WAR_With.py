from colorama import Fore
from random import choice
def color():
    colors=["GREEN","BLUE","RED","YELLOW","MAGENTA"]
    color=choice(colors)
    if color=="GREEN":
        print(Fore.GREEN)
    elif color=="BLUE":
        print(Fore.BLUE)
    elif color=="RED":
        print(Fore.RED)
    elif color=="YELLOW":
        print(Fore.YELLOW)
    elif color=="MAGENTA":
        print(Fore.MAGENTA)

def baza():
    color()
    try:
        name=input("Введите имя: ")
        age=int(input("Введите возраст: "))
        ballance=float(input("Введите баланс в рублях: "))
        work_money=float(input("Введите зарплату: "))

        with open("test.txt", "a") as f:
            f.write(f"имя = {name} | возраст = {age} лет | баланс = {ballance} р. | Зарплата = {work_money} р.\n")
    except TypeError:
        color()
        print("Ошибка при вводе данных")
        baza()

    except ValueError:
        color()
        print("Ошибка при вводе данных")
        baza()

    finally:
        color()
        print("Все данные:")
        with open("test.txt","r") as f:
            for k in f:
                print(k)
baza()