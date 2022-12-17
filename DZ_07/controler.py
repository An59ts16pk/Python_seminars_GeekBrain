#import csv
import view
import model
import logging

logging.basicConfig(filename='DZ_07/log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")

sp_list = [['Иванов', 'Иванович', '89036078912', 'служащий'],['Александр', 'Петрович', '89157125468', 'электрик'],
['Николай','Васильевич','89103127612', 'программист'], ['Елена', 'Петровна', '89103127934','бухгалтер'],
['Ольга', 'Николаевна', '89035612309', 'экономист'], ['Валентина', 'Васильевна', '89052146512', 'секретарь']]

sp_l = []


def main_function():
    select = view.greeting()
    try:
        if select == 11:
            logging.info("Выбран режим чтения в формате txt")
            res_txt = model.file_txt_read('DZ_07/f_sp.txt')
            view.view_result(res_txt)
            logging.info("Файл выведен в формате txt")
            view.view_result("\nФайл успешно прочитан в формате txt.")
        elif select == 12:
            logging.info("Выбран режим записи из списка в формате txt")
            model.file_txt_write(sp_list)
            logging.info("Файл записан в формате txt")
            view.view_result("\nФайл успешно записан в формате txt.")
        elif select == 21:
            logging.info("Выбран режим чтения в формате csv")
            sp_l = model.file_csv_read('DZ_07/f_sp.csv')
            view.view_res_csv(sp_l)
            logging.info("Файл выведен в формате csv")
            view.view_result("\nФайл успешно прочитан в формате csv.")
        elif select == 22:
            logging.info("Выбран режим записи из списка в формате csv")
            model.file_csv_write(sp_list)
            logging.info("Файл записан в формате csv")
            view.view_result("\nФайл успешно записан в формате csv.")
        elif select == 13:
            logging.info("Выбран режим перекодирования txt в формат csv")
            model.txt_in_csv('DZ_07/f_sp.txt')
            logging.info("Файл успешно перекодирован из txt в формат csv")
            view.view_result("\nФайл успешно перекодирован в формат csv.")
        elif select == 23:
            logging.info("Выбран режим перекодирования csv в формат txt")
            model.csv_in_txt('DZ_07/f_sp.csv')
            logging.info("Файл успешно перекодирован из csv в формат txt")
            view.view_result("\nФайл успешно перекодирован в формат txt.")
        elif select == 31:
            logging.info("Выбран режим экспорта csv в формат json")
            model.csv_in_json('DZ_07/f_sp.csv', 'DZ_07/f_sp.json')
            logging.info("Файл успешно экспортирован из csv в формат json")
            view.view_result("\nФайл успешно экспортирован в формат json.")
        elif select == 32:
            logging.info("Выбран режим экспорта json в формат csv")
            model.json_in_csv('DZ_07/f_sp.json', 'DZ_07/f_sp.csv')
            logging.info("Файл успешно экспортирован из json в формат csv")
            view.view_result("\nФайл успешно экспортирован в формат csv.")
    except Exception as er:
        logging.warning(f'Ошибка - файла с таким форматом ещё нет, с начала выберите запись файла с таким форматом", {er}')
        print("\nОшибка - Файла с таким форматом ещё нет, сначала его создайте!!!\n")
