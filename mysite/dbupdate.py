import sqlite3
import pandas as pd
import math


conn = sqlite3.connect('ghi.db')


conn.execute('''DROP TABLE IF EXISTS drug2010''')
conn.execute('''DROP TABLE IF EXISTS drug2013''')

conn.execute('''DROP TABLE IF EXISTS drugr2010''')
conn.execute('''DROP TABLE IF EXISTS drugpie2010''')

conn.execute('''DROP TABLE IF EXISTS drugr2013''')
conn.execute('''DROP TABLE IF EXISTS drugpie2013''')

conn.execute('''CREATE TABLE drugr2010
            (drug text, company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real)''')

conn.execute('''CREATE TABLE drugr2013
            (drug text, company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real)''')


datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv'
df = pd.read_csv(datasrc, skiprows=1)
drugdata = []
drugrdata = []
drug2010 = []
drug2013 = []
perc2010 = []

def cleanfloat(var):
    if var == '#REF!':
        var = 0
    if type(var) != float and type(var) != int:
        var = float(var.replace(',',''))
    if var != var:
        var = 0
    return var

for i in range(1,43):
    drugr = []
    name = df.iloc[4,i]
    drugr.append(name)
    company = df.iloc[1,i]
    drugr.append(company)
    for j in range(10,20):
        if j == 10:
            tb1 = cleanfloat(df.iloc[7,i])
            tb2 = cleanfloat(df.iloc[8,i])
            tb3 = cleanfloat(df.iloc[9,i])
            tb=[tb1,tb2,tb3]
            temp = (tb1+tb2+tb3)
            drugr.append(temp)
        elif j == 11:
            mal1 = cleanfloat(df.iloc[10,i])
            mal2 = cleanfloat(df.iloc[11,i])
            mal=[mal1,mal2]
            temp = (mal1+mal2)
            drugr.append(temp)
        elif j == 19:
            total = cleanfloat(df.iloc[j,i])
            zz = [name,total]
            perc2010.append(zz)
        else:
            temp = df.iloc[j,i]
            if isinstance(temp,float) == False and isinstance(temp,int) == False:
                temp = float(temp.replace(',',''))
            if temp != temp:
                temp = 0
            drugr.append(temp)
        if temp > 0:
            if j == 10:
                disease = 'TB'
                color = 'FFB31C'
            elif j == 11 or j == 12:
                disease = 'Malaria'
                color = '0083CA'
            elif j == 13:
                disease = 'HIV'
                color = 'EF3E2E'
            elif j == 14:
                disease = 'Roundworm'
                color = '003452'
            elif j == 15:
                disease = 'Hookworm'
                color = '86AAB9'
            elif j == 16:
                disease = 'Whipworm'
                color = 'CAEEFD'
            elif j == 17:
                disease = 'Schistosomiasis'
                color = '546675'
            elif j == 18:
                disease = 'Onchocerasis'
                color = '8A5575'
            elif j == 19:
                disease = 'LF'
                color = '305516'
            company = df.iloc[1,i]
            drugrow = [name, company, disease, temp, color]
            drug2010.append(drugrow)



    if isinstance(df.iloc[20,i],float) == False:
        score = float(df.iloc[20,i].replace(',',''))
    else:
        score = df.iloc[20,i]
    row = [name,score]
    drugdata.append(row)
    drugrdata.append(drugr)

unmet = ['Unmet Need','Unmet Need']
unmetsum = 0
for xx in [[7,8,9],[10,11],[12],[13],[14],[15],[16],[17],[18]]:
    val = 0
    for yy in xx:
        t = df.iloc[yy,45]
        if isinstance(t,float) == False and isinstance(t,int) == False:
            t = float(t.replace(',',''))
        if t != t:
            t = 0
        val += t
    unmet.append(val)
    unmetsum += val
print(unmet)
print(drugrdata[0])
drugrdata.append(unmet)

for row in drugrdata:
    tot = sum(row[2:])
    row.append(tot)
    conn.execute('insert into drugr2010 values (?,?,?,?,?,?,?,?,?,?,?,?)', row)


drugdata = []
drugrdata = []
perc2013 = []

for i in range(50,91):
    drugr = []
    name = df.iloc[4,i]
    drugr.append(name)
    company = df.iloc[1,i]
    drugr.append(company)
    for j in range(10,20):
        if j == 10:
            tb1 = cleanfloat(df.iloc[7,i])
            tb2 = cleanfloat(df.iloc[8,i])
            tb3 = cleanfloat(df.iloc[9,i])
            tb=[tb1,tb2,tb3]
            temp = (tb1+tb2+tb3)
            drugr.append(temp)
        elif j == 11:
            mal1 = cleanfloat(df.iloc[10,i])
            mal2 = cleanfloat(df.iloc[11,i])
            mal=[mal1,mal2]
            temp = (mal1+mal2)
            drugr.append(temp)
        elif j == 19:
            total = cleanfloat(df.iloc[j,i])
            zz = [name,total]
            perc2013.append(zz)
        else:
            temp = df.iloc[j,i]
            if isinstance(temp,float) == False and isinstance(temp,int) == False:
                temp = float(temp.replace(',',''))
            if temp != temp:
                temp = 0
            drugr.append(temp)
        if temp > 0:
            if j == 10:
                disease = 'TB'
                color = 'FFB31C'
            elif j == 11 or j == 12:
                disease = 'Malaria'
                color = '0083CA'
            elif j == 13:
                disease = 'HIV'
                color = 'EF3E2E'
            elif j == 14:
                disease = 'Roundworm'
                color = '003452'
            elif j == 15:
                disease = 'Hookworm'
                color = '86AAB9'
            elif j == 16:
                disease = 'Whipworm'
                color = 'CAEEFD'
            elif j == 17:
                disease = 'Schistosomiasis'
                color = '546675'
            elif j == 18:
                disease = 'Onchocerasis'
                color = '8A5575'
            elif j == 19:
                disease = 'LF'
                color = '305516'
            company = df.iloc[1,i]
            drugrow = [name, company, disease, temp, color]
            drug2013.append(drugrow)



    if isinstance(df.iloc[20,i],float) == False:
        score = float(df.iloc[20,i].replace(',',''))
    else:
        score = df.iloc[20,i]
    row = [name,score]
    drugdata.append(row)
    drugrdata.append(drugr)

unmet = ['Unmet Need','Unmet Need']
unmetsum = 0
for xx in [[7,8,9],[10,11],[12],[13],[14],[15],[16],[17],[18]]:
    val = 0
    for yy in xx:
        t = df.iloc[yy,93]
        if isinstance(t,float) == False and isinstance(t,int) == False:
            t = float(t.replace(',',''))
        if t != t:
            t = 0
        val += t
    unmet.append(val)
    unmetsum += val
drugrdata.append(unmet)
sortedlist = sorted(drug2013, key=lambda xy: xy[3], reverse=True)

for row in drugrdata:
    tot = sum(row[2:])
    row.append(tot)
    conn.execute('insert into drugr2013 values (?,?,?,?,?,?,?,?,?,?,?,?)', row)
perc2013.sort(key=lambda x: x[1], reverse=True)

conn.commit()