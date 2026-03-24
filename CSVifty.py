import csv,datetime,os

listcsv=[]
def loadCSV():
    global listcsv
    try:
        if not(os.path.exists("start.csv")):
            listcsv=[]
        else:
            with open("start.csv","r",encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    listcsv.append(row)
    except:
        print("Не удалось открыть файл, начинаем с нуля")
        listcsv=[]

def writerCSV():
    while True:
        try:
            data=input("Введите дату траты в формате 2026-03-18: ")
            category=input("Введите категорию траты, например еда, развлечения, лечение\nКатегория: ")
            amount=float(input("Введите сумму траты: "))
            listcsv.append({"date":data,"category":category,"amount":amount})
            break
        except ValueError:
            print("Неудача, попробуйте еще")
def save():
        with open("start.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["date","category","amount"])
            writer.writeheader()
            writer.writerows(listcsv)
def show():
    for i in listcsv:
        print(i)
loadCSV()
def menu():
    while True:
        try:
            otvet=int(input("1. Добавить запись\n2. Посмотреть записи\n3. Сохранить и выйти\nВведите цифру: "))
            if otvet==1:
                writerCSV()
                save()
            elif otvet==2:
                show()
            elif otvet==3:
                save()
                break
            else:
                print("!!! Введите цифру от 1 до 3 !!!")
        except ValueError:
            print("Ошибка ввода")
if __name__=="__main__":
    print("Основа")