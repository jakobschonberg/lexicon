#F1
'''
Create functions to normalize a participant name,
validate an age range using boolean return values,
calculate a registration fee based on age/student status,
and create a participant dictionary. 
'''

def process_participant(p):
    '''Returns false if invalid input'''
    r = {}
    name = p["Name"]
    if not name:
        return False, None, None
    r["Name"] = (name[0:1]).upper() + (name[1:]).lower()
    age = p["Age"]
    if age < 0:
        return False, None, None
    else:
        r["Age"] = age
        if age < 18 or p["Student_status"] == False:
            r["Registration_fee"] = 0
        else:
            r["Registration_fee"] = 100
    r["Student_status"] = p["Student_status"]
    return True, p["Id"], r

def process_participant_list(l):
    d = {}
    for participant_data in participants:        
        valid, id, participant = process_participant(participant_data)
        if valid:
            d[id] = participant
    return d


#F2
'''
Create at least eight participant dictionaries using your functions.
'''
participants = [{"Id": "0201010101", "Name": "Ada", "Age": 25, "Student_status": True},
                {"Id": "2805060708", "Name": "bOb", "Age": -4, "Student_status": False},
                {"Id": "0502030406", "Name": "ceCil", "Age": 21, "Student_status": True},
                {"Id": "2006050403", "Name": "Dave", "Age": 6, "Student_status": False},
                {"Id": "9801010101", "Name": "Eskil", "Age": 28, "Student_status": True},
                {"Id": "9901010101", "Name": "Franz", "Age": 27, "Student_status": True},
                {"Id": "2401010101", "Name": "Gunnar", "Age": 2, "Student_status": False},
                {"Id": "0001010101", "Name": "Hilda", "Age": 26, "Student_status": False},
                {"Id": "9701010101", "Name": "Ida", "Age": 29, "Student_status": True}]
d = process_participant_list(participants)
#print(d)

#F3
'''
Write a function that receives the participant list
and returns the total expected registration revenue.
'''
def revenue(participants):
    r = 0
    for student in process_participant_list(participants).values():        
        r += int(student["Registration_fee"])
    return r

print(revenue(participants))

#F4
'''
Write a function that returns only student participants.
'''
def get_students(participants):
    r = []
    for participant in participants:
        if participant["Student_status"]:
            r.append(participant)
    return r

print(get_students(participants))

#F5
'''
Write a function that returns the oldest participant. 
'''
def get_oldest(participants):
    oldest = None
    for participant in participants:
        if oldest == None or participant["Age"] > oldest["Age"]:
            oldest = participant
    return oldest

print(get_oldest(participants))

#F6
'''
Write a function that creates a readable summary string for one participant.
'''
'''
def print_summary(participant):
    print(participant["Name"])
    print(participant["Age"])
    if(participant["Student_status"]):
        print("Student")

print_summary(get_oldest(participants))
'''

#F7
'''
Keep input/output responsibilities separate
from calculation functions as much as possible.
'''

def summary(participant):
    s = "Name: " + participant["Name"] + "\nAge: " + str(participant["Age"])
    if(participant["Student_status"]):
        s = s + "\nStudent"
    return s

print(summary(get_oldest(participants)))