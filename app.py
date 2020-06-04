"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (os.environ.get(
    'DATABASE_URL', 'postgres:///blogly'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'marcoNharryMUHAHA'

connect_db(app)
db.create_all()


@app.route('/')
def show_users():
    users = User.query.all()
    return render_template('index.jinja', users=users)


@app.route('/add-user')
def add_user():
    return render_template('add-user.jinja', user={})


@app.route('/add-user', methods=["POST"])
def save_user():
    form_values = {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'image_url': request.form.get('image_url', '')
    }
    user = User(**form_values)
    db.session.add(user)
    db.session.commit()
    return redirect('/')


@app.route('/user/<int:id>')
def show_user_details(id):
    user = User.query.get_or_404(id)
    return render_template('user-details.jinja', user=user)


@app.route('/edit-user/<int:id>')
def edit_user_detail(id):
    user = User.query.get_or_404(id)
    return render_template('edit-user.jinja', user=user)


@app.route('/edit-user/<int:id>', methods=["POST"])
def update_user(id):
    user = User.query.get_or_404(id)
    user.first_name = request.form.get('first_name')
    user.last_name = request.form.get('last_name')
    user.image_url = request.form.get('image_url')
    db.session.commit()
    return redirect(f'/user/{user.id}')


@app.route('/delete-user/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash(f"User {user.first_name} {user.last_name} deleted!")
    return redirect('/')


@app.route('/add-post/<int:id>')
def add_post(id):
    user = User.query.get_or_404(id)
    return render_template('add-post.jinja', user=user)


@app.route('/add-post/<int:id>', methods=["POST"])
def save_post(id):
    form_values = {
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'user_id': id
    }
    post = Post(**form_values)
    db.session.add(post)
    db.session.commit()
    return redirect(f'/post/{post.id}')


@app.route('/post/<int:id>')
def show_post(id):
    post = Post.query.get_or_404(id)
    return render_template('show-post.jinja', post=post)


@app.route('/edit-post/<int:id>')
def edit_post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template('edit-post.jinja', post=post)


@app.route('/edit-post/<int:id>', methods=["POST"])
def update_post(id):
    post = Post.query.get_or_404(id)
    post.title = request.form.get('title')
    post.content = request.form.get('content')
    db.session.commit()
    return redirect(f'/post/{post.id}')


@app.route('/delete-post/<int:id>')
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title}' deleted!")
    return redirect('/')
