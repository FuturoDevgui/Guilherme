from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(_name_)
app.config['SECRET_KEY'] = 'testando321'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=["POST"])
def login():

    usuario = request.form.get('nome')
    senha = request.form.get('senha')

    if usuario == 'usuario.teste' and senha == 'testando321':
            return render_template("home.html")
    else:
            return render_template("login.html")


if _name_ in "_main_":
    app.run(debug=True)
