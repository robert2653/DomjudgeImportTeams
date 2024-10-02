CATAGORIES_EXTERNAL_ID = [""]
TEAMS_TXT_FILE = "teams.txt" # ACCOUNT
ACCOUNTS_TXT_FILE = "accounts.txt" # PASSWORD
TEAM_COUNT = 3

import json

def read_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return [line.strip() for line in file]
    

def create_team_data(accounts, team_names):
    teams = []
    for account, name in zip(accounts, team_names):
        team = {
            "id": name, # extercal_id
            "username": name, # 帳號
            "password": account, # 密碼
            "type": "team",
            "name": name, # 後台可看名稱
            "team_id": name
        }
        teams.append(team)
    return teams

accounts = read_file(ACCOUNTS_TXT_FILE)
team_names = read_file(TEAMS_TXT_FILE)

teams = create_team_data(accounts, team_names)

with open("accounts.json", 'w', encoding='utf-8') as teamsFile:
    json.dump(teams, teamsFile, indent=2, ensure_ascii=False)

print("accounts.json created successfully")