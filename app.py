from flask import Flask, render_template, url_for

app = Flask(__name__)

books = [
    {
        'name':"Harry Potter and the Philosopher's Stone",
        'author':'JK Rowling',
        'publisher':'Bloomsbury',
        'publishDate':'1997',
        'cover':"/static/pics/philosophers_Stone.png"
    },
    {
        'name':'Harry Potter and the Chamber of Secrets',
        'author':'JK Rowling',
        'publisher':'Bloomsbury',
        'publishDate':'1998',
        'cover':"/static/pics/chamber_of_secrets.png"
    }
]

@app.route('/')
def home():
    return render_template('index.html', books = books, title = "Home")

if __name__ == "__main__":
    app.run(debug=True)