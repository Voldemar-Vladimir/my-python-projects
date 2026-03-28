import random,string,time,csv,json,os,datetime,password,habit_tracker,notes,marks_helper,calories_control
import matplotlib.pyplot as plt
from colorama import Fore
def save_all_projects():
    try:
        habit_tracker.save_t()
        marks_helper.save()
        calories_control.save()
    except:pass
def menu():
    while True:
        try:
            print(Fore.CYAN)
            time.sleep(1)
            otvet=int(input("1. Калькулятор оценок\n2. Дневник калорий\n3. Заметки\n4. Генератор паролей\n5. Трекер привычек\n6. Сохранить и выйти\nВведите цифру: "))
            if otvet==1:
                marks_helper.load()
                while True:
                    try:
                        print(Fore.CYAN)
                        time.sleep(1)
                        otvet=int(input("1. Добавить четвертные\n2. Посмотреть четвертные\n3. Посмотреть предварительные итоги\n4. Что подтянуть?\n5. График успеваемости\n6. Удалить данные\n7. Сохранить и выйти\nВведите цифру: "))
                        if otvet==1:
                            marks_helper.new_fourth_mark()
                        elif otvet==2:
                            marks_helper.show_all()
                        elif otvet==3:
                            marks_helper.show_finish()
                        elif otvet==4:
                            marks_helper.problems()
                        elif otvet==5:
                            marks_helper.graph()
                        elif otvet==6:
                            marks_helper.remove_csv()
                        elif otvet==7:
                            marks_helper.save()
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
            elif otvet==2:
                calories_control.load()
                while True:
                    time.sleep(0.5)
                    try:
                        print(Fore.YELLOW)
                        otvet=int(input("1. Добавить запись\n2. Посмотреть записи\n3. Сумма калорий сегодня\n4. Сколько нужно калорий?\n5. Калории за неделю\n6. Удалить данные\n7. Сохранить и выйти\nВведите цифру: "))
                        if otvet==1:
                            calories_control.new_eat()
                        elif otvet==2:
                            calories_control.show_all()
                        elif otvet==3:
                            calories_control.show_sum()
                        elif otvet==4:
                            calories_control.calc_calories()
                        elif otvet==5:
                            calories_control.show_sum_week()
                        elif otvet==6:
                            calories_control.remove_csv()
                        elif otvet==7:
                            calories_control.save()
                            break
                        else:
                            print(Fore.MAGENTA)
                            print("!!! Введите цифру от 1 до 6 !!!")
                    except ValueError:
                        print(Fore.RED)
                        print("Ошибка ввода\n")
                        time.sleep(0.5)
                    except Exception as e:
                        print(Fore.RED)
                        print(f"Ошибка: {e}\n")
                        time.sleep(0.5)
            elif otvet==3:
                    while True:
                        try:
                            print(Fore.CYAN)
                            time.sleep(1)
                            otvet=int(input("1. Новая запись\n2. Посмотреть заметки\n3. Удалить заметки\n4. Сохранить и выйти\nВведите цифру: "))
                            if otvet==1:
                                notes.add_note()
                            elif otvet==2:
                                notes.show_notes()
                            elif otvet==3:
                                notes.clear_notes()
                            elif otvet==4:
                                break
                            else:
                                print(Fore.MAGENTA)
                                print("Вводите цифры от 1 до 4")
                        except ValueError:
                            print(Fore.RED)
                            print("Ошибка ввода")
                        except Exception as e:
                            print(Fore.RED)
                            print(f"Ошибка: {e}")
            elif otvet==4:
                while True:
                    try:
                        print(Fore.CYAN)
                        time.sleep(1)
                        otvet=int(input("1. Сгенерировать пароль\n2. Проверить свой пароль\n3. Выйти\nВведите цифру: "))
                        if otvet==1:
                            password.pasgen()
                        elif otvet==2:
                            password.pasinfo()
                        elif otvet==3:
                            break
                        else:
                            print(Fore.MAGENTA)
                            print("Вводите цифры от 1 до 3")
                    except ValueError:
                        print(Fore.RED)
                        print("Ошибка ввода")
                    except Exception as e:
                        print(Fore.RED)
                        print(f"Ошибка: {e}")
            elif otvet==5:
                habit_tracker.load_data()
                habits = habit_tracker.load_data()
                while True:
                    print(Fore.CYAN)
                    try:
                        otvet=input("1. Добавить привычку\n2. Отметить привычку выполненной\n3. Показать все привычки со статусом на сегодня\nВыйти (с сохранением)\nЧто хотите сделать?\nУкажите номер: ")
                        if otvet=="1":
                            habit_tracker.add_t()
                        elif otvet=="2":
                            habit_tracker.metka_t()
                        elif otvet=="3":
                            habit_tracker.print(habits)
                        elif otvet=="4":
                            habit_tracker.save_t(habits)
                            break
                        else:
                            print(Fore.MAGENTA)
                            print("Вводите цифру от 1 до 4")
                    except ValueError:
                        print(Fore.RED)
                        print("Ошибка ввода")
                    except Exception as e:
                        print(Fore.RED)
                        print(f"Ошибка: {e}")
            elif otvet==6:
                save_all_projects()
                exit()
                break
            else:
                print(Fore.RED)
                print("!!! Введите цифру от 1 до 6 !!!")
                time.sleep(1)
        except ValueError:
            print(Fore.RED)
            print("Ошибка ввода\n")
        except Exception as e:
            print(Fore.RED)
            print(f"Ошибка: {e}\n")
if __name__=="__main__":
    menu()