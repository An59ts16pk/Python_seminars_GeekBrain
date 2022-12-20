import view
import model
import logging

logging.basicConfig (filename='DZ_08/log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG, encoding="UTF-8")


def main():
    select = view.show_menu()
    if select == 1:
        logging.info("\nВыбрана команда - показать всех сотрудников.")
        sotr = model.get_list()
        view.show_employees(sotr)
        logging.info("Показаны все сотрудники.")
        print("\nВыведен список всех сотрудников.")
    elif select == 2:
        logging.warning("\nВыбрана команда - добавить сотрудника.")
        data = view.add_employee()
        model.add_employee_to_list(data)
        logging.warning("Сотрудник добавлен.")
        print("\nСотрудник добавлен.")
    elif select == 3:
        logging.info("\nВыбрана команда - изменить данные сотрудника.")
        change, string = view.change_employee()
        print(change, string)
        model.update_employee(change, string)
        logging.warning(f"Данные сотрудника изменены. Номер записи - {change}.")
        print(f"\nДанные сотрудника с номером записи {change} изменены.")
    elif select == 4:
        logging.warning("\nВыбрана команда - удалить сотрудника.")
        number = view.delete_employee()
        model.delete_employee(number)
        logging.warning(f"Сотрудник удалён - номер записи: {number}")
        print(f"\nСотрудник c номером записи: {number} - удалён.")
    elif select == 5:
        logging.info("\nВыбрана команда - вывести данные сотрудника.")
        num = view.employee()
        st = model.read_employee(num)
        view.print_employee(st)
        logging.warning(f"Выведен сотрудник - номер записи: {num}")
        print(f"\nСотрудник c номером записи: {num} - показан.\n")
    elif select == 6:
        logging.info("\nВыбрана команда - экспорт выбранных сотрудников в файл.")
        nums = view.export_employees()
        ex = model.export_employees_file(nums)
        logging.warning(f"Выполнен экспорт сотрудников с номерами записей: {ex} в файл.")
        view.res_expotr(ex, nums)
    elif select == 7:
        logging.info("\nВыбрана команда - импорт сотрудников из файла.")
        count1, count2 = model.import_exployees_file()
        logging.warning("Успешный импорт сотрудников из файла.")
        view.res_import(count1, count2)
    elif select == 8:
        logging.info("\nВыбрана команда - создание пустой базы.")
        model.create('DZ_08/catalog.csv')
        logging.info("\nПустая база успешно создана.")
    else:
        print("\nТакой команды в системе нет!")
    logging.info("Программа отработала корректно!")
