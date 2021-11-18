from flask import Flask, render_template, url_for
from api_connection import *

app = Flask(__name__)

books = [get_book_info("1781100489"),get_book_info("1781100489"),get_book_info("1781100489"),get_book_info("1781100489"),get_book_info("1781100489")]


@app.route('/')
def home():
    return render_template('index.html', books = books, title = "Home")

if __name__ == "__main__":
    app.run(debug=True)