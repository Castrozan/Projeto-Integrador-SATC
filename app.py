import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

#Função para conectar com o banco
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

#Atualmente não utilizada
#Função para pegar o ID dos Modulos
def get_post_modulos(post_id_modulos):
    conn = get_db_connection()
    post_modulos = conn.execute('SELECT * FROM modulos WHERE id_modulos = ?',
                        (post_id_modulos,)).fetchone()
    conn.close()
    if post_modulos is None:
        abort(404)
    return post_modulos

#Atualmente não utilizada
#Função para pegar o ID dos inversores
def get_post_inversores(post_id_inversores):
    conn = get_db_connection()
    post_inversores = conn.execute('SELECT * FROM inversores WHERE id_inversores = ?',
                        (post_id_inversores,)).fetchone()
    conn.close()
    if post_inversores is None:
        abort(404)
    return post_inversores

#Atualmente não utilizada
#Função para pegar o ID do consumo
def get_post_consumo(post_id_consumo):
    conn = get_db_connection()
    post_consumo = conn.execute('SELECT * FROM consumo_anual WHERE id_consumo_anual = ?',
                        (post_id_consumo,)).fetchone()
    conn.close()
    if post_consumo is None:
        abort(404)
    return post_consumo

#Função padrão para pegar o ID das postagens
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
    posts_inversores = conn.execute('SELECT * FROM inversores').fetchall()
    consumo = conn.execute('SELECT * FROM consumo_anual').fetchall()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    print('Atualização do Index')
    conn.close()
    return render_template('index.html', posts_modulos=posts_modulos, posts_inversores=posts_inversores, consumo=consumo, posts=posts)

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
        quantidade = request.form['quantidade']
        potencia = request.form['potencia']  

        if not modelo:
            flash('Modelo é nessário!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE modulos SET modelo = ?, quantidade = ?, potencia = ?'
                         ' WHERE id_modulos = ?',
                         (modelo, quantidade, potencia, id))
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
        quantidade = request.form['quantidade']
        potencia = request.form['potencia'] 

        if not modelo:
            flash('Modelo é nessário!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE inversores SET modelo = ?, quantidade = ?, potencia = ?'
                         ' WHERE id_inversores = ?',
                         (modelo, quantidade, potencia, id))
            conn.commit()
            conn.close()
            print('Banco atualizado')
            return redirect(url_for('index'))

    return render_template('edit_inversores.html', post_inversor=post_inversor)


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

#ROTA DO RELATÓRIO
@app.route('/google')
def gera_relatorio():
    return render_template('relatorio.html')

#ROTA DO SOBRE
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


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
