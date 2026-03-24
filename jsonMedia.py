import json
media=[]
def load_data():
    try:
        with open("media.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
media = load_data()
def save_media(media):
    with open("media.json","w", encoding="utf-8") as f:
        json.dump(media, f, ensure_ascii=False, indent=4)
def add_media():
    id=len(media)+1
    tip=input("Введите тип: ")
    name=input("Введите название: ")
    year=input("Введите год: ")
    avtor=input("Введите автора: ")
    status=input("Введите статус: ")
    media.append({"id":id,"name":name,"year":year,"avtor":avtor,"status":status})
    save_media(media)
def menu():
        otvet=input("1. Добавить\n2. Посмотреть\n3. Выйти (с сохранением)\nЧто хотите сделать?\nУкажите номер: ")
        if otvet=="1":
            add_media()
        elif otvet=="2":
            print(media)
        elif otvet=="3":
            save_media(media)
            exit()
        else:
            menu()
while True:
    menu()