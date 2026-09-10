#G1
study_sessions = [
    {"subject": "Java", "minutes": 0},
    {"subject": "Visual Basic", "minutes": 1},
    {"subject": "C", "minutes": 2},
    {"subject": "C++", "minutes": 3},
    {"subject": "C#", "minutes": 4},
    {"subject": "C", "minutes": 5},
    {"subject": "C++", "minutes": 6},
    {"subject": "Python", "minutes": 7},
    {"subject": "AI", "minutes": 8},
    {"subject": "Python", "minutes": 49}
]

#G2
total_minutes = 0
for session in study_sessions:
    total_minutes += session["minutes"]
print(total_minutes)

#G3
minutes_per_subject = {}
for session in study_sessions:
    subject = session["subject"]
    if (subject in minutes_per_subject.keys()):
        minutes_per_subject[subject] += session["minutes"]
    else:
        minutes_per_subject[subject] = session["minutes"]
for subject, minutes in minutes_per_subject.items():
    print(subject, minutes)

#G4
longest = None
for session in study_sessions:
    if (longest == None or session["minutes"] > longest["minutes"]):        
        longest = session
if (longest):
    print (longest["minutes"])

#G5
for session in study_sessions:
    if (session["minutes"] > 45):
        print(session)

#G6 and G7
menu = ["view all sessions", "view total time", "filter by subject", "quit"]
while True:
    selected = None
    print (*enumerate(menu))
    inp = input("choose option: ")
    if inp in menu:
        selected = menu.index(inp)
    else:
        try:
            num = int(inp)
            selected = num
        except:
            continue #swallow exception and do nothing
    if selected != None and selected >= 0 and selected < len(menu):
        if menu[selected] == "quit":
            break
        else:
            if menu[selected] == "view all sessions":
                print(study_sessions)
            elif menu[selected] == "view total time":
                print(total_minutes)
            elif menu[selected] == "filter by subject":
                selected_subject = None
                subjects = list(minutes_per_subject.keys())
                if(not len(subjects)):
                   continue
                print (*enumerate(subjects))
                sub_inp = input("select subject: ")
                if sub_inp in subjects:
                    selected_subject = subjects.index(sub_inp)
                else:
                    try:
                        subject_num = int(sub_inp)
                        selected_subject = subject_num
                    except:
                        continue #swallow exception and do nothing
                if (selected_subject != None and selected_subject >= 0 and
                    selected_subject < len(subjects)):
                    subject_name = subjects[selected_subject]
                    for session in study_sessions:
                        if (session["subject"] == subject_name):
                            print (session)
