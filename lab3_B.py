import cmath
#B1
if(""):
    print('""')
if({}):
    print("{}")
if([]):
    print("[]")
if(()):
    print("()")
if():
    print("_")
if(0):
    print("0")
if(complex(0)):
    print("complex(0)")
if(" "):
    print('" "')
if(-1e-66):
    print(-1e-66)
if(["a", "b"]):
    print("['a'] ['b']")

#B2
languages = ["a", "b", "c"]
language_queries = ["c", "c++", "c#"]
for lang in language_queries:
    print (lang in languages)

#B3
blocked_usernames = ["John", "Peter"]
user_queries = ["Ada", "Berry", "Peter"]
for name in user_queries:
    if(name in blocked_usernames):
        print("rejected")
    else:
        print("accepted")

#B4
for name in user_queries:
    if not name in blocked_usernames:
        print (name)
if(not False):
    print (True)