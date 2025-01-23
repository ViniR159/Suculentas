from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogo.db'
app.config['UPLOAD_FOLDER'] = 'static/Img/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}  
db = SQLAlchemy(app)

admUser = "123"
AdmSenha = 1234

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

class Catalogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String, nullable=False)
    Img = db.Column(db.String, nullable=False)
    Desc = db.Column(db.String, nullable=False)
    Quant = db.Column(db.String, nullable=False)
    Valor = db.Column(db.String, nullable=False)

def formatar_valor(Valor):
    try:
        valor_float = float(Valor)
        return f"{valor_float:,.2f}".replace(".", ",") 
    except ValueError:
        return f"{Valor}"

@app.route('/')
def index():
    Plantas = Catalogo.query.all() 

    for planta in Plantas:
        planta.Valor = formatar_valor(planta.Valor)


    return render_template('index.html', Plantas=Plantas)

@app.route('/Client.html')
def client():
    Plantas = Catalogo.query.all() 
    return render_template('Client.html', Plantas=Plantas)

@app.route('/Login', methods=['POST'])
def Login():
    User = request.form['User']
    Senha = request.form['Senha']
    if User == admUser and Senha == str(AdmSenha):
        return redirect('/')
    else:
        return redirect('/Client.html')

@app.route('/criar', methods=['POST'])
def Criar():
    Nome = request.form['Nome']
    Img = request.files['Img']
    Desc = request.form['Desc']
    Quant = request.form['Quant']
    Valor = request.form['Valor']
    if Img and allowed_file(Img.filename):
        filename = secure_filename(Img.filename)
        Img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
        img_path = os.path.join('Img', filename)

        novo = Catalogo(Nome=Nome, Img=img_path, Desc=Desc, Quant=Quant, Valor=Valor)
        db.session.add(novo)
        db.session.commit()
    return redirect('/')

@app.route('/delete/<int:Planta_Id>', methods=['POST'])
def Deletar(Planta_Id):
    planta = Catalogo.query.get(Planta_Id)

    if planta:
        db.session.delete(planta)
        db.session.commit()

    return redirect('/')

@app.route('/update/<int:Planta_Id>', methods=['POST'])
def Update(Planta_Id):
    planta = Catalogo.query.get(Planta_Id)

    if planta:
        if 'Img' in request.files:
            Img = request.files['Img']
            if Img and allowed_file(Img.filename):
                filename = secure_filename(Img.filename)
                Img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                planta.Img = os.path.join('Img', filename) 

        planta.Nome = request.form['Nome']
        planta.Desc = request.form['Desc']
        planta.Quant = request.form['Quant']
        planta.Valor = request.form['Valor']
        db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
