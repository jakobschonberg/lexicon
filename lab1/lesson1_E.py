#E1
first_name = input("First name: ")
last_name = input("Last name: ")
city = input("City: ")
year_of_birth = int(input("Year of birth: "))
programming_language = input("Favourite programming language: ")

#E2
first_name = first_name.strip()
last_name = last_name.strip()
city = city.strip()
programming_language = programming_language.strip()

#E3
userID = first_name[:3] + last_name[:3] + str(year_of_birth%100)

#E4
print(f"{first_name} {last_name}\n{city}\n{year_of_birth}\n{programming_language}\n{userID}")

#5
print(first_name[0:1] + last_name[0:1])
print(str(len(first_name)+len(last_name)))
print(programming_language[::-1])

#6
likes_python = programming_language.lower() == "python"
likes_c = (programming_language.lower() == "c" or
           programming_language.lower() == "c++" or
           programming_language.lower() == "c#")
likes_java = programming_language.lower() == "java"
