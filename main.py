from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogo.db'
app.config['UPLOAD_FOLDER'] = 'static/Img/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  
db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

class Catalogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String, nullable=False)
    Img = db.Column(db.String, nullable=False)
    Desc = db.Column(db.String, nullable=False)
    Valor = db.Column(db.String, nullable=False)

def formatar_valor(valor):
    try:
        valor_float = float(valor)
        return f"R$ {valor_float:,.2f}".replace(".", ",")
    except ValueError:
        return f"R$ {valor}"


@app.route('/')
def index():
    Plantas = Catalogo.query.all() 

    for planta in Plantas:
        planta.Valor = formatar_valor(planta.Valor)


    return render_template('index.html', Plantas=Plantas)

@app.route('/Client.html')
def adm():
    Plantas = Catalogo.query.all() 
    return render_template('Client.html', Plantas=Plantas)

@app.route('/criar', methods=['POST'])
def Criar():
    Nome = request.form['Nome']
    Img = request.files['Img']
    Desc = request.form['Desc']
    Valor = request.form['Valor']
    if Img and allowed_file(Img.filename):
        filename = secure_filename(Img.filename)
        Img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
        img_path = os.path.join('Img', filename)

        novo = Catalogo(Nome=Nome, Img=img_path, Desc=Desc, Valor=Valor)
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
                planta.Img = os.path.join('Img', filename)  # Atualiza apenas se o upload for bem-sucedido

        planta.Nome = request.form['Nome']
        planta.Desc = request.form['Desc']
        planta.Valor = request.form['Valor']
        db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
