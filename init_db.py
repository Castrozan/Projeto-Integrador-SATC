import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO modulos (modelo, quantidade, potencia) VALUES (?, ?, ?)",
            ('SunPower SPR-400E-WHT-D', '48', '400W')
            )

cur.execute("INSERT INTO inversores (modelo, quantidade, potencia) VALUES (?, ?, ?)",
            ('SMA America SB3800TL-US-22', '4', '3800W')
            )

cur.execute("INSERT INTO consumo_anual (escola, janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('E.M.E.I.E.F Éricco Nonnemacher', '100', '100', '100', '100', '100', '100', '100', '100', '100', '100', '100', '100')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

connection.commit()
connection.close()