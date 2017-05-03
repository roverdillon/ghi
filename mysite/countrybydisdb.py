import sqlite3
import pandas as pd
import math

conn = sqlite3.connect('ghi.db')


conn.execute('''DROP TABLE IF EXISTS countrybydis2010''')
conn.execute('''DROP TABLE IF EXISTS countrybydis2013''')

conn.execute('''CREATE TABLE countrybydis2010
             (country text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schis real, onch real, lf real)''')

conn.execute('''CREATE TABLE countrybydis2013
             (country text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schis real, onch real, lf real)''')


datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1996016204&single=true&output=csv'
df = pd.read_csv(datasrc, skiprows=1)
for i in range (1,216):
    temprow = []
    temprow.append(df.iloc[i,0])
    for k in range(1,10):
        temp = df.iloc[i,k]
        if isinstance(temp,float):
            temprow.append(0.0)
        else:
            temprow.append(float(temp.replace(',','').replace('-','0')))
    conn.execute(' insert into countrybydis2010 values (?,?,?,?,?,?,?,?,?,?)', temprow)

for i in range (1,216):
    temprow = []
    temprow.append(df.iloc[i,11])
    for k in range(12,21):
        temp = df.iloc[i,k]

        if isinstance(temp,float):
            temprow.append(0.0)
        else:
            temprow.append(float(temp.replace(',','').replace('-','0')))
    conn.execute(' insert into countrybydis2013 values (?,?,?,?,?,?,?,?,?,?)', temprow)


conn.commit()