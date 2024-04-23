import mysql.connector;

conn = mysql.connector.connect(host='127.0.0.1',database='saasure_prod',user='root',password='sAAsysu3')

if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()

cursor.execute('SELECT * FROM Apps')

# for one record
# cursor.fetchone()
rows = cursor.fetchall()
print("Total Number of records",cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()