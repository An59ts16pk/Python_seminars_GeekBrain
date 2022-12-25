import sqlite3


def db_view(db_f):
    conn = sqlite3.connect(db_f, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('select * from phones')
    res = cursor.fetchall()
    conn.close()
    return res

def db_one(val, db_f):
    conn = sqlite3.connect(db_f)
    cursor = conn.cursor()
    cursor.execute(f"select * from phones where surname like '%{val}%'"
                    f"or name like '%{val}%'")
    res = cursor.fetchall()
    conn.close()
    if res:
        return res
    return 'Контакт не найден!'

def db_num(val, db_f):
    conn = sqlite3.connect(db_f)
    cursor = conn.cursor()
    cursor.execute(f'select * from phones where id={val}')
    res = cursor.fetchone()
    conn.close()
    if res:
        return res
    return 'Контакт не найден!'

def db_add(val, db_f):
    conn = sqlite3.connect(db_f)
    cursor = conn.cursor()
    v = val.split()
    surname, name, phone, post = tuple(v)
    cursor.execute(f"insert into phones (surname, name, phone, post)"
                 f"values ('{surname}', '{name}', {phone}, '{post}')")
    conn.commit()
    conn.close()

def db_delete(val, db_f):
    conn = sqlite3.connect(db_f)
    cursor = conn.cursor()
    cursor.execute(f'select * from phones where id={val}')
    res = cursor.fetchone()
    if res:
        cursor.execute(f"delete from phones where id={val}")
        conn.commit()
        conn.close()
        return 'Контакт удалён.'
    conn.close()
    return 'Контакт не найден!'

def db_redact(val, id, db_f):
    conn = sqlite3.connect(db_f)
    cursor = conn.cursor()
    surname, name, phone, post = tuple(val)
    cursor.execute(f"update phones set surname='{surname}', name='{name}', phone={phone}, post='{post}' where id={id}")
    conn.commit()
    conn.close()