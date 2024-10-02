## 用途
密碼隨機，適合辦在正式比賽。

## 帳號
teamXXX 三位數，起始值要可在 ```iterater_team_id``` 自己設定，小心不要撞已經有的。

## 密碼
隨機產生，不會出現 ```0oOlI1```，這幾種會混淆的。

## 使用方法
1. 首先建立一個 teams.txt 文件
    - 如果在 Scoreboard 上顯示的名稱要自創的話，在裡面寫入隊名，以換行隔開，如果不用自創隊名就留空。
    - 如果有多個 txt 檔要創，例如要把 ```organization_id``` 分開的話，可以到兩個 .py 檔修改 ```TEAMS_TXT_FILE```，注意由於 domjudge import 的 json 檔名稱是固定的，所以請做完一組就 import 一次。

2. 變數設定
    1. ```CATAGORIES_EXTERNAL_ID```:
        隊伍所屬的 Group，要去 ```Team Categories``` 複製 ```external_id```。
    2. ```TEAMS_TXT_FILE```:
        讀入的隊伍名，檔案可留空，但一定要創。
    3. ```ACCOUNTS_DOCX```:
        密碼紙的 word 檔名。
    4. ```ORGANIZATION_EXTERNAL_ID```:
        隊伍的機構名稱，要去 ```Team Affiliations``` 複製 ```external_id```，如果不需要設定就把會用到的地方註解掉。
    5. ```LOCATION```:
        隊伍的國家，如果不需要設定就把會用到的地方註解掉。
    6. ```else_team_count```:
        比較複雜，到使用方法的第三點展開。
    7. ```iterater_team_id```:
        就是帳號，此值會設定第一個帳號名稱，例如為 1 是 team001, team002...，100 是 team100, team101...，
        程式會先掃過 ```teams.txt```、再來是 ```else_team_count```。

3. 帳密、Scoreboard 顯示隊名:
    以下是一些情況。
    1. Scoreboard 名稱自創:
        - Scoreboard 顯示的隊名跟隨 txt 給的隊名。
        - 設定 ```else_team_count``` 代表備用帳號數量，這些帳號在 Scoreboard 顯示的隊名會跟隨 ```iterater_team_id```，也就是他們的帳號。
    2. Scoreboard 匿名:
        - 跟第一點一樣，只是 Scoreboard 顯示的隊名統一跟隨帳號 TeamXXX，但是密碼紙一樣可以認人。
        - 去 ```createTeam.py``` 的 ```create_team_data``` 把 "display_name" 改成跟 "id" 一樣。
    3. 直接建立一定數字的帳號:
        - 把 ```teams.txt``` 留空，設定這個數字代表要建立多少帳號。

4. 運行兩個 .py 檔
5. 到 domjudge import

    Import -> Import JSON / YAML

    1. Type 選 team，File 選 teams.json
    2. Type 選 account，File 選 accounts.json

    以上要照順序。