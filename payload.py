from utilities.configurations import *


def addBookPayload(isbn, aisle):
    body = {

        "name": "Learn Appium Automation with Java" ,
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }
    return body


def deleteBookPayload(bookID):
    body = {

        "ID": bookID

    }
    return body


def buildPayLoadFromDB(query):
    tp = getQuery(query)
    addBody = {}
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
