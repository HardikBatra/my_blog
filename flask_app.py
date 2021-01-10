from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
with open ('config.json','r') as r:
    params=json.load(r)["params"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = params['uri']
db = SQLAlchemy(app)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120),  nullable=False)
    content = db.Column(db.String(120),  nullable=False)
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120),  nullable=False)
    msg = db.Column(db.String(120),  nullable=False)
@app.route('/')
def index():
    posts=Posts.query.filter_by().all()
    return render_template('index.html',params=params,posts=posts)
@app.route('/about')
def about():
    return render_template('about.html',params=params)
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
    
    
    
    return render_template('contact.html',params=params)


@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html',params=params,post=post)
app.run(debug=True)