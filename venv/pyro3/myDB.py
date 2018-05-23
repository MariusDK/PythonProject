#!/usr/bin/python
import sqlite3
from Agenda import Eveniment

db = sqlite3.connect('C:\\Users\\MariusDK\\PycharmProjects\\PythonProject\\venv\\database\\db',check_same_thread=False)

print("Open database successfully")
sql_script_create_table = '''CREATE TABLE IF NOT EXISTS users ( 
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      age TEXT NOT NULL,
                      email TEXT NOT NULL,
                      telefon INTEGER,
                      username TEXT UNIQUE NOT NULL, 
                      password TEXT NOT NULL
                      ); '''
sql_script_create_table2 = '''CREATE TABLE IF NOT EXISTS agenda(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                         denumire TEXT NULL,
                                         locatie TEXT NULL,
                                         descriere TEXT NULL,
                                         data DATE NULL,
                                         type TEXT NULL,
                                         id_user INTEGER,
                                         FOREIGN KEY(id_user) REFERENCES users(id)
                                         )'''
c = db.cursor()
c.execute(sql_script_create_table);
#c.execute('''DROP TABLE agenda''')
c.execute(sql_script_create_table2);
print("Table created successfully");

# cursor = db.cursor('''CREATE TABLE agenda(id INTEGER PRIMARY KEY ,
#                                          denumire TEXT,
#                                          locatie TEXT,
#                                          descriere TEXT,
#                                          data DATE,
#                                          type TEXT,
#                                          id_user INTEGER FOREIGN KEY UNIQUE
#                                          )''')

def insert_ev(denumire,locatie,descriere,data,type,id_user):
    #ev = Eveniment(denumire,locatie,descriere,data,type)
    with db:
        c.execute('INSERT INTO agenda(denumire,locatie,descriere,data,type,id_user) VALUES ( ?, ?, ?, ?, ?, ?)',
              (denumire,locatie,descriere,data,type,id_user))
        db.commit()

def update_ev(id,denumire,locatie,descriere,data,type):
    with db:
        c.execute('''UPDATE agenda 
        SET denumire = ? ,
        locatie = ? ,
        descriere = ? ,
        data = ? ,
        type = ?
        WHERE id = ?''',(denumire,locatie,descriere,data,type,id))
        db.commit()

def delete_ev(id):
    with db:
        c.execute('''DELETE FROM agenda WHERE id = ?''',id)
        db.commit()

def get_cronological_list(idUser):
    list=[]
    with db:
        c.execute('''SELECT * FROM agenda WHERE id_user = ? ORDER BY DATE(data) DESC''',(idUser,))
        rows = c.fetchall()
        for row in rows:
            e = Eveniment(row[1], row[3], row[2], row[4], row[5], row[0],row[6])
            list.append(e)
    return list

def flitrare_type(type):
    with db:
        cursor.execute('''SELECT * FROM agenda WHERE type = ?''',type)
        return cursor.fetchall()
def filtrare_locatie(locatie,idUser):
    list = []
    with db:
        c.execute('''SELECT * FROM agenda WHERE locatie = ? AND id_user = ? ''', (locatie,idUser))
        rows = c.fetchall()
        for row in rows:
            e = Eveniment(row[1], row[3], row[2], row[4], row[5], row[0],row[6])
            list.append(e)
    return list


def filtrare_data(data):
    list = []
    with db:
        c.execute('''SELECT * FROM agenda WHERE data = ?''',data)
        rows = c.fetchall()
        for row in rows:

            e = Eveniment(row[1], row[3], row[2], row[4], row[5], row[0], row[6])
            list.append(e)
    return list
def get_all(idUser):

    list = []
    with db:
        c.execute('''SELECT * FROM agenda WHERE id_user = ?''',(idUser,))
        rows = c.fetchall()

        for row in rows:
            e = Eveniment(row[1], row[3], row[2], row[4], row[5], row[0],row[6])
            list.append(e)
    return list

def get_one(id):
    with db:
        c.execute('''SELECT * FROM agenda WHERE id = ?''',id)
        row = c.fetchone()
        e = Eveniment(row[1],row[3],row[2],row[4],row[5],row[0],row[6])
        return e

def login(username,password):

    with db:
        c.execute('''SELECT * FROM users WHERE username=? and password=?''',(username,password))
        row = c.fetchone()

    if (row==None):
        return 0
    else:
        return row[0]


def register(name,age,email,phone,username,password):
    with db:
        c.execute('INSERT INTO users(name,age,email,telefon,username,password) VALUES ( ?, ?, ?, ?, ?, ?)',
                  (name, age, email, phone, username, password))
        db.commit()