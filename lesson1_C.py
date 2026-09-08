#C1
full_sentence = " This is a full sentence "
print(len(full_sentence))
print (full_sentence.upper())
print (full_sentence.lower())
print (full_sentence.strip())

#C2
first_name = input("First name: ")
last_name = input("Last name: ")
full_name = f"{first_name} {last_name}"
print(full_name)

#C3
s = "python programming"
print(s[:1])
print(s[-1:])
print(s[:6])
print(s[-11:])
print(s[::-1])

#C4
user_name = (first_name[:3]+last_name[:5]).lower()
print (user_name)

#C5
email = "spam@me.com"
first, second = email.split("@")
print(first)
print(second)

#C6
s = "Java is an island"
t = s.replace("Java", "Python")
print (s)
print (t)

