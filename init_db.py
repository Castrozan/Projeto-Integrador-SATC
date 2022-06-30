import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO modulos (modelo, potencia, tensao, corrente) VALUES (?, ?, ?, ?)",
            ('SunPower SPR-400E-WHT-D', '400', '85.3', '5.9')
            )

cur.execute("INSERT INTO inversores (modelo, potencia, tensao_max, tensao_min, corrente, mppts, quantidade) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('SMA America SB3800TL-US-22', '10000', '480', '100', '28.7897', '3', '2')
            )

cur.execute("INSERT INTO arranjos (numero_total_modulos, num_strings_mppt1, mod_strings_mppt1, azimute_mppt1, inclinacao_mppt1, num_strings_mppt2, mod_strings_mppt2, azimute_mppt2, inclinacao_mppt2, num_strings_mppt3, mod_strings_mppt3, azimute_mppt3, inclinacao_mppt3, num_strings_mppt4, mod_strings_mppt4, azimute_mppt4, inclinacao_mppt4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('48','2', '4', '0', '0', '2', '4', '0', '0','2', '4', '0', '0','0', '0', '0', '0')
            )

cur.execute("INSERT INTO consumo_anual (escola, janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('E.M.E.I.E.F Éricco Nonnemacher', '100', '100', '100', '100', '100', '100', '100', '100', '100', '100', '100', '100')
            )

cur.execute("INSERT INTO relatorios (notas_geracao, min_geracao, presente_geracao, max_geracao, notas_inversor, min_inversor, presente_inversor, max_inversor, notas_mppts, notas_tensao_mppt1, min_mppt1, presente_mppt1, max_mppt1, notas_corrente_mppt1, notas_tensao_mppt2, min_mppt2, presente_mppt2, max_mppt2, notas_corrente_mppt2, notas_tensao_mppt3, min_mppt3, presente_mppt3, max_mppt3, notas_corrente_mppt3, notas_tensao_mppt4, min_mppt4, presente_mppt4, max_mppt4, notas_corrente_mppt4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado', 'dado')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

connection.commit()
connection.close()