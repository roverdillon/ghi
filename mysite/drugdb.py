import sqlite3
import pandas as pd
import math

conn = sqlite3.connect('ghi.db')


conn.execute('''DROP TABLE IF EXISTS drug2010''')
conn.execute('''DROP TABLE IF EXISTS drug2013''')

conn.execute('''CREATE TABLE drug2013
             (drug text, company text, disease text, score real, percent real, color text)''')

conn.execute('''CREATE TABLE drug2010
             (drug text, company text, disease text, score real, percent real, color text)''')


datasrc = 'https://docs.google.com/spreadsheets/d/1KtWAdu4qO0mRJREY5Aje5CMZhdnxPoTPRdBXIUKN-uw/pub?gid=1560508440&single=true&output=csv'
df = pd.read_csv(datasrc, skiprows=1)
drugdata = []
drug2010 = []
drug2013 = []

for i in range(1,40):
    name = df.iloc[5,i]
    for j in range(8,19):
        temp = df.iloc[j,i]
        if type(temp) != float:
            temp = float(temp.replace(',',''))

            if temp > 0:
                if j == 8 or j == 9 or j == 10:
                    disease = 'TB'
                    color = '#FFB31C'
                elif j == 11 or j == 12:
                    disease = 'Malaria'
                    color = '#0083CA'
                elif j == 13:
                    disease = 'HIV'
                    color = '#EF3E2E'
                elif j == 14:
                    disease = 'Roundworm'
                    color = '#003452'
                elif j == 15:
                    disease = 'Hookworm'
                    color = '#86AAB9'
                elif j == 16:
                    disease = 'Whipworm'
                    color = '#CAEEFD'
                elif j == 17:
                    disease = 'Schistosomiasis'
                    color = '#546675'
                elif j == 18:
                    disease = 'Onchocerasis'
                    color = '#8A5575'
                elif j == 19:
                    disease = 'LF'
                    color = '#305516'
                company = df.iloc[0,i]

                drugrow = [name, company, disease,temp,color]
                drug2010.append(drugrow)
    score = float(df.iloc[20,i].replace(',',''))
    row = [name,score]
    drugdata.append(row)
sortedlist = sorted(drug2010, key=lambda xy: xy[3], reverse=True)
data = drugdata
maxrow = sortedlist[0]

max = maxrow[3]

for y in sortedlist:
    percent = (float(y[3]) / float(max)) * 100
    y.append(percent)
    print(y)

for row in sortedlist:
    conn.execute('insert into drug2010 values (?,?,?,?,?,?)', row)

for i in range(50,91):
    name = df.iloc[5,i]
    for j in range(8,19):
        temp = df.iloc[j,i]
        if type(temp) != float:
            temp = float(temp.replace(',',''))

            if temp > 0:
                if j == 8 or j == 9 or j == 10:
                    disease = 'TB'
                    color = '#FFB31C'
                elif j == 11 or j == 12:
                    disease = 'Malaria'
                    color = '#0083CA'
                elif j == 13:
                    disease = 'HIV'
                    color = '#EF3E2E'
                elif j == 14:
                    disease = 'Roundworm'
                    color = '#003452'
                elif j == 15:
                    disease = 'Hookworm'
                    color = '#86AAB9'
                elif j == 16:
                    disease = 'Whipworm'
                    color = '#CAEEFD'
                elif j == 17:
                    disease = 'Schistosomiasis'
                    color = '#546675'
                elif j == 18:
                    disease = 'Onchocersais'
                    color = '#8A5575'
                elif j == 19:
                    disease = 'LF'
                    color = '#305516'
                company = df.iloc[0,i]

                drugrow = [name, company, disease,temp,color]
                drug2013.append(drugrow)
sortedlist = sorted(drug2013, key=lambda xy: xy[3], reverse=True)
data = drugdata
maxrow = sortedlist[0]
max = maxrow[3]
for y in sortedlist:
    percent = (float(y[3]) / max) * 100
    y.append(percent)

for row in sortedlist:
    conn.execute('insert into drug2013 values (?,?,?,?,?,?)', row)

conn.commit()