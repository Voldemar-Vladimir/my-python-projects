import string, random,time
from colorama import Fore, Style, Back, init
def pasgen():
    print(Fore.BLUE)
    chars = string.ascii_letters
    print("Отвечайте 'ДА' или 'НЕТ' !!!\n")
    time.sleep(1)
    spec_s=input("Использовать спец символы?\n: ")
    if spec_s.upper() == "ДА" :
        chars += "!@#$%&*"
    else:
        pass
    num_s=input("Использовать цифры?\n: ")
    if num_s.upper() == "ДА" :
        chars += string.digits
    else:
        pass
    long=int(input("Введите длинну пароля: "))
    time.sleep(1)
    password=""
    for i in range(long):
        new=(random.choice(chars))
        while new in password:
            new=(random.choice(chars))
        password+=new
    print(password)
    return password
def pasinfo(password=""):
    if password=="":
        return print("Нет пароля для проверки")
    grade=5
    if len(set(password))==len(password):
        print(Fore.GREEN)
        print("Отлично, все символы уникальны!")
        time.sleep(1)
    else:
        print(Fore.WHITE)
        print("Не все символы уникальны!")
        time.sleep(1)
        grade -= 1
    cif_in_password=False
    for cif in string.digits:
        if cif in password:
            cif_in_password=True
            break
    if cif_in_password==True:
        print(Fore.GREEN)
        print("Отлично, есть цифры!")
        time.sleep(1)
    else:
        print(Fore.WHITE)
        print("Нет цифр")
        time.sleep(1)
        grade-=1
    spec_in_password=False
    for spec in "!@#$%&*":
        if spec in password:
            spec_in_password=True
            break
    if spec_in_password==True:
        print(Fore.GREEN)
        print("Отлично, есть спец символы!")
        time.sleep(1)
    else:
        print(Fore.WHITE)
        print("Нет спец символов!")
        time.sleep(1)
        grade-=1
    print(Fore.YELLOW)
    print(f"Ваш пароль {password} сделан на {grade}")
    time.sleep(1)
def menu():
    while True:
        time.sleep(1)
        try:
            print(Fore.CYAN)
            time.sleep(1)
            otvet=int(input("1. Сгенерировать пароль\n2. Проверить свой пароль\n3. Выйти\nВведите цифру: "))
            if otvet==1:
                pasgen()
            elif otvet==2:
                pasinfo()
            elif otvet==3:
                exit()
            else:
                print(Fore.MAGENTA)
                print("Вводите цифры от 1 до 3")
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