from flask import Flask, render_template, url_for
from api_connection import *

app = Flask(__name__)

books = [get_book_info("1781100489"),get_book_info("1781100500"),get_book_info("1781100233"),get_book_info("1781105677"),get_book_info("1781100241"),get_book_info("178110025X"),get_book_info("0553573403"), get_book_info("0008144222"), get_book_info("1846558239"), get_book_info("145162171X")]

books[0]["url"] = "sorcerersstone"
books[1]["url"] = "chamberofsecrets"
books[2]["url"] = "azkaban"
books[3]["url"] = "goblet "
books[4]["url"] = "phoenix"
books[5]["url"] = "prince"
books[6]["url"] = "agameofthrones"
books[7]["url"] = "thealchemist"
books[8]["url"] = "sapiens"
books[9]["url"] = "winfriends"

@app.route('/')
def home():
    return render_template('index.html', books = books, title = "Home")

@app.route('/sorcerersstone')
def book0():
    return render_template('book.html', book=books[0])

@app.route('/chamberofsecrets')
def book1():
    return render_template('book.html', book=books[1])

@app.route('/azkaban')
def book2():
    return render_template('book.html', book=books[2])

@app.route('/goblet')
def book3():
    return render_template('book.html', book=books[3])

@app.route('/phoenix')
def book4():
    return render_template('book.html', book=books[4])

@app.route('/prince')
def book5():
    return render_template('book.html', book=books[5])

@app.route('/agameofthrones')
def book6():
    return render_template('book.html', book=books[6])

@app.route('/thealchemist')
def book7():
    return render_template('book.html', book=books[7])

@app.route('/sapiens')
def book8():
    return render_template('book.html', book=books[8])

@app.route('/winfriends')
def book9():
    return render_template('book.html', book=books[8])

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)