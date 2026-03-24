import requests

def cityWttr():
    try:
        city = input("Введите город: ")
        url = f"https://wttr.in/{city}?format=%t+%c"
        response = requests.get(url, timeout=10)  # ← вот это
    except requests.exceptions.Timeout:
        print("Сервер не отвечает, попробуй позже")
        return
    except Exception as e:
        print("Ошибка подключения:", e)
        return

    if response.status_code == 200:
        print(f"Погода в {city}: {response.text}")
    else:
        print("Ошибка, попробуй другой город")

cityWttr()