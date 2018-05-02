#!/usr/bin/python
import sqlite3
from classes import Eveniment

db = sqlite3.connect('mydb.db',check_same_thread=False)

print("Open database successfully")
sql_script_create_table = '''CREATE TABLE IF NOT EXISTS users ( 
                      id INT PRIMARY KEY NOT NULL,
                      name TEXT NOT NULL,
                      varsta TEXT NOT NULL,
                      email TEXT NOT NULL,
                      telefon INTEGER 
                      ); '''
sql_script_create_table2 = '''CREATE TABLE IF NOT EXISTS agenda(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                         denumire TEXT NULL,
                                         locatie TEXT NULL,
                                         descriere TEXT NULL,
                                         data DATE NULL,
                                         type TEXT NULL,
                                         id_user INT UNIQUE NULL,
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

def insert_ev(denumire,locatie,descriere,data,type):
    #ev = Eveniment(denumire,locatie,descriere,data,type)
    with db:
        c.execute('INSERT INTO agenda(denumire,locatie,descriere,data,type) VALUES ( ?, ?, ?, ?, ?)',
              (denumire,locatie,descriere,data,type))
        db.commit()

def update_ev(ev):
    with db:
        cursor.execute('''UPDATE agenda 
        SET denumire = ? ,
        locatie = ? ,
        descriere = ? ,
        data = ? ,
        type = ?
        WHERE id = ?''',(ev.get_denumire(),ev.get_locatie(),ev.get_descriere(),ev.get_data(),ev.get_type(),ev.get_id()))
        db.commit()

def delete_ev(ev):
    with db:
        cursor.execute('''DELETE FROM agenda WHERE id = ?''',(ev.get_id))
        db.commit()

def get_cronological_list():
    with db:
        cursor.execute('''SELECT * FROM agenda ORDER BY DATE(data) DESC LIMIT 1''')
        return cursor.fetchall()

def flitrare_type(type):
    with db:
        cursor.execute('''SELECT * FROM agenda WHERE type = ?''',type)
        return cursor.fetchall()
def filtrare_locatie(locatie):
    with db:
        cursor.execute('''SELECT * FROM agenda WHERE locatie = ?''', locatie)
        return cursor.fetchall()
def filtrare_data(data):
    with db:
        cursor.execute('''SELECT * FROM agenda WHERE data = ?''',data)
        return cursor.fetchall()
def get_all():
    with db:
        c.execute('''SELECT * FROM agenda ''')
        rows = c.fetchall()
        for row in rows:
            print (row[0], row[1])
