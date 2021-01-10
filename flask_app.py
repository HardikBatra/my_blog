from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
with open ('config.json','r') as r:
    params=json.load(r)["params"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = params['uri']
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120),  nullable=False)
    msg = db.Column(db.String(120),  nullable=False)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        msg=request.form.get('msg')
        entry=Contacts(name=name,email=email,phone=phone,msg=msg)
        db.session.add(entry)
        db.session.commit()
    
    
    
    return render_template('contact.html')
@app.route('/post')
def post():
    return render_template('post.html')


app.run(debug=True)