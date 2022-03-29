import sqlite3 as sql


def insertRow(nombre, apellido, celular, email):
    conn = sql.connect('crud.db')
    cursor = conn.cursor()
    consulta = f"INSERT INTO persona (nombre, apellido, celular, email) VALUES ('{nombre}', '{apellido}', '{celular}', '{email}')"
    cursor.execute(consulta)
    conn.commit()
    conn.close()

def search():
    conn = sql.connect('crud.db')
    cursor = conn.cursor()
    consulta = f"SELECT * FROM persona"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def deleteRow(item):
    conn = sql.connect('crud.db')
    cursor = conn.cursor()
    consulta = f"DELETE FROM persona WHERE id='{item}'"
    cursor.execute(consulta)
    conn.commit()
    conn.close()