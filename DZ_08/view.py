def show_menu():
    print("Команды информационной системы: \n1 - показать всех сотрудников\n"
          "2 - добавить сотрудника\n3 - изменить данные сотрудника\n4 - удалить сотрудника\n"
          "5 - показать одного сотрудника\n6 - экспорт выбранных сотрудников в файл\n"
          "7 - импорт сотрудников из файла\n8 - создать пустую базу")
    try:
        select = int(input("    Выберите команду: "))
        if not select in [1, 2, 3, 4, 5, 6, 7]:
            raise ValueError
        return select
    except Exception:
        print("\nВведена неверная команда!!!")
        exit()


def show_employees(spisok):
    print("\nСписок всех сотрудников :")
    for i, sotrudnik in enumerate(spisok):
        if i == 0:
            print(" ", *sotrudnik)
        else:
            print(i, *sotrudnik)


def add_employee():
    print("\nВведите Фамилию Имя Телефон и должность через пробел: ")
    data = input().split()
    return data


def change_employee():
    change = int(input("\nВыберите номер строки для перезаписи: "))
    print("Новая строка - Фамилию Имя Телефон и должность через пробел: ")
    string = input("Введите строку для записи: ").split()
    return change, string


def delete_employee():
    number = int(input("\nВведите номер строки для удаления: "))
    return number

def employee():
    number = int(input("\nВведите номер строки сотрудника: "))
    return number

def print_employee(string):
    print("\nДанные выбранного сотрудника:")
    print(string)

def export_employees():
    print("\nВведите номера сотрудников для экспорта в другой файл через пробел: ", end='')
    numbers = [int(n) for n in input().split()]
    return numbers

def res_expotr(exp, not_exp):
    if len(exp) !=0:
        exp = [str(i) for i in exp]
        print(f"Выполнен экспорт сотрудников с номерами записей: {', '.join(exp)} успешно.")
    else:
        print("Экспорт не осуществлён - не были переданы номера строк присутствующие в базе.")
    if len(not_exp) != 0:
        not_exp = [str(i) for i in not_exp]
        print(f"Такие номера: {', '.join(not_exp)} в базе отсутствуют.")

def res_import(imp, not_imp):
    print(f"\nИз файла добавлено в базу записей: {imp}.")
    print(f"Не добавлено записей в базу: {not_imp} - они уже присутствуют в базе.")