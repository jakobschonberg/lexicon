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
    {"_id",      --unique id for different physical books of same title
    "book_id",   --referencing books
    "loan" (list containing member_id who lent it?, loaned date and returned date) -- in case a book is damamged it might be valuable to know not just who lent the book last
    }
'''

def my_quit():
    pass

menu = {1:("Quit", "my_quit"),
        2:("Schema Validation", "schema_validation"),
        3:("Create test data", "setup_test_data"),
        4:("Search for book", "book_search"),
        5:("Loan book","loan_book"),
        6:("Return book","return_book"),
        7:("Show members", "show_members"),
        8:("Show overdue books", "show_overdue_books")
        }

def schema_validation():
    members_vexpr =  {"$jsonSchema":
        {
            "bsonType": "object",
            "required": ["name", "email"],
            "properties": {
                "name": {
                   "bsonType": "string",
                   "description": "must be a string and is required"
                },
                "email": {
                   "bsonType": "string",
                   "description": "must be a string and is required"
                }
            }
        },
        "validationLevel": "strict",
        "validationAction": "error"
    }
    books_vexpr =  {"$jsonSchema":
        {
            "bsonType": "object",
            "required": ["title", "author", "genre", "copies"],
            "properties": {
                "title": {
                   "bsonType": "string",
                   "description": "must be a string and is required"
                },
                "author": {
                   "bsonType": "string",
                   "description": "must be a string and is required"
                },
                "genre": {
                   "enum": ["Science Fiction", "Fantasy", "Adventure", "Mystery", "Horror", "Thriller", "Romance", "Math", "Computer Science", "Physics", "History", "Other"],
                   "description": "can only be one of the enum values and is required"
                },
                "copies": {
                   "bsonType": "int",
                   "minimum": 0,
                   "description": "must be an int and is required"
                },
                "reviews": {
                   "bsonType": "string",
                   "description": "must be a list[dict{int: tuple(int, string)}] and is not required"
                }                
             }
        },
        "validationLevel": "strict",
        "validationAction": "error"
    }


'''
                "year": {
                   "bsonType": "int",
                   "minimum": 2017,
                   "maximum": 3017,
                   "exclusiveMaximum": False,
                   "description": "must be an integer in [ 2017, 3017 ] and is required"
                },
                "major": {
                   "enum": [ "Math", "English", "Computer Science", "History", None ],
                   "description": "can only be one of the enum values and is required"
                },
                "gpa": {
                   # In case you might want to allow doubles OR int, then add
                   # "int" to the bsonType array below:
                   "bsonType": [ "double" ],
                   "minimum": 0,
                   "description": "must be a double and is required"
                }

'''


def setup_test_data():
    raise NotImplementedError()

def book_search():
    raise NotImplementedError()

def loan_book():
    raise NotImplementedError()

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
