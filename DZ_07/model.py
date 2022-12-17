import csv
import json


def file_csv_read(fl):
    lst = []
    with open(fl, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        for row in file_reader:
            lst.append(row)
    return lst

def file_csv_write(lst):
    with open('DZ_07/f_sp.csv', 'w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Имя", "Фамилия", "Телефон", "Описание"])
        for s in lst:
            file_writer.writerow(s)

def file_txt_read(fl):
    with open(fl, encoding='utf-8') as r_file:
        data = r_file.read()
    return data

def file_txt_write(lst):
    with open('DZ_07/f_sp.txt', 'w', encoding='utf-8') as w_file:
        for s in lst:
            w_file.write('\n'.join(s) + '\n\n')

def txt_in_csv(fl):
    lst = []
    with open(fl, encoding='utf-8') as r_file, open('DZ_07/f_sp.csv', 'w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Имя", "Фамилия", "Телефон", "Описание"])
        
        st = [line.strip() for line in r_file]
        lst = [st[i:i+4] for i in range(0, len(st), 5)]
        
        for x in lst:
            file_writer.writerow(x)


def csv_in_txt(fl):
    lst = []
    with open(fl, encoding='utf-8') as r_file, open('DZ_07/f_sp.txt', 'w', encoding='utf-8') as w_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        for row in file_reader:
            lst.append(row)
        for i in range(1,len(lst)):
            w_file.write('\n'.join(lst[i]) + '\n\n')

def csv_in_json(f_c, f_j):
    data = {}
    with open(f_c, encoding='utf-8') as r_file:
        csv_read = csv.DictReader(r_file)
        n_key = 0
        for rows in csv_read:
            n_key += 1
            data[n_key] = rows
    with open(f_j, 'w', encoding='utf-8') as w_file:
        w_file.write(json.dumps(data, indent=4, ensure_ascii=False))

def json_in_csv(f_j, f_c):
    sp_lst = []
    with open(f_j, encoding='utf-8') as r_file:
        data = json.load(r_file)
    for key in data.keys():
        sp_lst.append([v for v in data[key].values()])
    
    with open(f_c, 'w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Имя", "Фамилия", "Телефон", "Описание"])
        for x in sp_lst:
            file_writer.writerow(x)