from urllib.request import urlopen
import json
import random

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

def get_book_info(isbn = "1593276036"):
    resp = urlopen(api+isbn)
    book_data = json.load(resp)
    info = book_data["items"][0]["volumeInfo"]
    title = info['title']
    authors = info['authors']
    publishDate = info["publishedDate"]
    publisher = info["publisher"]
    imageLink = book_data["items"][0]['volumeInfo']['imageLinks']['thumbnail']
    return({"name":title,"authors":authors,"publishDate":publishDate,"publisher":publisher, "imageLink":imageLink})
