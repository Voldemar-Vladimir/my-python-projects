import datetime,csv,os,time
import matplotlib.pyplot as plt
from colorama import Fore
def __init__():
    pass
listcsv=[]
def load():
    global listcsv
    try:
        if not(os.path.exists("notes.csv")):
            print(Fore.MAGENTA)
            print("Файл с сохранениями не наден\nНачинаем с нуля")
            listcsv=[]
        else:
            with open("notes.csv","r",encoding="utf-8") as f:
                reader=csv.DictReader(f)
                for row in reader:
                    listcsv.append(row)
    except Exception as e:
        print(Fore.RED)
        print("Ошибка:",e)
load()
def save():
    with open("notes.csv","w", encoding="utf-8", newline="") as f:
        write=csv.DictWriter(f,fieldnames=["Четверть","Предмет","Оценка"])
        write.writeheader()
        write.writerows(listcsv)
def remove_csv():
    global listcsv
    listcsv=[]
    print(Fore.GREEN)
    print("Успешное удаление")
def new_fourth_mark():
    print("\n\n")
    while True:
        try:
            print(Fore.BLUE)
            fourth=int(input("Оценка какой четверти?\nВведите номер от 1 до 4: "))
            subject=input("Предмет: ")
            mark=int(input("Введите оценку от 1 до 5: "))
            if not(0<fourth<5):
                print(Fore.MAGENTA)
                print("Вводите четверть правильно")
                continue
            if not(6>mark>1):
                print(Fore.MAGENTA)
                print("Вводите оценку правильно")
                time.sleep(1)
                continue
            listcsv.append({"Четверть":fourth,"Предмет":subject,"Оценка":mark})
            save()
            time.sleep(1)
            print(Fore.CYAN)
            otvet=int(input("Выйти? 1-да , 2-нет : "))
            if otvet==1:
                break
            else:
                continue
        except ValueError:
            print(Fore.RED)
            print("Ошибка ввода, попробуйте еще\n")
            time.sleep(1)
        except Exception as e:
            print(Fore.RED)
            print("Ошибка:",e,", попробуйте еще\n")
            time.sleep(1)
def show_all():
    print("\n\n")
    for i in range(4):
        for row in listcsv:
            if int(row["Четверть"])==i+1:
                time.sleep(0.2)
                print(Fore.BLUE)
                print(f"{row['Четверть']} четверть: {row['Предмет']} – {row['Оценка']}")
    return print("\n\n")
def show_finish():
    print("\n\n")
    quarter_stats = {}
    for row in listcsv:
        q = int(row['Четверть'])
        mark = int(row['Оценка'])
        quarter_stats.setdefault(q, [0, 0])
        quarter_stats[q][0] += mark
        quarter_stats[q][1] += 1
    for q in sorted(quarter_stats.keys()):
        avg = quarter_stats[q][0] / quarter_stats[q][1]
        print(Fore.BLUE)
        print(f"Средний балл за {q} четверть: {avg:.2f}")
    time.sleep(1)
    return print("\n\n")
def problems():
    print("\n\n")
    stats = {}
    for row in listcsv:
        subj = row['Предмет']
        mark = int(row['Оценка'])
        stats.setdefault(subj, [0, 0])  # [сумма, кол-во]
        stats[subj][0] += mark
        stats[subj][1] += 1
    for subj, (total, cnt) in stats.items():
        avg = total / cnt
        if avg < 2.5:
            print(Fore.MAGENTA)
            print(f"{subj}: срочно подтянуть ({avg:.2f})")
        elif 3.3 <avg < 3.5:
            print(Fore.GREEN)
            print(f"{subj}: можно вытянуть до четвёрки ({avg:.2f})")
        elif 4.3 <avg < 4.5:
            print(Fore.GREEN)
            print(f"{subj}: можно вытянуть до пятёрки ({avg:.2f})")
        else:
            print(Fore.BLUE)
            print(f"{subj}: норм ({avg:.2f})")
        time.sleep(0.2)
    return print("\n\n")
def graph():
    print("\n\n")
    quarters = []
    averages = []
    stats = {}
    for row in listcsv:
        q = int(row['Четверть'])
        mark = int(row['Оценка'])
        stats.setdefault(q, [0, 0])
        stats[q][0] += mark
        stats[q][1] += 1
    for q in sorted(stats.keys()):
        quarters.append(q)
        averages.append(stats[q][0] / stats[q][1])
    plt.plot(quarters, averages, marker='o')
    plt.title('Динамика среднего балла')
    plt.xlabel('Четверть')
    plt.ylabel('Средний балл')
    plt.xticks(quarters)
    plt.grid(True)
    plt.show()
def menu():
    print("\n\n")
    while True:
        try:
            print(Fore.CYAN)
            time.sleep(1)
            otvet=int(input("1. Добавить четвертные\n2. Посмотреть четвертные\n3. Посмотреть предварительные итоги\n4. Что подтянуть?\n5. График успеваемости\n6. Удалить данные\n7. Сохранить и выйти\nВведите цифру: "))
            if otvet==1:
                new_fourth_mark()
            elif otvet==2:
                show_all()
            elif otvet==3:
                show_finish()
            elif otvet==4:
                problems()
            elif otvet==5:
                graph()
            elif otvet==6:
                remove_csv()
            elif otvet==7:
                save()
                break
            else:
                print(Fore.RED)
                print("!!! Введите цифру от 1 до 6 !!!")
                time.sleep(1)
        except ValueError:
            print(Fore.RED)
            print("Ошибка ввода\n")
            time.sleep(1)
        except Exception as e:
            print(Fore.RED)
            print(f"Ошибка: {e}\n")
            time.sleep(1)
if __name__=="__main__":
    menu()