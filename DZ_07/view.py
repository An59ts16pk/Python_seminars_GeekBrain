def greeting():
    print()
    print("11 - читать из файла txt, 12 - запись в файл txt, 13 - перекодировка txt в файл csv")
    print("21 - читать из файла csv, 22 - запись в файл csv, 23 - перекодировка csv в файл txt")
    print("31 - экспорт файла csv в json, 32 - экспорт файла json в csv")
    select = int(input("    Выберите формат ввода - вывода данных из телефонного справочника: "))
    return select

def view_result(result):
    print("\n    Результат: ")
    print(result)

def view_res_csv(result):
    print("\n    Результат: ")
    for s in result:
        print(', '.join(s))
