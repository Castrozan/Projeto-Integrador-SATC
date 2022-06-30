import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

#Função para conectar com o banco
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#Função para pegar o post Modulos
def get_post_modulos(post_id_modulos):
    conn = get_db_connection()
    post_modulos = conn.execute('SELECT * FROM modulos WHERE id_modulos = ?',
                        (post_id_modulos,)).fetchone()
    conn.close()
    if post_modulos is None:
        print('não tem nada')
        abort(404)
    return post_modulos

#Função para pegar o post inversores
def get_post_inversores(post_id_inversores):
    conn = get_db_connection()
    post_inversores = conn.execute('SELECT * FROM inversores WHERE id_inversores = ?',
                        (post_id_inversores,)).fetchone()
    conn.close()
    if post_inversores is None:
        abort(404)
    return post_inversores

#Função para pegar post arranjos
def get_post_arranjos(post_id_arranjos):
    conn = get_db_connection()
    post_arranjos = conn.execute('SELECT * FROM arranjos WHERE id_arranjos = ?',
                        (post_id_arranjos,)).fetchone()
    conn.close()
    if post_arranjos is None:
        abort(404)
    return post_arranjos


#Função para pegar post consumo
def get_post_consumo(post_id_consumo):
    conn = get_db_connection()
    post_consumo = conn.execute('SELECT * FROM consumo_anual WHERE id_consumo_anual = ?',
                        (post_id_consumo,)).fetchone()
    conn.close()
    if post_consumo is None:
        abort(404)
    return post_consumo

#Função para pegar o post relatorios
def get_post_relatorios(post_id_relatorio):
    conn = get_db_connection()
    post_relatorio = conn.execute('SELECT * FROM relatorios WHERE id_relatorios = ?',
                        (post_id_relatorio,)).fetchone()
    conn.close()
    if post_relatorio is None:
        print('não tem nada')
        abort(404)
    return post_relatorio

#Função padrão para pegar as postagens
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)

#Rota do INDEX
@app.route('/')
def index():
    conn = get_db_connection()
    posts_modulos = conn.execute('SELECT * FROM modulos').fetchall()
    #print(type(posts_modulos))
    posts_inversores = conn.execute('SELECT * FROM inversores').fetchall()
    posts_arranjos = conn.execute('SELECT * FROM arranjos').fetchall()
    consumo = conn.execute('SELECT * FROM consumo_anual').fetchall()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    print('Atualização do Index')
    conn.close()
    return render_template('index.html', posts_modulos=posts_modulos, posts_inversores=posts_inversores, posts_arranjos=posts_arranjos, consumo=consumo, posts=posts)

#ROTAS PARA OS MODULOS
#Rota para a visualização de modulos
@app.route('/post_id_modulos')
def post_modulo():
    id = 1
    post_modulo = get_post_modulos(id)
    return render_template('post_modulos.html', post_modulo=post_modulo)

#Rota para edição de modulos
@app.route('/edit_modulos', methods=('GET', 'POST'))
def edit_modulos():
    id = 1
    post_modulo = get_post_modulos(id)
    print('Rota de edição de modulos')

    if request.method == 'POST':
        modelo = request.form['modelo']
        potencia = request.form['potencia']
        tensao = request.form['tensao']
        corrente = request.form['corrente']

        if not modelo:
            flash('Modelo é nessário!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE modulos SET modelo = ?, potencia = ?, tensao = ?, corrente = ?'
                         ' WHERE id_modulos = ?',
                         (modelo, potencia, tensao, corrente, id))
            conn.commit()
            conn.close()
            print('Banco atualizado')
            return redirect(url_for('index'))

    return render_template('edit_modulos.html', post_modulo=post_modulo)

#ROTAS PARA OS INVERSORES
#Rota para a visualização de inversores
@app.route('/post_id_inversores')
def post_inversor():
    id = 1
    post_inversor = get_post_inversores(id)
    return render_template('post_inversores.html', post_inversor=post_inversor)

#Rota para edição de inversores
@app.route('/edit_inversores', methods=('GET', 'POST'))
def edit_inversores():
    id = 1
    post_inversor = get_post_inversores(id)
    print('Rota de edição de inversores')

    if request.method == 'POST':
        modelo = request.form['modelo']
        potencia = request.form['potencia']
        tensao_max = request.form['tensao_max']
        tensao_min = request.form['tensao_min']
        corrente = request.form['corrente']
        mppts = request.form['mppts'] 
        quantidade = request.form['quantidade'] 

        if not modelo:
            flash('Modelo é nessário!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE inversores SET modelo = ?, potencia = ?, tensao_max = ?, tensao_min = ?, corrente = ?, mppts = ?, quantidade = ?'
                         ' WHERE id_inversores = ?',
                         (modelo, potencia, tensao_max, tensao_min, corrente, mppts, quantidade, id))
            conn.commit()
            conn.close()
            print('Banco atualizado')
            return redirect(url_for('index'))

    return render_template('edit_inversores.html', post_inversor=post_inversor)

#ROTAS PARA OS ARRANJOS
#Rota para a visualização de arranjos
@app.route('/post_id_arranjos')
def post_arranjo():
    id = 1
    post_arranjo = get_post_arranjos(id)
    return render_template('post_arranjos.html', post_arranjo=post_arranjo)

#Rota para edição de arranjos
@app.route('/edit_arranjos', methods=('GET', 'POST'))
def edit_arranjos():
    id = 1
    post_arranjo = get_post_arranjos(id)
    print('Rota de edição de arranjos')

    if request.method == 'POST':
        numero_total_modulos = request.form['numero_total_modulos']
        num_strings_mppt1 = request.form['num_strings_mppt1']
        mod_strings_mppt1 = request.form['mod_strings_mppt1']
        azimute_mppt1 = request.form['azimute_mppt1']
        inclinacao_mppt1 = request.form['inclinacao_mppt1']

        num_strings_mppt2 = request.form['num_strings_mppt2']
        mod_strings_mppt2 = request.form['mod_strings_mppt2'] 
        azimute_mppt2 = request.form['azimute_mppt2'] 
        inclinacao_mppt2 = request.form['inclinacao_mppt2'] 

        num_strings_mppt3 = request.form['num_strings_mppt3'] 
        mod_strings_mppt3 = request.form['mod_strings_mppt3'] 
        azimute_mppt3 = request.form['azimute_mppt3'] 
        inclinacao_mppt3 = request.form['inclinacao_mppt3'] 

        num_strings_mppt4 = request.form['num_strings_mppt4'] 
        mod_strings_mppt4 = request.form['mod_strings_mppt4'] 
        azimute_mppt4 = request.form['azimute_mppt4'] 
        inclinacao_mppt4 = request.form['inclinacao_mppt4'] 

        if not num_strings_mppt1:
            flash('num_strings_mppt1 é nessário!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE arranjos SET numero_total_modulos = ?, num_strings_mppt1 = ?, mod_strings_mppt1 = ?, azimute_mppt1 = ?, inclinacao_mppt1 = ?, num_strings_mppt2 = ?, mod_strings_mppt2 = ?, azimute_mppt2 = ?, inclinacao_mppt2 = ?, num_strings_mppt3 = ?, mod_strings_mppt3 = ?, azimute_mppt3 = ?, inclinacao_mppt3 = ?, num_strings_mppt4 = ?, mod_strings_mppt4 = ?, azimute_mppt4 = ?, inclinacao_mppt4 = ?'
                         ' WHERE id_arranjos = ?',
                         (numero_total_modulos, num_strings_mppt1, mod_strings_mppt1, azimute_mppt1, inclinacao_mppt1, num_strings_mppt2, mod_strings_mppt2, azimute_mppt2, inclinacao_mppt2, num_strings_mppt3, mod_strings_mppt3, azimute_mppt3, inclinacao_mppt3, num_strings_mppt4, mod_strings_mppt4, azimute_mppt4, inclinacao_mppt4, id))
            conn.commit()
            conn.close()
            print('Banco atualizado')
            return redirect(url_for('index'))

    return render_template('edit_arranjos.html', post_arranjo=post_arranjo)

#ROTAS PARA O CONSUMO
#Rota para a visualização do consumo
@app.route('/post_id_consumo')
def post_consumo():
    id = 1
    post_consumo = get_post_consumo(id)
    return render_template('post_consumo.html', post_consumo=post_consumo)

#Rota para edição de consumo
@app.route('/edit_consumo', methods=('GET', 'POST'))
def edit_consumo():
    id = 1
    post_consumo = get_post_consumo(id)
    print('Rota de edição do consumo')

    if request.method == 'POST':
        escola = request.form['escola']
        janeiro = request.form['janeiro']
        fevereiro = request.form['fevereiro']
        marco = request.form['marco']
        abril = request.form['abril']
        maio = request.form['maio']
        junho = request.form['junho']
        julho = request.form['julho']
        agosto = request.form['agosto']
        setembro = request.form['setembro']
        outubro = request.form['outubro']
        novembro = request.form['novembro']
        dezembro = request.form['dezembro']

        if not escola:
            flash('Modelo é nessário!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE consumo_anual SET escola = ?, janeiro = ?, fevereiro = ?, marco = ?, abril = ?, maio = ?, junho = ?, julho = ?, agosto = ?, setembro = ?, outubro = ?, novembro = ?, dezembro = ?'
                         ' WHERE id_consumo_anual = ?',
                         (escola, janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro, id))
            conn.commit()
            conn.close()
            print('Banco atualizado')
            return redirect(url_for('index'))

    return render_template('edit_consumo.html', post_consumo=post_consumo)

#ROTA DO SOBRE
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

#ROTA DO RELATÓRIO
@app.route('/relatorio')
def gera_relatorio():
    id = 1

    #Dados gerais
    irradiacao_local = 4.38
    temperatura_minima_ambiente = 0.00
    constante_gstc = 1.00
    taxa_desempenho_sistema = 0.80

    # Dados modulos
    print('# Dados modulos')
    potencia_maxima_modulo = 0
    tensao_modulo_ca = 0 
    corrente_cc = 0

    conn = get_db_connection()
    records = conn.execute('SELECT * from modulos').fetchall()
    for row in records:
        potencia_maxima_modulo = float(row[3])
        tensao_modulo_ca = float(row[4])
        corrente_cc = float(row[5])
    conn.close()

    print('potencia_maxima_modulo',potencia_maxima_modulo)
    print('tensao_modulo_ca',tensao_modulo_ca)
    print('corrente_cc',corrente_cc)

    #Dados do inversor 
    print('#Dados do inversor ')
    potencia_maxima_inversor = 0
    tensao_maxima_mppt = 0
    tensao_minima_mppt = 0
    corrente_maxima_mppt = 0
    numero_mppt = 0
    quantidade_inversores = 0

    conn = get_db_connection()
    records = conn.execute('SELECT * from inversores').fetchall()
    for row in records:
        potencia_maxima_inversor = float(row[3])
        tensao_maxima_mppt = float(row[4])
        tensao_minima_mppt = float(row[5])
        corrente_maxima_mppt = float(row[6])
        numero_mppt = float(row[7])
        quantidade_inversores = float(row[8])
    conn.close()

    print('potencia_maxima_inversor',potencia_maxima_inversor)
    print('tensao_maxima_mppt',tensao_maxima_mppt)
    print('tensao_minima_mppt',tensao_minima_mppt)
    print('corrente_maxima_mppt',corrente_maxima_mppt)
    print('numero_mppt',numero_mppt)
    print('quantidade_inversores',quantidade_inversores)

    #Dados do inversor 
    print('#Dados do inversor ')
    potencia_maxima_inversor = 0
    tensao_maxima_mppt = 0
    tensao_minima_mppt = 0
    corrente_maxima_mppt = 0
    numero_mppt = 0
    quantidade_inversores = 0

    conn = get_db_connection()
    records = conn.execute('SELECT * from inversores').fetchall()
    for row in records:
        potencia_maxima_inversor = float(row[3])
        tensao_maxima_mppt = float(row[4])
        tensao_minima_mppt = float(row[5])
        corrente_maxima_mppt = float(row[6])
        numero_mppt = float(row[7])
        quantidade_inversores = float(row[8])
    conn.close()

    print('potencia_maxima_inversor',potencia_maxima_inversor)
    print('tensao_maxima_mppt',tensao_maxima_mppt)
    print('tensao_minima_mppt',tensao_minima_mppt)
    print('corrente_maxima_mppt',corrente_maxima_mppt)
    print('numero_mppt',numero_mppt)
    print('quantidade_inversores',quantidade_inversores)

    # Dados consumo_anual

    consumo_total_energia = 0

    conn = get_db_connection()
    records = conn.execute('SELECT * from consumo_anual').fetchall()
    for row in records:
        janeiro = float(row[2])
        fevereiro = float(row[3])
        marco = float(row[4])
        abril = float(row[5])
        maio = float(row[6])
        junho = float(row[7])
        julho = float(row[8])
        agosto = float(row[9])
        setembro = float(row[10])
        outubro = float(row[11])
        novembro = float(row[12])
        dezembro = float(row[13])

    conn.close()

    consumo_total_energia = janeiro + fevereiro + marco + abril + maio + junho + julho + agosto + setembro + outubro + novembro + dezembro

    print('consumo_total_energia',consumo_total_energia)

    # Dados MPPT
    print('# Dados MPPT')
    capacidade_cc = 19200
    capacidade_ca = 20000
    numero_maximo_strings = 4
    numero_maximo_strings = 5

    # Dados dos arranjos | se tiver tudo 0 o mppt não será utilizado
    numero_total_modulos = 0

    #mppt 1
    numero_strings_mppt1 = 0
    numero_modulo_mppt1 = 0
    azimute_mppt1 = 0 
    inclinacao_mppt1 = 0

    #mppt 2
    numero_strings_mppt2 = 0
    numero_modulo_mppt2 = 0
    azimute_mppt2 = 0 
    inclinacao_mppt2 = 0 

    #mppt 3
    numero_strings_mppt3 = 0
    numero_modulo_mppt3 = 0
    azimute_mppt3 = 0 
    inclinacao_mppt3 = 0 

    #mppt 4
    numero_strings_mppt4 = 0 
    numero_modulo_mppt4 = 0 
    azimute_mppt4 = 0 
    inclinacao_mppt4 = 0 

    conn = get_db_connection()
    records = conn.execute('SELECT * from arranjos').fetchall()
    for row in records:
        numero_total_modulos = float(row[2])
        
        numero_strings_mppt1 = float(row[3])
        numero_modulo_mppt1 = float(row[4])
        azimute_mppt1 = float(row[5])
        inclinacao_mppt1 = float(row[6])

        numero_strings_mppt2 = float(row[7])
        numero_modulo_mppt2 = float(row[8])
        azimute_mppt2 = float(row[9])
        inclinacao_mppt2 = float(row[10])

        numero_strings_mppt3 = float(row[11])
        numero_modulo_mppt3 = float(row[12])
        azimute_mppt3 = float(row[13])
        inclinacao_mppt3 = float(row[14])

        numero_strings_mppt4 = float(row[15])
        numero_modulo_mppt4 = float(row[16])
        azimute_mppt4 = float(row[17])
        inclinacao_mppt4 = float(row[18])
    conn.close()

    print('numero_total_modulos',numero_total_modulos)

    print('numero_strings_mppt1',numero_strings_mppt1)
    print('numero_modulo_mppt1',numero_modulo_mppt1)
    print('azimute_mppt1',azimute_mppt1)
    print('inclinacao_mppt1',inclinacao_mppt1)

    print('numero_strings_mppt2',numero_strings_mppt2)
    print('numero_modulo_mppt2',numero_modulo_mppt2)
    print('azimute_mppt2',azimute_mppt2)
    print('inclinacao_mppt2',inclinacao_mppt2)

    print('numero_strings_mppt3',numero_strings_mppt3)
    print('numero_modulo_mppt3',numero_modulo_mppt3)
    print('azimute_mppt3',azimute_mppt3)
    print('inclinacao_mppt3',inclinacao_mppt3)

    print('numero_strings_mppt4',numero_strings_mppt4)
    print('numero_modulo_mppt4',numero_modulo_mppt4)
    print('azimute_mppt4',azimute_mppt4)
    print('inclinacao_mppt4',inclinacao_mppt4)

    # SAÍDAS RELATÓRIO
    # GERAÇÃO FOTOVOLTAICA
    print('GERAÇÃO FOTOVOLTAICA')
    if consumo_total_energia/12 > (numero_total_modulos*potencia_maxima_modulo*30*irradiacao_local*taxa_desempenho_sistema/(constante_gstc*1000)):
        notas_geracao = 'ADICIONAR MAIS MÓDULOS'
    elif (numero_total_modulos*potencia_maxima_modulo*30*irradiacao_local*taxa_desempenho_sistema/(constante_gstc*1000))>1.2*consumo_total_energia/12:
        notas_geracao = 'REDUZIR MÓDULOS'
    else:
        notas_geracao = 'VÁLIDA'

    print('notas_geracao', notas_geracao)

    min_geracao = consumo_total_energia
    presente_geracao = (numero_total_modulos*potencia_maxima_modulo*30*irradiacao_local*taxa_desempenho_sistema/(constante_gstc*1000))*12
    max_geracao = min_geracao*1.2
    print('min_geracao ',min_geracao )
    print('presente_geracao ',presente_geracao )
    print('max_geracao ',max_geracao )

    #POTÊNCIA DO INVERSOR
    print('#POTÊNCIA DO INVERSOR ' )
    if potencia_maxima_modulo*numero_total_modulos*0.8 > potencia_maxima_inversor*quantidade_inversores:
        notas_inversor = 'DIMENSIONAR INVERSOR DE MAIOR POTÊNCIA'
    elif potencia_maxima_inversor*quantidade_inversores*0.8 > potencia_maxima_modulo*numero_total_modulos:
        notas_inversor = 'DIMENSIONAR INVERSOR DE MENOR POTÊNCIA'
    else:
        notas_inversor = 'VÁLIDA'

    print('notas_inversor ',notas_inversor )

    min_inversor = numero_total_modulos*potencia_maxima_modulo*0.8
    presente_inversor = potencia_maxima_inversor*quantidade_inversores
    max_inversor = numero_total_modulos*potencia_maxima_modulo*1.2

    print('min_inversor ',min_inversor )
    print('presente_inversor ',presente_inversor )
    print('max_inversor ',max_inversor )

    # Validação de quantidade de MPPTs
    print('# Validação de quantidade de MPPTs ' )

    if numero_total_modulos != quantidade_inversores*(numero_strings_mppt1*numero_modulo_mppt1+numero_strings_mppt2*numero_modulo_mppt2+numero_strings_mppt3*numero_modulo_mppt3+numero_strings_mppt4*numero_modulo_mppt4):
        notas_mppts = 'NÚMERO DE MÓDULOS NOS ARRANJOS DIFERENTE DO NÚMERO DE MÓDULOS DEFINIDO PARA O SISTEMA'
    elif numero_mppt == 1:
        if numero_strings_mppt2*numero_modulo_mppt2+numero_strings_mppt3*numero_modulo_mppt3+numero_strings_mppt4*numero_modulo_mppt4 == 0 and numero_strings_mppt1*numero_modulo_mppt1 > 0:
            notas_mppts = 'VÁLIDA'
        else:
            notas_mppts = 'MÓDULOS DISPOSTOS INCORRETAMENTE NOS MPPTs'
    elif numero_mppt == 2:
        if numero_strings_mppt3*numero_modulo_mppt3+numero_strings_mppt4*numero_modulo_mppt4 == 0 and numero_strings_mppt1*numero_modulo_mppt1 > 0 and numero_strings_mppt2*numero_modulo_mppt2 > 0:
            notas_mppts = 'VÁLIDA'
        else:
            notas_mppts = 'MÓDULOS DISPOSTOS INCORRETAMENTE NOS MPPTs'
    elif numero_mppt == 3:
        if numero_strings_mppt4*numero_modulo_mppt4 == 0 and numero_strings_mppt1*numero_modulo_mppt1 > 0 and numero_strings_mppt2*numero_modulo_mppt2 > 0 and numero_strings_mppt3*numero_modulo_mppt3 > 0:
            notas_mppts = 'VÁLIDA'
        else:
            notas_mppts = 'MÓDULOS DISPOSTOS INCORRETAMENTE NOS MPPTs'
    elif numero_strings_mppt1*numero_modulo_mppt1 != 0 and numero_strings_mppt3*numero_modulo_mppt3 != 0 and numero_strings_mppt3*numero_modulo_mppt3 != 0 and numero_strings_mppt4*numero_modulo_mppt4 != 0:
        notas_mppts = 'VÁLIDA'
    else:
        notas_mppts = 'MÓDULOS DISPOSTOS INCORRETAMENTE NOS MPPTs'
    print('notas_mppts ',notas_mppts )

    # MPPT 1

    # TENSÃO DE OPERAÇÃO NO MPPTs
    print('# TENSÃO DE OPERAÇÃO NO MPPTs 1 ' )
    if numero_modulo_mppt1*tensao_modulo_ca > tensao_maxima_mppt:
        notas_tencao_mppt1 = 'REDUZIR MÓDULOS POR STRING'
    elif tensao_modulo_ca*numero_modulo_mppt1 < tensao_minima_mppt:
        notas_tensao_mppt1 = 'ADICIONAR MAIS MÓDULOS POR STRING'
    else:
        notas_tensao_mppt1 = 'VÁLIDA'
    print('notas_tensao_mppt1 ',notas_tensao_mppt1 )

    min_mppt1 = tensao_minima_mppt
    presente_mppt1 = tensao_modulo_ca*numero_modulo_mppt1
    max_mppt1 = tensao_maxima_mppt
    print('min_mppt1 ',min_mppt1 )
    print('presente_mppt1 ',presente_mppt1 )
    print('max_mppt1 ',max_mppt1 )

    # CORRENTE DE OPERAÇÃO NO MPPTs
    print('# CORRENTE DE OPERAÇÃO NO MPPTs 1' )
    if corrente_cc*numero_strings_mppt1>corrente_maxima_mppt:
        notas_corrente_mppt1 = 'CORRENTE ELEVADA - REDUZIR QUANTIDADE DE STRINGS'
    else:
        notas_corrente_mppt1 = 'VÁLIDA'

    print('notas_corrente_mppt1 ',notas_corrente_mppt1 )

    # MPPT 2

    # TENSÃO DE OPERAÇÃO NO MPPTs
    print('# TENSÃO DE OPERAÇÃO NO MPPTs 2' )
    if numero_mppt > 1:
        if numero_mppt > 1:
            if numero_modulo_mppt2*tensao_modulo_ca > tensao_maxima_mppt:
                notas_tensao_mppt2 = 'REDUZIR MÓDULOS POR STRING'
            else:
                if tensao_modulo_ca*numero_modulo_mppt2 < tensao_minima_mppt:
                    notas_tensao_mppt2 = 'ADICIONAR MAIS MÓDULOS POR STRING'
                else:
                    notas_tensao_mppt2 = 'VÁLIDA'
        else:
            notas_tensao_mppt2 = 'VÁLIDA'
    else:
        notas_tensao_mppt2 = 'VÁLIDA'

    print('notas_tensao_mppt2 ',notas_tensao_mppt2 )

    min_mppt2 = tensao_minima_mppt
    presente_mppt2 = tensao_modulo_ca*numero_modulo_mppt2
    max_mppt2 = tensao_maxima_mppt
    print('min_mppt2 ',min_mppt2 )
    print('presente_mppt2 ',presente_mppt2 )
    print('max_mppt2 ',max_mppt2 )

    # CORRENTE DE OPERAÇÃO NO MPPTs
    print('# CORRENTE DE OPERAÇÃO NO MPPTs 2' )
    if numero_mppt > 1:
        if corrente_cc*numero_strings_mppt2 > corrente_maxima_mppt:
            notas_corrente_mppt2 = 'CORRENTE ELEVADA - REDUZIR QUANTIDADE DE STRINGS'
        else:
            notas_corrente_mppt2 = 'VÁLIDA'
    else: 
        notas_corrente_mppt2 = 'VÁLIDA'
    print('notas_corrente_mppt2 ',notas_corrente_mppt2 )

    # MPPT 3

    # TENSÃO DE OPERAÇÃO NO MPPTs
    print('# TENSÃO DE OPERAÇÃO NO MPPTs 3' )
    if numero_mppt > 2:
        if numero_modulo_mppt3*tensao_modulo_ca > tensao_maxima_mppt:
            notas_tensao_mppt3 = 'REDUZIR MÓDULOS POR STRING'
        else:
            if tensao_modulo_ca*numero_modulo_mppt3 < tensao_minima_mppt:
                notas_tensao_mppt3 = 'ADICIONAR MAIS MÓDULOS POR STRING'
            else:
                notas_tensao_mppt3 = 'VÁLIDA'
    else:
        notas_tensao_mppt3 = 'VÁLIDA'
    print('notas_tensao_mppt3 ',notas_tensao_mppt3 )

    min_mppt3 = tensao_minima_mppt
    presente_mppt3 = tensao_modulo_ca*numero_modulo_mppt3
    max_mppt3 = tensao_maxima_mppt
    print('min_mppt3 ',min_mppt3 )
    print('presente_mppt3 ',presente_mppt3 )
    print('max_mppt3 ',max_mppt3 )

    # CORRENTE DE OPERAÇÃO NO MPPTs
    print('# CORRENTE DE OPERAÇÃO NO MPPTs 3' )
    if numero_mppt > 2:
        if  corrente_cc*numero_strings_mppt3 > corrente_maxima_mppt:
            notas_corrente_mppt3 = 'CORRENTE ELEVADA - REDUZIR QUANTIDADE DE STRINGS'
        else:
            notas_corrente_mppt3 = 'VÁLIDA'
    else:
        notas_corrente_mppt3 = 'VÁLIDA'
    print('notas_corrente_mppt3 ', notas_corrente_mppt3)

    # MPPT 4

    # TENSÃO DE OPERAÇÃO NO MPPTs
    print('# TENSÃO DE OPERAÇÃO NO MPPTs 4' )
    if numero_mppt > 3:
        if numero_modulo_mppt4*tensao_modulo_ca > tensao_maxima_mppt:
            notas_tensao_mppt4 = 'REDUZIR MÓDULOS POR STRING'
        else:
            if tensao_modulo_ca*numero_modulo_mppt4 < tensao_minima_mppt:
                notas_tensao_mppt4 = 'ADICIONAR MAIS MÓDULOS POR STRING'
            else:
                notas_tensao_mppt4 = 'VÁLIDA' 
    else:
        notas_tensao_mppt4 = 'VÁLIDA'
    print('notas_tensao_mppt4 ',notas_tensao_mppt4 )

    min_mppt4 = tensao_minima_mppt
    presente_mppt4 = tensao_modulo_ca*numero_modulo_mppt4
    max_mppt4 = tensao_maxima_mppt
    print('min_mppt4 ',min_mppt4 )
    print('presente_mppt4 ',presente_mppt4 )
    print('max_mppt4 ',max_mppt4 )

    # CORRENTE DE OPERAÇÃO NO MPPTs
    print('# CORRENTE DE OPERAÇÃO NO MPPTs 4' )
    if numero_mppt > 3:
        if corrente_cc*numero_strings_mppt4 > corrente_maxima_mppt:
            notas_corrente_mppt4 = 'CORRENTE ELEVADA - REDUZIR QUANTIDADE DE STRINGS'
        else:
            notas_corrente_mppt4 = 'VÁLIDA'
    else: 
        notas_corrente_mppt4 = 'VÁLIDA'

    print('notas_corrente_mppt4 ',notas_corrente_mppt4 )

    conn = get_db_connection()
    conn.execute('UPDATE relatorios SET notas_geracao = ?, min_geracao = ?, presente_geracao = ?, max_geracao = ?, notas_inversor = ?, min_inversor = ?, presente_inversor = ?, max_inversor = ?, notas_mppts = ?, notas_tensao_mppt1 = ?, min_mppt1 = ?, presente_mppt1 = ?, max_mppt1 = ?, notas_corrente_mppt1 = ?, notas_tensao_mppt2 = ?, min_mppt2 = ?, presente_mppt2 = ?, max_mppt2 = ?, notas_corrente_mppt2 = ?, notas_tensao_mppt3 = ?, min_mppt3 = ?, presente_mppt3 = ?, max_mppt3 = ?, notas_corrente_mppt3 = ?, notas_tensao_mppt4 = ?, min_mppt4 = ?, presente_mppt4 = ?, max_mppt4 = ?, notas_corrente_mppt4 = ?'
                    ' WHERE id_relatorios = ?',
                    (notas_geracao, min_geracao, presente_geracao, max_geracao, notas_inversor, min_inversor, presente_inversor, max_inversor, notas_mppts, notas_tensao_mppt1, min_mppt1, presente_mppt1, max_mppt1, notas_corrente_mppt1, notas_tensao_mppt2, min_mppt2, presente_mppt2, max_mppt2, notas_corrente_mppt2, notas_tensao_mppt3, min_mppt3, presente_mppt3, max_mppt3, notas_corrente_mppt3, notas_tensao_mppt4, min_mppt4, presente_mppt4, max_mppt4, notas_corrente_mppt4, id))
    conn.commit()
    conn.close()

    post_relatorio = get_post_relatorios(id)

    return render_template('relatorio.html', post_relatorio=post_relatorio)
    

#ROTAS ABAIXO SÃO PARA AS POSTAGENS ORIGINAIS
#Rota padrão para a visualização de postagens
@app.route('/<int:post_id>')
def post(post_id):
    print(post_id)
    post = get_post(post_id)
    return render_template('post.html', post=post)

#Rota padrão para edição de postagens
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    print('Rota de edição padrão')

    if request.method == 'POST':
        print('Solicitação padrão de post')
        title = request.form['title']
        print(title)
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            print('banco padrão atualizado')
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

#Rota padrão para deleção de postagens
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

print('Atualização do BackEnd')
