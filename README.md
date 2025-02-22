## 用途
帳號密碼自行設定，可以都是學號，Scoreboard 顯示的是帳號，適合辦在練習賽、作業。

## 帳號
teams.txt 給的。

## 密碼
accounts.txt 給的。

## 使用方法
1. 建立 teams.txt 跟 accounts.txt 文件，分別輸入帳號密碼，記得要一行對應一行。

2. 變數設定
    1. ```CATAGORIES_EXTERNAL_ID```:
        隊伍所屬的 Group，要去 ```Team Categories``` 複製 ```external_id```。
    2. ```TEAMS_TXT_FILE```:
        帳烙。
    3. ```ACCOUNTS_TXT_FILE```:
        密碼。
    4. ```ORGANIZATION_EXTERNAL_ID```:
        隊伍的機構名稱，要去 ```Team Affiliations``` 複製 ```external_id```，如果不需要設定就把會用到的地方註解掉。
    5. ```LOCATION```:
        隊伍的國家，如果不需要設定就把會用到的地方註解掉。

3. 運行兩個 .py 檔。
4. 到 domjudge import
    Import -> Import JSON / YAML
    1. Type 選 team，File 選 teams.json
    2. Type 選 account，File 選 accounts.json
    以上要照順序。