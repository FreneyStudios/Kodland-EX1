# Import
from flask import Flask, render_template,request, redirect
# Collegare la libreria del database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Connettere SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creare il DB
db = SQLAlchemy(app)
# Creare la tabella

class Card(db.Model):
    # Creazione delle colonne
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Titolo
    title = db.Column(db.String(100), nullable=False)
    # Sottotitolo
    subtitle = db.Column(db.String(300), nullable=False)
    # Testo
    text = db.Column(db.Text, nullable=False)

    # Visualizzazione dell'oggetto e dell'id
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Consegna #1. Creare la tabella User
class User(db.Model):
    # Creazione delle colonne
    # id
    id   = db.Column(db.Integer, primary_key=True)
    # Email
    login = db.Column(db.String(100), nullable=False)
    # Password
    password = db.Column(db.String(300), nullable=False)
    # Testo
    text = db.Column(db.Text, nullable=False)

    






# Esecuzione della pagina dei contenuti
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Consegna #2. Implementare l'autorizzazione
            users_db = User.query.all()

            for user in users_db:
                if form_login == user.login and form_password == user.password:
                    return redirect('/index')
            else:
                error = 'E-mail o password errate!'
                return render_template('login.html', error=error)

            
        else:
            return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login    = request.form['email']
        password = request.form['password']
        
        #Consegna #3. Fare in modo che i dati dell'utente vengano registrati nel database.
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# Esecuzione della pagina dei contenuti
@app.route('/index')
def index():
    # Visualizzazione delle voci del database
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Esecuzione della pagina con la voce
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Esecuzione della pagina di creazione della voce
@app.route('/create')
def create():
    return render_template('create_card.html')

# Il modulo di iscrizione
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Creare un oggetto che sarà inviato al DB
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')





if __name__ == "__main__":
    app.run(debug=True)