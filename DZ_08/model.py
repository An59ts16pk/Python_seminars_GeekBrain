import csv

def get_list():
    with open('DZ_08/catalog.csv', encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter=';')
        return list(reader)


def add_employee_to_list(employee):
    with open('DZ_08/catalog.csv', 'a', encoding="utf-8", newline='') as a_file:
        writer = csv.writer(a_file, delimiter=';')
        writer.writerow(employee)


def update_employee(number, string):
    try:
        with open('DZ_08/catalog.csv', 'r', encoding="utf-8", newline='') as r_file:
            reader = csv.reader(r_file, delimiter=';')
            data = list(reader)
            data[number] = string
        with open('DZ_08/catalog.csv', 'w', encoding="utf-8", newline='') as w_file:
            writer = csv.writer(w_file, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы массива.")
        exit()
    except Exception:
        print("Выявлены другие ошибки!!!")
        exit()


def delete_employee(number):
    try:
        with open('DZ_08/catalog.csv', 'r', encoding="utf-8", newline='') as r_file:
            reader = csv.reader(r_file, delimiter=';')
            data = list(reader)
            del data[number]
        with open('DZ_08/catalog.csv', 'w', encoding="utf-8", newline='') as w_file:
            writer = csv.writer(w_file, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print("Вы вышли за границы массива.")
        exit()
    except Exception:
        print("Выявлены другие ошибки!!!")
        exit()

def read_employee(number):
    try:
        with open('DZ_08/catalog.csv', 'r', encoding="utf-8", newline='') as r_file:
            reader = csv.reader(r_file, delimiter=';')
            data = list(reader)
            string = ', '.join(data[number])
            return string
    except IndexError:
        print(f"Запись с номером {number} отсутствует в базе.")
        exit()

def export_employees_file(numbers):
    exp = []
    exp_i = []
    with open('DZ_08/catalog.csv', 'r', encoding="utf-8", newline='') as r_file:
        reader = csv.reader(r_file, delimiter=';')
        data = list(reader)
        for i, sotrudnik in enumerate(data):
            if i in numbers:
                exp.append(sotrudnik)
                exp_i.append(i)
                numbers.remove(i)
    with open('DZ_08/out.csv', 'w', encoding="utf-8", newline='') as w_file:
        writer = csv.writer(w_file, delimiter=';')
        writer.writerow(["Имя", "Фамилия", "Телефон", "Должность"])
        for i in exp:
            writer.writerow(i)
    return exp_i
        
def import_exployees_file():
    with open('DZ_08/impr.csv', 'r', encoding="utf-8", newline='') as r_file:
        reader1 = csv.reader(r_file, delimiter=';')
        data1 = list(reader1)
        data1.pop(0)
        d = len(data1)
        count = 0
    with open('DZ_08/catalog.csv', 'r', encoding="utf-8", newline='') as r_file:
        reader2 = csv.reader(r_file, delimiter=';')
        data2 = list(reader2)
    with open('DZ_08/catalog.csv', 'a', encoding="utf-8", newline='') as a_file:
        writer = csv.writer(a_file, delimiter=';')
        for s in data1:
            if s not in data2:
                writer.writerow(s)
                count += 1
    return str(count), str(d - count)

def create(fl):
    with open(fl, 'w', encoding="utf-8", newline='') as w_file:
        writer = csv.writer(w_file, delimiter=';')
        writer.writerow(["Имя", "Фамилия", "Телефон", "Должность"])
       