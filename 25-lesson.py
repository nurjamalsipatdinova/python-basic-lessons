import sqlite3
db=sqlite3.connect("data.db")
cursor=db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS jurnal(
tema TEXT,
podtema TEXT,
view INTEGER,
avtor TEXT
)
""")



# db.commit()
# cursor.execute("INSERT INTO jurnal VALUES('Instgram', 'Insta', 100000 , 'Aydos' )")
# cursor.execute("INSERT INTO jurnal VALUES('Google', 'Google en jaqsisi', 3400 , 'Azamat' )")
# cursor.execute("INSERT INTO jurnal VALUES('Fecebook!', 'Fecebook qiziqarli', 4080 , 'Salamat' )")
# cursor.execute("INSERT INTO jurnal VALUES('Telegram!', 'Telegram kop funkciyali', 4080 , 'Salamat' )")

# cursor.execute("SELECT * FROM jurnal")
# print(cursor.fetchall())
# print(cursor.fetchmany())
# print(cursor.fetchmany()[0])
# # print(cursor.fetchone())

# m= cursor.fetchall()
# for i in m:
#     if i[0] == "Fecebook!":
#         print(f"{i[0]} temasin jazgan adam {i[3]}")




# cursor.execute("DELETE FROM jurnal WHERE avtor= 'Azamat'")
# cursor.execute("SELECT ROWID, * FROM jurnal")
# db.commit()
# print(cursor.fetchall())


# cursor.execute("UPDATE jurnal SET avtor='Darmen', view=1000  WHERE avtor= 'Sala'")
# cursor.execute("SELECT * FROM jurnal")
# db. commit()
# items=cursor.fetchall()
# for i in items:
#     print(i[2], '-', i[3])
#
# db.close()



cursor.execute(""" CREATE TABLE IF NOT EXISTS info(
name TEXT,
fam TEXT,
nomer INTEGER,
gmail TEXT
)
""")
db.commit()
# cursor.execute("INSERT INTO info VALUES('Darmen', 'Allambergenov', 901234567 , '@darmenallgmail.com ' )")
# cursor.execute("INSERT INTO info VALUES('Meyrambek', 'Maxsetov', 907654321 , '@meyrambekmaxsetovgmail.com ' )")
# cursor.execute("INSERT INTO info VALUES('Nurjamal', 'Sipatdinova', 904688391 , '@nurjamalsipatdinova.com ' )")


# cursor.execute("DELETE FROM info WHERE  name='Darmen'")
# cursor.execute("UPDATE info SET  name='Asan', fam='Tolepov' WHERE name='Meyrambek'")
# db.commit()
# print(cursor.fetchall())
# cursor.execute("SELECT * FROM info")
# items=cursor.fetchall()
# print(items)
# for i in items:
#     print(f"Konkursda {i[0]} {i[1]} qaldi")




# cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
# name TEXT,
# fam TEXT,
# nomer INTEGER,
# gmail TEXT
# )
# """)
# db.commit()
# cursor.execute("INSERT INTO users VALUES('Darmen', 'Allambergenov', 901234567 , '@darmenallgmail.com ' )")
# cursor.execute("INSERT INTO  VALUES('Meyrambek', 'Maxsetov', 907654321 , '@meyrambekmaxsetovgmail.com ' )")
# cursor.execute("INSERT INTO info VALUES('Nurjamal', 'Sipatdinova', 904688391 , '@nurjamalsipatdinova.com ' )")



# cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
# ati TEXT,
# fam TEXT,
# t_jil INTEGER,
# tel INTEGER,
# gmail TEXT
# )
# """)
def add(ati, fam, t_jil, tel, gmail):
    global cursor, db
    cursor.execute(f"INSERT INTO users VALUES ('{ati}', '{fam}', {t_jil}, {tel}, '{gmail}')")
    db.commit()

# add("Nurjamal", "Sipatdinova", 2004, 901234567, "nurjamalsipatdinova")
# add("Aygul", "Sarsenbaeva", 2004, 907654321, "aygulsarsenbaeva")
# add("Aynur", "Saparbaeva", 2001, 907654461, "aynursaparbaeva")



def oshiriw(name):
    cursor.execute(f"DELETE FROM users WHERE  ati = '{name}' ")
    db.commit()

# oshiriw("Nurjamal")



def ozgertiw(name, nomer, gmail):
    cursor.execute(f"UPDATE  users SET tel={nomer} , gmail='{gmail}' WHERE ati='{name}'")
    db. commit()
# ozgertiw("Aygul", 123456789, "ftfyjguikhyi")
