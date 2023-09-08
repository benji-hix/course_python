from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import author, book

@app.route('/authors')
#*insert routes, Class
def index():
    all_authors = author.Author.read_all()
    return render_template('author_all.html', all_authors = all_authors)


@app.route('/submit_author', methods = ['POST'])
#*insert routes, Class
def submit_author():
    author.Author.create(request.form)
    return redirect('/authors')


@app.route('/authors/<int:pk>')
def author_page(pk):
    author_data = author.Author.author_with_books(pk)
    all_books = book.Book.read_all()
    redirect_id = str(pk)
    return render_template('author_single.html', author_data = author_data, all_books = all_books, redirect_id=redirect_id)

@app.route('/add_book', methods=['POST'])
def add_book():
    author.Author.create_favorite_author(request.form)
    redirect_url = '/authors/' + str(request.form['form_author_id'])
    return redirect(redirect_url)