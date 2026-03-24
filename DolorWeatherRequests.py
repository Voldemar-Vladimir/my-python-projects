import requests,json,time,sys,datetime
from colorama import Fore
from functools import wraps

def load_weathers():
    global weathers
    try:
        with open("weathers.json", "r", encoding="utf-8") as f:
            weathers = json.load(f)
    except FileNotFoundError:
        weathers = []  # файла нет — начинаем с нуля
    except json.JSONDecodeError:
        print("Файл повреждён, начинаем с чистого списка")
        weathers = []
def load_valutes():
    global valutes
    try:
        with open("valutes.json", "r", encoding="utf-8") as f:
            valutes = json.load(f)
    except FileNotFoundError:
        valutes = []  # файла нет — начинаем с нуля
    except json.JSONDecodeError:
        print("Файл повреждён, начинаем с чистого списка")
        valutes = []
weathers=[]
valutes=[]
def del_story(listik):
    if listik=="weathers":
        weathers=[]
        save_weathers()
    elif listik=="valutes":
        valutes=[]
        save_valutes()
def menu_weathers():
    try:
        otvet=int(input("1. Посмотреть историю\n2. Стереть историю\n3. Выйти\nВведите цифру: "))
        if otvet==1:
            weathers_story()
        elif otvet==2:
            del_story("weathers")
        elif otvet==3:
            return None
    except ValueError:
        print("Ошибка")
def menu_valutes():
    try:
        otvet=int(input("1. Посмотреть историю\n2. Стереть историю\n3. Выйти\nВведите цифру: "))
        if otvet==1:
            valutes_story()
        elif otvet==2:
            del_story("valutes")
        elif otvet==3:
            return None
    except ValueError:
        print("Ошибка")
load_valutes()
load_weathers()
def save_weathers():
    with open("weathers.json", "w", encoding="utf-8") as f:
        json.dump(weathers,f,ensure_ascii=False, indent=4)
def save_valutes():
    with open("valutes.json", "w", encoding="utf-8") as f:
        json.dump(valutes,f,ensure_ascii=False, indent=4)
def valutes_story():
    with open("valutes.json","r",encoding="utf-8") as f:
        data = json.load(f)
        for entry in data:
            print(entry)
def weathers_story():
    with open("weathers.json","r",encoding="utf-8") as f:
        data = json.load(f)
        for entry in data:
            print(entry)
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start=time.time()
        print(Fore.GREEN)
        print(f"Вызываем функцию {func.__name__} с аргументами: {args}\n{kwargs}")
        result=func(*args, **kwargs)
        end=time.time()
        seconds=end-start
        with open("logs.txt","a",encoding="utf-8") as f:
            f.write(f"{datetime.now()}: Функция {func.__name__} с аргументами ({args, kwargs}) отработала за {seconds} сек. и вернула: {result}\n")
        return result
    return wrapper
@log
def balance_valute():
    try:
        url="https://www.cbr-xml-daily.ru/daily_json.js"
        pr=requests.get(url, timeout=10)
        if pr.status_code==200:
            print(Fore.MAGENTA)
            data=pr.json()
            usd = data['Valute']['USD']['Value']
            eur = data['Valute']['EUR']['Value']
            if usd>0 and eur>0:
                while True:
                    try:
                        rub=float(input("Сколько у вас рублей?\n->: "))
                        break
                    except ValueError:continue
                print(f"\nRUB: {rub}\nUSD: {rub/usd}\nEUR: {rub/eur}\n")
                time.sleep(0.5)
                valutes.append({"Время":datetime.now().isoformat(),"RUB": rub , "USD": rub/usd , "EUR": rub/eur})
                save_valutes()
            else:
                print(Fore.RED)
                print("Потраченно")
        else:
            print(Fore.RED)
            print("Потраченно")
    except:
        print(Fore.RED)
        print("Потраченно")
@log
def weather(city="Москва"):
    try:
        url = f"https://wttr.in/{city}?format=j1&lang=ru"
        print(Fore.YELLOW + f"Запрашиваю погоду для {city}...")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        if 'application/json' in response.headers.get('Content-Type', ''):
            data = response.json()
            temp = data['current_condition'][0]['temp_C']
            fake_temp = data['current_condition'][0]['FeelsLikeC']
            wind = data['current_condition'][0]['windspeedKmph']
            hum = data['current_condition'][0]['humidity']
            city = data['nearest_area'][0]['areaName'][0]['value']
            print(Fore.GREEN + "Данные получены:")
            print(f"Температура: {temp} , ощущается как: {fake_temp}\nВетер: {wind} , влажность: {hum}")
            weathers.append({"Время":datetime.now().isoformat(),"Город":city,"Температура":temp,"Ощущается":fake_temp,"Ветер":wind,"Влажность":hum})
            save_weathers()
        else:
            print(Fore.RED + "Сервер вернул не JSON, возможно, город не найден.")
            print(response.text[:200])


    except requests.exceptions.Timeout:
        print(Fore.RED + "Ошибка: превышен таймаут соединения.")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "Ошибка: проблемы с подключением к интернету.")
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"HTTP ошибка: {e}")
    except Exception as e:
        print(Fore.RED + f"Неизвестная ошибка: {e}")
while True:
    try:
        print(Fore.YELLOW)
        otvet=int(input("1. Погода\n2. Валюта\n3. История ПОГОДА\n4. История ВАЛЮТА\n5. Выход \nВведите цифру: "))
        if otvet==1:
            city=input("Введите город: ")
            if city=="":
                city="Москва"
            weather(city)
        elif otvet==2:
            balance_valute()
        elif otvet==3:
            menu_weathers()
        elif otvet==4:
            menu_valutes()
        elif otvet==5:
            exit()
        else:
            print(Fore.RED+"!!! Введите цифру от 1 до 3 !!!")
    except ValueError:
        print(Fore.RED+"Ошибка ввода")
if __name__ == "__main__":
    try:
        with open("logs.txt","r") as f:
            for i in f:
                print(i)
    except ValueError:
        pass