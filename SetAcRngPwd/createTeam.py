CATAGORIES_EXTERNAL_ID = [""]
TEAMS_TXT_FILE = "teams.txt"
ORGANIZATION_EXTERNAL_ID = ""
LOCATION = "TWD"
iterater_team_id = 0 # 第一支隊伍 ID
else_team_count = 0 # 用 team_id 當計分板名稱的數量

import json

def read_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return [line.strip() for line in file]

def create_team_data(team_name):
    global iterater_team_id
    team = {
        "id": "team{:03}".format(iterater_team_id), # extercal_id
        # "icpc_id": account,
        "group_ids": CATAGORIES_EXTERNAL_ID, # catagory belong to
        "name": team_name,
        "display_name": team_name, # scoreboard name
        "organization_id": ORGANIZATION_EXTERNAL_ID, # 組織
        "location.description": LOCATION, # country
    }
    iterater_team_id += 1
    return team

def main():
    team_names = read_file(TEAMS_TXT_FILE)
    teams = []
    
    for team_name in team_names:
        teams.append(create_team_data(team_name))

    for i in range(else_team_count):
        teams.append(create_team_data("team{:03}".format(iterater_team_id)))

    with open("teams.json", 'w', encoding='utf-8') as teamsFile:
        json.dump(teams, teamsFile, indent=2, ensure_ascii=False)

    print("teams.json created successfully")

if __name__ == '__main__':
    main()