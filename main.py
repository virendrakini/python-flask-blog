from contextlib import redirect_stderr
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import session
from flask_mail import Mail
from datetime import datetime
import json
import os
import math
from werkzeug.utils import secure_filename

from os.path import dirname, join
current_dir = dirname(__file__)
filepath = join(current_dir, "./config.json")

with open(filepath, 'r') as c:
    params = json.load(c)['params']
local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['img_folder']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gamil-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/rkcomputer'
db = SQLAlchemy(app)

class Contacts(db.Model):
    contacts_id = db.Column(db.Integer, primary_key=True)
    contacts_name = db.Column(db.String(80), unique=False, nullable=False)
    contacts_email = db.Column(db.String(120), unique=False, nullable=False)
    contacts_phone = db.Column(db.String(120), unique=False, nullable=False)
    contacts_mesg = db.Column(db.String(120), unique=False, nullable=False)

class Posts(db.Model):
    post_id  = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(80), unique=False, nullable=False)
    post_description = db.Column(db.String(120), unique=False, nullable=False)
    post_slug = db.Column(db.String(120), unique=False, nullable=False)
    post_author = db.Column(db.String(120), unique=False, nullable=False)
    post_status = db.Column(db.String(120), unique=False, nullable=False)
    post_date  = db.Column(db.String(120), unique=False, nullable=False)
    post_img  = db.Column(db.String(120), unique=False, nullable=False)

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    if page==1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page==last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)
    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    if "user" in session and session['user']==params['admin_user']:
        posts = Posts.query.all()
        return render_template("dashboard.html", params=params, posts = posts)
    
    if request.method=="POST":
        username = request.form.get("uname")
        userpass = request.form.get("upass")
        if username==params['admin_user'] and userpass==params['admin_password']:
            session['user']=username
            posts = Posts.query.all()
            return render_template("dashboard.html", params=params, posts = posts)
        else:
            return render_template("login.html", params=params)
    else:
        return render_template("login.html", params=params)

@app.route("/contact", methods=['GET', 'POST','DELETE', 'PATCH'])
def contact():
    if(request.method=='POST'):
        contacts_name = request.form.get('contacts_name')
        contacts_email = request.form.get('contacts_email')
        contacts_phone = request.form.get('contacts_phone')
        contacts_mesg = request.form.get('contacts_mesg')
        #date= datetime.now()
        entry = Contacts(contacts_name=contacts_name,contacts_email=contacts_email,contacts_phone=contacts_phone,contacts_mesg=contacts_mesg)
        db.session.add(entry)
        db.session.commit()
        mail.send_message(  'New Message from ' + contacts_name, 
                            sender = contacts_email,
                            recipients = [params['gamil-user']],
                            body = contacts_mesg + "\n phone no : " + contacts_phone +  "\n email : " + contacts_email
                          )
    return render_template('contact.html')

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(post_slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/edit/<string:srno>", methods=['GET', 'POST'])
def edit_posts(srno):
    if "user" in session and session['user']==params['admin_user']:
        if request.method == 'POST':
            post_title = request.form.get('post_title')
            post_slug = request.form.get('post_slug')
            post_author = request.form.get('post_author')
            post_img = request.form.get('post_img')
            post_description = request.form.get('post_description')
            post_status = request.form.get('post_status')
            post_date = datetime.now()
            
            if srno =='0':
                post = Posts(post_title = post_title, post_description = post_description, post_slug = post_slug, post_author=post_author , post_date=post_date,post_img = post_img, post_status = post_status)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(post_id=srno).first()
                post.post_title = post_title
                post.post_slug = post_slug
                post.post_author = post_author
                post.post_img = post_img
                post.post_description = post_description
                post.post_status = post_status
                post.post_date = post_date
                db.session.commit()
                return redirect('/edit/'+srno)

        post = Posts.query.filter_by(post_id = srno).first()       
        return render_template('edit.html' , srno=srno , post = post)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route('/delete/<string:srno>', methods=['GET','POST'])
def delete(srno):
    if "user" in session and session['user']==params['admin_user']:
        post = Posts.query.filter_by(post_id=srno).first()
        db.session.delete(post)
        db.session.commit()

    return redirect('/dashboard')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if "user" in session and session['user']==params['admin_user']:
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully!"

app.run(debug=True)