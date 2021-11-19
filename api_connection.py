from urllib.request import urlopen
import json
import random

api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

def get_book_info(isbn = "1593276036"):
    resp = urlopen(api+isbn)
    book_data = json.load(resp)
    info = book_data["items"][0]["volumeInfo"]
    title = info['title']
    authorsArr = info['authors']
    authors = ", ".join(authorsArr)
    publisher = info["publisher"]
    publishDate = info["publishedDate"]
    imageLink = book_data["items"][0]['volumeInfo']['imageLinks']['thumbnail']
    if 'categories' in info.keys():
        categoriesArr = info["categories"]
        categories = ", ".join(categoriesArr)
    else:
        categories = "None"
    desc = info["description"]
    pageCount = info["pageCount"]
    return({"name":title,"authors":authors,"publishDate": publishDate,"publisher":publisher, "imageLink":imageLink, "categories":categories, "description":desc, "pageCount":pageCount})


get_book_info("1781100233")