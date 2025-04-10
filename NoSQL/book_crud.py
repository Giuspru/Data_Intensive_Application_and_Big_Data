from pymongo import MongoClient
from bson.objectid import ObjectId

# 0. Creation of a connection  to MongooDB

client = MongoClient("mongodb://localhost:27017/")
db = client["book_review_app"]
books = db["books"]
reviews = db["reviews"]


#1. Insert a new book

def insertBook(title, author, year, genre):

    # cration a dictionary
    book = {
        "title" : title, 
        "author" : author,
        "year" : year,
        "genre" : genre
    }

    # insert the book into the database
    result = books.insert_one(book)
    print(f"Inserted book with ID: {result.inserted_id}")


# 2. Show all the books:

def listBooks():

    print("List of all books:")
    for book in books.find():
        print("\nID:" ,book["_id"], "\nTitle:", book["title"] , "\nAuthor:", book["author"], "\nYear:", book["year"], "\nGenre:", book["genre"])


# 3. Findign a book by its title:

def findBookByTitle(title):
    book = books.find_one({"title": title})
    if book:
        print("Book found:")
        print("ID:", book["_id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Genre:", book["genre"])
        return book
    else:
        print("Book not found.")
        return None
    


# 4. Update a book:

def updateBook(book_id, update_fields):
    result = books.update_one({"_id": ObjectId(book_id)},
                              {"$set": update_fields})
    if result.modified_count > 0:
        print("Book updated successfully.")
    else:
        print("Book not found or no updates made.")

# 5. Delete a book:

def deleteBook(book_id):
    result = books.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count > 0:
        print("Book deleted successfully.")
    else:
        print("Book not found.")




if __name__ == "__main__":

    insertBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
    insertBook("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
    insertBook("1984", "George Orwell", 1949, "Dystopian")
    insertBook("Pride and Prejudice", "Jane Austen", 1813, "Romance")
    insertBook("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction")

    listBooks()

    book = findBookByTitle("The Great Gatsby")
    if book:
        updateBook(book["_id"], {"title": "The Great Gatsby (Updated)"})
        listBooks()

    # #deleting all books:
    # books.delete_many({})
