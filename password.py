import string, random
from colorama import Fore, Style, Back, init
def __init__():
    pass
def pasgen():
    print(Fore.BLUE)
    chars = string.ascii_letters
    print("Отвечайте 'ДА' или 'НЕТ' !!!\n")
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
    password=""
    for i in range(long):
        new=(random.choice(chars))
        while new in password:
            new=(random.choice(chars))
        password+=new
    print(password)
    return password
def pasinfo(password):
    grade=5
    if len(set(password))==len(password):
        print("Отлично, все символы уникальны!")
    else:
        print("Не все символы уникальны!")
        grade -= 1
    cif_in_password=False
    for cif in string.digits:
        if cif in password:
            cif_in_password=True
            break
    if cif_in_password==True:print("Отлично, есть цифры!")
    else:
        print("Нет цифр")
        grade-=1
    spec_in_password=False
    for spec in "!@#$%&*":
        if spec in password:
            spec_in_password=True
            break
    if spec_in_password==True:print("Отлично, есть спец символы!")
    else:
        print("Нет спец символов!")
        grade-=1
    print(f"Ваш пароль {password} сделан на {grade}")



if "__main__"==__name__:
    print("Все норм, работаем")
