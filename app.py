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
        print('Solicitação de POST')

        #O ERRO ESTÁ AQUI!
        
        modelo = request.form['modelo']
        print('Aceito 1')
        quantidade = request.form['quantidade']
        print('Aceito 2')
        potencia = request.form['potencia']
        print('Aceito 3')
        print('Solicitação aceita')    

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