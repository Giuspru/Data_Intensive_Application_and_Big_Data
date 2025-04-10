from pymongo import MongoClient 
from bson.objectid import ObjectId
from datetime import datetime

# 0. Creation of a connection  to MongooDB
client = MongoClient("mongodb://localhost:27017/")
db = client["book_review_app"]
books = db["books"]
reviews = db["reviews"]

# 1. Insert a new review

def newReview(book_id, rating, comment):
    review = {
        "book_id": book_id,
        "rating": rating,
        "comment": comment,
        "timestamp": datetime.now()
    }
    result = reviews.insert_one(review)
    print(f"Inserted review with ID: {result.inserted_id}")


# 2. List all reviews for a book

def reviewsByBook(book_id):
    print(f"Reviews for book with ID {book_id}:")
    for review in reviews.find({"book_id": ObjectId(book_id)}):
        print(f"ID: {review['_id']}, Rating: {review['rating']}, Comment: {review['comment']}, Timestamp: {review['timestamp']}")


