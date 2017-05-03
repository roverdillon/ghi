import sqlite3
import pandas as pd
import math


conn = sqlite3.connect('ghi.db')

conn.execute(''' DROP TABLE IF EXISTS country2010 ''')
conn.execute(''' DROP TABLE IF EXISTS country2013 ''')
conn.execute(''' DROP TABLE IF EXISTS countryp2010 ''')
conn.execute(''' DROP TABLE IF EXISTS countryp2013 ''')

conn.execute(''' CREATE TABLE country2010 (country text, total real, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistomasis real, lf real) ''')
conn.execute(''' CREATE TABLE country2013 (country text, total real, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistomasis real, onchoceriasis real, lf real) ''')

conn.execute(''' CREATE TABLE countryp2010 (country text, total real, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistomasis real, lf real) ''')
conn.execute(''' CREATE TABLE countryp2013 (country text, total real, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistomasis real, onchoceriasis real, lf real) ''')


url = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=0&single=true&output=csv'
df = pd.read_csv(url, skiprows=1)

def cleanfloat(var):
        if var == '#REF!':
            var = 0
        if var == '#DIV/0!':
            var = 0
        if type(var) != float and type(var) != int:
            var = float(var.replace(',','').replace('%','').replace(' ','').replace('-','0'))
        if var != var:
            var = 0
        return var

countrydata = []
mapp = []

for i in range(3, 218):
    country = df.iloc[i,0]
    tb = cleanfloat(df.iloc[i,7])
    malaria = cleanfloat(df.iloc[i,34])
    hiv = cleanfloat(df.iloc[i,47])
    roundworm = cleanfloat(df.iloc[i,66])
    hookworm = cleanfloat(df.iloc[i,67])
    whipworm = cleanfloat(df.iloc[i,68])
    schistomasis = cleanfloat(df.iloc[i,76])
    lf = cleanfloat(df.iloc[i,80])
    total = tb + malaria + hiv + roundworm + hookworm + whipworm + schistomasis + lf
    row = [country, total, tb, malaria, hiv, roundworm, hookworm, whipworm, schistomasis, lf]
    countrydata.append(row)
    print(row)

sortedlist = sorted(countrydata, key=lambda xy: xy[1], reverse=True)
maxrow = sortedlist[0]
maxval = maxrow[1]
for j in sortedlist:
    country = j[0]
    total = (j[1]/maxval) *  100
    tb = (j[2]/maxval) *  100
    malaria = (j[3]/maxval) *  100
    hiv = (j[4]/maxval) *  100
    roundworm = (j[5]/maxval) *  100
    hookworm = (j[6]/maxval) *  100
    whipworm = (j[7]/maxval) *  100
    schistomasis = (j[8]/maxval) *  100
    lf = (j[9]/maxval) *  100
    row = [country, total, tb, malaria, hiv, roundworm, hookworm, whipworm, schistomasis, lf]
    mapp.append(row)
    print(row)

for k in countrydata:
    conn.execute(''' INSERT INTO country2010 VALUES (?,?,?,?,?,?,?,?,?,?) ''', k)

for l in mapp:
    conn.execute(''' INSERT INTO countryp2010 VALUES (?,?,?,?,?,?,?,?,?,?) ''', l)

countrydata2 = []
mapp2 = []
for i in range(3, 218):
    country = df.iloc[i,83]
    tb = cleanfloat(df.iloc[i,90])
    malaria = cleanfloat(df.iloc[i,120])
    hiv = cleanfloat(df.iloc[i,131])
    roundworm = cleanfloat(df.iloc[i,150])
    hookworm = cleanfloat(df.iloc[i,151])
    whipworm = cleanfloat(df.iloc[i,152])
    schistomasis = cleanfloat(df.iloc[i,160])
    onchoceriasis = cleanfloat(df.iloc[i,165])
    lf = cleanfloat(df.iloc[i,169])
    total = tb + malaria + hiv + roundworm + hookworm + whipworm + schistomasis + onchoceriasis + lf
    row = [country, total, tb, malaria, hiv, roundworm, hookworm, whipworm, schistomasis, onchoceriasis, lf]
    countrydata2.append(row)

sortedlist2 = sorted(countrydata2, key=lambda xy: xy[1], reverse=True)
maxrow = sortedlist2[0]
maxval = maxrow[1]
for j in sortedlist2:
    country = j[0]
    total = (j[1]/maxval) *  100
    tb = (j[2]/maxval) *  100
    malaria = (j[3]/maxval) *  100
    hiv = (j[4]/maxval) *  100
    roundworm = (j[5]/maxval) *  100
    hookworm = (j[6]/maxval) *  100
    whipworm = (j[7]/maxval) *  100
    schistomasis = (j[8]/maxval) *  100
    onchoceriasis = (j[9]/maxval) * 100
    lf = (j[10]/maxval) *  100
    row = [country, total, tb, malaria, hiv, roundworm, hookworm, whipworm, schistomasis, onchoceriasis, lf]
    mapp2.append(row)

for k in countrydata2:
    conn.execute(''' INSERT INTO country2013 VALUES (?,?,?,?,?,?,?,?,?,?,?) ''', k)

for l in mapp2:
    conn.execute(''' INSERT INTO countryp2013 VALUES (?,?,?,?,?,?,?,?,?,?,?) ''', l)

conn.commit()