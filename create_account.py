CATAGORIES_EXTERNAL_ID = [""]
TEAMS_TXT_FILE = "teams.txt"
USERS_TXT_FILE = "users.txt"
PASSWORDS_TXT_FILE = "passwords.txt"
PASSWORDS_DOCX = "passwords.docx" # 密碼紙
iterater_team_id = 1 # 第一支隊伍 ID
else_team_count = 0 # 用 team_id 當計分板名稱的數量

import json
from generator import password_generator
from create_word_document import create_word_document

def read_file(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return [line.strip() for line in file]
    except:
        return []

def create_account_data(user_name, password) -> dict:
    global iterater_team_id
    account = {
        "id": "team{:03}".format(iterater_team_id), # external_id
        "username": "team{:03}".format(iterater_team_id), # 帳號
        "password": password, # 密碼
        "type": "team", # 固定
        "name": str(user_name), # 後臺名字
        "team_id": "team{:03}".format(iterater_team_id) # 所屬的 team_external_id
    }
    iterater_team_id += 1
    return account

def main():
    team_names = read_file(TEAMS_TXT_FILE)
    user_names = read_file(USERS_TXT_FILE)
    passwords = read_file(PASSWORDS_TXT_FILE)

    if len(user_names) == 0:
        user_names = [''] * len(team_names)
    else:
        assert len(user_names) == len(team_names), "users.txt 的行數必須與 teams.txt 相同"
    if len(passwords) == 0:
        passwords = [password_generator() for _ in team_names]
    else:
        assert len(passwords) == len(team_names), "passwords.txt 的行數必須與 teams.txt 相同"

    accounts = []

    for user_name, password in zip(user_names, passwords):
        accounts.append(create_account_data(user_name, password))

    for _ in range(else_team_count):
        team_names.append("team{:03}".format(iterater_team_id))
        accounts.append(create_account_data("team{:03}".format(iterater_team_id)))

    with open("accounts.json", 'w', encoding='utf-8') as accountsFile:
        json.dump(accounts, accountsFile, indent=2, ensure_ascii=False)

    create_word_document(team_names, accounts)
    print("accounts.json and accounts.docx created successfully")
    
if __name__ == '__main__':
    main()