import time, asyncio

tasks = []

async def load():
    await asyncio.sleep(1)
    tasks=[{"index":1,"title":"Погулять с собакой","done":False}, {"index":2,"title":"Помыть посуду","done":False}]
    return tasks

async def add_task(title):
    index=len(tasks)+1
    tasks.append({"index": index,"title": title, "done": False})

def show_tasks():
    for i in tasks:
        ind=i["index"]
        T=i["title"]
        D=i["done"]
        if D == False:
            print(f"{ind}. {T}  X")
        else:
            print(f"{ind}. {T}  ~")
    
def complete_task(index):
    for i in tasks:
        if i["index"]==index:
            i["done"]=True

async def menu():
    while True:
        print("1. Посмотреть задачи,\n2. Отметить выполнение,\n3. Добавить задачу,\n4. Выйти")
        choice=int(input("Выберите действие: "))

        if choice==1:
            show_tasks()

        elif choice==2:
            show_tasks()
            index=int(input("Введите номер: "))
            complete_task(index)

        elif choice==3:
            title=input("Введите название задачи: ")
            await add_task(title)

        elif choice==4:
            break

        else:
            print("Нераспознанно")
async def main():  
    tasks.extend(await load())
    await menu()

asyncio.run(main())