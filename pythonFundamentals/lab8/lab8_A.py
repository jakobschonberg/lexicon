#A1
class BadTeam:
    def __init__(self, name, members = []):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)

#A2
bad_team_1 = BadTeam("Alpha")
bad_team_2 = BadTeam("Beta")
bad_team_1.add_member("Ada")
print(bad_team_1.members)
print(bad_team_2.members)
#default value members = [] is only called once when the class is created
#all BadTeam objects referes to the same list since members is never assigned to another list than the default one

#A3
class Team:
    def __init__(self, name, members = None):
        self.name = name
        self.members = members
        if self.members is None: #making sure self.members gets initialized to either a given argument list or a new empty list for each new object
            self.members = []
    
    def add_member(self, member):
        self.members.append(member)

#A4
team_1 = Team("Alpha")
team_2 = Team("Beta")
team_3 = Team("Gamma", ["Bob", "Cecil"]) #just to show it also works with members argument
team_1.add_member("Ada")
print(team_1.members)
print(team_2.members)
print(team_3.members)