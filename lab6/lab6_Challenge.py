original_data = [
    {"name": "aDa", "team": "V3", "country": "japan", "score": 40, "matches": 10, "wins": 7, "active": True},
    {"name": " scwapie", "team": "", "country": "Brazil", "score": 67, "matches": 7, "wins": 7, "active": True},
    {"name": "Cecil ", "team": "TL", "country": "usa", "score": 0, "matches": 0, "wins": 0, "active": True},
    {"name": "Dave", "team": "foo", "country": "USA", "score": 7, "matches": 3, "wins": 2, "active": False},
    {"name": "Eve", "team": "sb", "country": "South Korea", "score": 0, "matches": 0, "wins": 0, "active": True},
    {"name": "Fakew", "team": "T1", "country": "South Korea", "score": 99, "matches": 12, "wins": 12, "active": True},
    {"name": "Gwanady", "team": "BIG", "country": "Germany", "score": 8, "matches": 5, "wins": 1, "active": True},
    {"name": "Huby", "team": "TL", "country": "Hungary", "score": 9, "matches": 5, "wins": 2, "active": False},
    {"name": "iPriMe", "team": "va bene!", "country": "Italy", "score": 10, "matches": 5, "wins": 2, "active": True},
    {"name": "Jo", "team": "V3", "country": "Japan", "score": 12, "matches": 5, "wins": 2, "active": True},
    {"name": "Kek", "team": "", "country": "Kenya", "score": 13, "matches": 5, "wins": 2, "active": True},
    {"name": "Lydia", "team": "TL", "country": "Latvia", "score": 14, "matches": 5, "wins": 2, "active": True},
    {"name": "Mox", "team": "TL", "country": "Mexico", "score": 15, "matches": 5, "wins": 2, "active": True},
    {"name": "wiwtual", "team": "tl", "country": "Norway", "score": 34, "matches": 4, "wins": 3, "active": True},
    {"name": "Omar", "team": "Tl", "country": "Oman", "score": 17, "matches": 5, "wins": 3, "active": True}
]

players = original_data.copy()

for player in players:
    player["name"] = player["name"].strip().title()
    player["team"] = player["team"].strip().title()
    player["country"] = player["country"].strip().title()

active_players = [player for player in players if player["active"]]
players_3_wins = [player for player in players if player["wins"] >= 3]
players_10_score = [player for player in players if player["score"] >= 10]
players_from_japan = [player for player in players if player["country"] == "Japan"]
unbeaten_players = [player for player in players if player["matches"] and player["wins"] == player["matches"]]

countries = {player["country"] for player in players}
teams = {player["team"] for player in players}
player_scores = {player["name"]: player["score"] for player in players}
player_wins = {player["name"]: player["wins"] for player in players}
player_scores_10 = {player["name"]: player["score"] for player in players if player["score"] >= 10}

player_names = ["Anna", "David", "Sara", "Leo", "Void"]
ranking_points = [1200, 950, 1430, 1100]
active = [True, True, True, False]
player_ranking_points = list(zip(player_names, ranking_points))
player_active = list(zip(player_names, active))
player_ranking_points_active = list(zip(player_names, ranking_points, active))

for player, points, active in player_ranking_points_active:
    print (player, points, active)
#shortest zip list is of length 4, so result is of length 4 ("Void" got voided)

players_sorted_by_score = sorted(player_scores.items(), key = lambda x: x[1], reverse = True)
players_sorted_by_score_asc = sorted(player_scores.items(), key = lambda x: x[1])
players_sorted_by_wins = sorted(player_wins.items(), key = lambda x: x[1], reverse = True)
player_matches = {player["name"]: player["matches"] for player in players}
players_sorted_by_matches = sorted(player_matches.items(), key = lambda x: x[1], reverse = True)
player_names_sorted = sorted([player["name"] for player in players])

for num, player in enumerate(players_sorted_by_score, start = 1):
    print(f"{num}. {player[0]} - {player[1]} points")

tl_players = [player["name"] for player in players if player["team"] == "Tl"]
players_3_wins = [player["name"] for player in players if player["wins"] >= 3]
teams = {player["team"] for player in players if player["team"]}
countries = {player["country"] for player in players}
players_active_and_score_10 = [player["name"] for player in players if player["active"] and player["score"] >= 10]

def performance(score, wins, matches):
    if not matches:
        return 0
    return (score + 3 * wins) / matches

player_performance = dict({player["name"]: performance(player["score"], player["wins"], player["matches"]) for player in players})
player_performance = sorted(player_performance.items(), key = lambda x: x[1], reverse = True)
print("Player performance:")
for rank, player in enumerate(player_performance, start = 1):
    print(f"{rank}. {player[0]} - {player[1]:.1f}")
player_performance_5 = {player[0]: player[1] for player in player_performance if player[1] >= 5}

final_report = {}
final_report["total_players"] = len(players)
final_report["active_players"] = len(active_players)
final_report["unique_teams"] = teams
final_report["unique_countries"] = countries
final_report["players_by_score"] = players_sorted_by_score
final_report["players_by_wins"] = players_sorted_by_wins
final_report["players_top_5"] = players_sorted_by_score[:5]
final_report["players_performance_5"] = player_performance_5
final_report["players_undefeated"] = [player["name"] for player in unbeaten_players]
final_report["inactive_players"] = [player["name"] for player in players if not player["active"]]
final_report["players_no_wins"] = [player["name"] for player in players if not player["wins"]]


def print_final_report():
    print("\nFinal Report:")
    print("Total players:", final_report["total_players"])
    print("Active players:", final_report["active_players"])
    u_teams = ""
    for team in final_report["unique_teams"]:
        if u_teams:
            u_teams += ", " + team
        else:
            u_teams = team
    print("Unique teams:", u_teams)
    u_countries = ""
    for country in final_report["unique_countries"]:
        if u_countries:
            u_countries += ", " + country
        else:
            u_countries = country
    print("Unique countries:", u_countries)
    print("Players ranked by score:")
    for player in final_report["players_by_score"]:
        print(*player)
    print("Players ranked by wins:")
    for player in final_report["players_by_wins"]:
        print(*player)
    print("Top 5 players:")
    for player in final_report["players_top_5"]:
        print(*player)
    print("Players at 5 or above performance:")
    for player in final_report["players_performance_5"].items():
        print(f"{player[0]} {player[1]:.1f}")
    print("Undefeated players:", *final_report["players_undefeated"])
    print("Inactive players:", *final_report["inactive_players"])
    print("Players with no wins:", *final_report["players_no_wins"])

print_final_report()


#original code:
'''
def performance(score, wins, matches):
    if not matches:
        return 0
    return (score + 3 * wins) / matches

player_performance = dict({player["name"]: performance(player["score"], player["wins"], player["matches"]) for player in players})
'''
#pure comprehension version:
player_performance = dict({player["name"]: 0 for player in players if not player["matches"]}|
                      {player["name"]: (player["score"] + 3 * player["wins"]) / player["matches"]
                       for player in players if player["matches"]})

#Both are fine by me, but maybe the original code is a little easier to read