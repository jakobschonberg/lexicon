from datetime import datetime, timedelta
from msvcrt import getch
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["library"]
'''
members:
    {"_id",
    "name",
    "email"}
books:       -- for each book title
    {"_id",
    "title",
    "author",
    "genre",
    "copies",
    "reviews" (list member_id, rating and review_text)}
physical_books:   --each book can have multiple copies that can be lent out/returned seperately
    {"_id",      --unique id for different physical books
    "book_id",   --referencing books
    "loan" (list containing member_id who lent it?, loaned date and returned date) -- in case a book is damamged it might be valuable to know not just who lent the book last
    }
'''

def my_quit():
    pass

def wait():
    print("--continue--")
    getch()

menu = {
    1:("Quit", "my_quit"),
    2:("Reset collections with test data and Schema Validation", "setup_test_data"),
    3:("Search for book", "book_search"),
    4:("Loan book","loan_book"),
    5:("Return book","return_book"),
    6:("Show members", "show_members"),
    7:("Show overdue books", "show_overdue_books")
}

def schema_validation():
    members_vexpr =  {
        "$jsonSchema": {
            "bsonType": 'object',
            "required": [
                '_id',
                'email',
                'name'
            ],
            "properties": {
                "_id": {
                    "bsonType": 'int'
                },
                "email": {
                    "bsonType": 'string',
                    "pattern": '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
                },
                "name": {
                    "bsonType": 'string'
                }
            }
        }
    }

    books_vexpr = { "$jsonSchema": {
            "bsonType": 'object',
            "required": [
            '_id',
            'author',
            'copies',
            'genre',
            'reviews',
            'title'
            ],
            "properties": {
                "_id": {
                    "bsonType": 'int'
                },
                "author": {
                    "bsonType": 'string'
                },
                "copies": {
                    "bsonType": 'int'
                },
                "genre": {
                    "bsonType": 'string'
                },
                "reviews": {
                    "bsonType": 'array',
                    "items": {
                    "bsonType": 'object',
                    "properties": {
                        "member_id": {
                        "bsonType": 'int'
                        },
                        "rating": {
                        "bsonType": 'int'
                        },
                        "review_text": {
                        "bsonType": 'string'
                        }
                    },
                    "required": [
                        'member_id',
                        'rating',
                        'review_text'
                    ]
                    }
                },
                "title": {
                    "bsonType": 'string'
                }
            }
        }
    }

    physical_books_vexpr = {"$jsonSchema": {
            "bsonType": 'object',
            "required": [
                '_id',
                'book_id',
                'loan'
            ],
            "properties": {
                "_id": {
                    "bsonType": 'int'
                },
                "book_id": {
                    "bsonType": 'int'
                },
                "loan": {
                    "bsonType": 'array',
                    "items": {
                        "bsonType": 'object',
                        "properties": {
                            "loan_date": {
                                "bsonType": 'date'
                            },
                            "member_id": {
                                "bsonType": 'int'
                            },
                            "return_date": {
                                "bsonType": [
                                    'date',
                                    'null'
                                ]
                            }
                        },
                        "required": [
                            'loan_date',
                            'member_id',
                            'return_date'
                        ]
                    }
                }
            }
        }
    }
    try:
        db.create_collection("members", validator=members_vexpr)
        db.create_collection("books", validator=books_vexpr)
        db.create_collection("physical_books", validator=physical_books_vexpr)
    except Exception as e:
        print(e)


def setup_test_data():
    for name in ["members", "books", "physical_books"]:
        db[name].drop()
    schema_validation()
    members = [{"_id": 1, "name": "Ada", "email": "ada@spam.com"},
               {"_id": 2, "name": "Bob", "email": "bob@spam.com"},
               {"_id": 3, "name": "Cecil", "email": "cecil@spam.com"},
               {"_id": 4, "name": "Dee", "email": "dee@spam.com"}
    ]
    db.members.insert_many(members)
    books = [
        {"_id": 1,
            "title": "Lord of the Rings",
            "author": "J.R.R Tolkien",
            "genre": "Fantasy",
            "copies": 3,
            "reviews": [{"member_id": 1, "rating": 5, "review_text": "Loved it!"}]
        },
        {"_id": 2,
            "title": "Daggerspell",
            "author": "Katherine Kerr",
            "genre": "Fantasy",
            "copies": 1,
            "reviews": [{"member_id": 2, "rating": 3, "review_text": "Intriguing"}]
        },
        {"_id": 3,
            "title": "2001: A Space Odyssey",
            "author": "Arthur C. Clarke",
            "genre": "Science Fiction",
            "copies": 1,
            "reviews": [{"member_id": 1, "rating": 2, "review_text": "Felt a bit dated"}]
        }
    ]
    db.books.insert_many(books)
    physical_books = [
        {"_id": 1,
         "book_id": 1,
         "loan": [{"member_id": 1, "loan_date": datetime(2026, 6, 1), "return_date": datetime(2026, 6, 15)}]},
        {"_id": 2,
         "book_id": 1,
         "loan": []},
        {"_id": 3,
         "book_id": 1,
         "loan": [{"member_id": 2, "loan_date": datetime(2026, 10, 12), "return_date": None}]},
        {"_id": 4,
         "book_id": 2,
         "loan": [{"member_id": 2, "loan_date": datetime(2026, 6, 5), "return_date": datetime(2026, 6, 18)}]},
        {"_id": 5,
         "book_id": 3,
         "loan": [{"member_id": 3, "loan_date": datetime(2026, 6, 17), "return_date": datetime(2026, 6, 24)},
                  {"member_id": 4, "loan_date": datetime(2026, 10, 13), "return_date": None}]}
    ]
    db.physical_books.insert_many(physical_books)

def book_search():
    search = input("Enter part or whole of Title or Author or Genre: ")
    for book in db.books.find({"$or": [{"title":{"$regex": search}},{"author":{"$regex": search}},{"genre":{"$regex": search}}]}):
        print("title:",book["title"],"author:", book["author"], "genre:", book["genre"])
    wait()
    

def loan_book():
    try:
        member_id = int(input("Enter member id: "))
        if not db.members.count_documents({"_id": member_id}):
            print("Invalid member id")
            wait()
            return
        member = db.members.find_one({"_id": member_id})
        search = input("Enter part or whole of Title or Author or Genre: ")
        books = db.books.find({"$or": [{"title":{"$regex": search}},{"author":{"$regex": search}},{"genre":{"$regex": search}}]})
        if (len(list(books)) == 1):
            book = db.books.find_one({"$or": [{"title":{"$regex": search}},{"author":{"$regex": search}},{"genre":{"$regex": search}}]})
            physical_book = db.physical_books.find_one({"book_id": book["_id"], "loan.return_date": {"$ne":  None}})
            if physical_book:
                confirm = input(f'Lend {book["title"]} to {member["name"]} (y/n)? ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    db.physical_books.update_one({"_id": physical_book["_id"]},
                                                {"$push": {"loan": {"member_id": member["_id"],
                                                                    "loan_date": datetime.now(),
                                                                    "return_date": None}}})
                    print(f'{member["name"]} lent {book["title"]}')                
                    return_date = datetime.now() + timedelta(days=14)
                    print(f'Please return at latest: {return_date.strftime("%Y-%m-%d")}')
                    wait()
            else:
                print("No copies available right now")
                wait()
        elif (len(list(books)) > 1):
            print("Ambigous, more than one book found")
            wait()
    except Exception as e:
        print("Error:", e)
        wait()

def return_book():
    raise NotImplementedError()

def show_members():
    raise NotImplementedError()

def show_overdue_books():
    raise NotImplementedError()

def main():
    choice = None
    while (choice != 1):
        for key, value in sorted(menu.items()):
            print(f'{key} {value[0]}')
        try:
            choice = int(input())
            if not choice in menu.keys():
                print("invalid menu number")
                choice = None
        except Exception as e:
            print(e)
            choice = None
        if choice:
            chosen = menu[choice][1]
            globals()[chosen]()

main()
