CATAGORIES_EXTERNAL_ID = ["students"]
TEAMS_TXT_FILE = "teams.txt"
USERS_TXT_FILE = "users.txt"
# ORGANIZATION_EXTERNAL_ID = ""
LOCATION = "TWD"

import json

def read_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return [line.strip() for line in file]

def create_team_data(team_name, user_name = None):
    if user_name is None:
        user_name = team_name

    team = {
        "id": str(team_name), # extercal_id
        # "icpc_id": str(account),
        "group_ids": CATAGORIES_EXTERNAL_ID, # catagory belong to
        "name": str(team_name),
        "display_name": str(user_name), # scoreboard name
        # "organization_id": ORGANIZATION_EXTERNAL_ID, # 組織
        # "location.description": LOCATION, # country
    }
    return team

if __name__ == "__main__":
    team_names = read_file(TEAMS_TXT_FILE)
    users_names = read_file(USERS_TXT_FILE)
    if len(users_names) == 0:
        users_names = [''] * len(team_names)

    teams = []

    for team_name, user_name in zip(team_names, users_names):
        teams.append(create_team_data(team_name, user_name))

    with open("teams.json", 'w', encoding='utf-8') as teamsFile:
        json.dump(teams, teamsFile, indent=2, ensure_ascii=False)

    print("teams.json created successfully")