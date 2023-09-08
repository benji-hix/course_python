from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import author, book

@app.route('/books')
#*insert routes, Class
def books_home():
    all_books = book.Book.read_all()
    return render_template('book_all.html', all_books=all_books)


@app.route('/submit_book', methods = ['POST'])
#*insert routes, Class
def submit_book():
    book.Book.create(request.form)
    return redirect('/books')

@app.route('/books/<int:pk>')
def book_page(pk):
    book_data = book.Book.book_with_authors(pk)
    all_authors = author.Author.read_all()
    redirect_id = str(pk)
    return render_template('book_single.html', book_data=book_data, all_authors= all_authors, redirect_id = redirect_id)

@app.route('/add_author', methods=['POST'])
def add_author():
    book.Book.create_favorite_book(request.form)
    redirect_url = '/books/' + str(request.form['form_book_id'])
    return redirect(redirect_url)