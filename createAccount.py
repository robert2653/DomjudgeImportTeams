CATAGORIES_EXTERNAL_ID = ["students"]
TEAMS_TXT_FILE = "teams.txt" # ACCOUNT
USERS_TXT_FILE = "users.txt"
PASSWORDS_TXT_FILE = "passwords.txt"

import json

def read_file(filename):
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return [line.strip() for line in file]
    except:
        return []
    

def create_account_data(team_name, password, user_name = None):
    if user_name is None:
        user_name = team_name

    account = {
        "id": str(team_name), # external_id
        "username": str(team_name), # 帳號
        "password": str(password), # 密碼
        "type": "team",
        "name": str(user_name), # 後台可看名稱
        "team_id": str(team_name)
    }
    return account

def main():
    team_names = read_file(TEAMS_TXT_FILE)
    print(len(team_names))
    passwords = read_file(PASSWORDS_TXT_FILE)
    print(len(passwords))
    user_names = read_file(USERS_TXT_FILE)
    print(len(user_names))
    if len(user_names) == 0:
        user_names = [''] * len(team_names)

    accounts = []

    for team_name, password, user_name in zip(team_names, passwords, user_names):
        accounts.append(create_account_data(team_name, password, user_name))

    with open("accounts.json", 'w', encoding='utf-8') as teamsFile:
        json.dump(accounts, teamsFile, indent=2, ensure_ascii=False)

    print("accounts.json created successfully")

if __name__ == "__main__":
    main()