# DOMjudge Import Teams

本專案提供了一套自動化腳本，用於批次產生可以匯入至 [DOMjudge](https://www.domjudge.org/) 的 `teams.json` 與 `accounts.json`，並同時產生便於列印發放的密碼紙 (Word 文件)。

## ✨ 主要功能

- **批次產生隊伍與帳號**：透過簡單的 txt 檔案讀入隊伍名稱與使用者名單。
- **安全的隨機密碼**：自動產生易讀且安全的隨機密碼（排除易混淆字元如 `0, o, O, l, I, 1`）。
- **密碼紙匯出**：自動產生包含隊伍名稱、帳號與密碼的 Word 文件，方便比賽當天裁切發放給選手。
- **高度客製化**：可設定隊伍隸屬的分類 (Categories)、機構 (Organizations)、以及 Scoreboard 上的顯示方式（實名或匿名）。
- **備用帳號產生**：可以指定數量，一次建立額外的備用隊伍與帳號。

## 📁 檔案結構說明

在執行腳本前，可以根據需求準備以下檔案（若無特殊需求，檔案可留空）：

- `teams.txt`：隊伍名稱列表，每行一個隊伍名稱。
- `users.txt`（可選）：設定讓後台看見的具體使用者姓名。若提供，行數需與 `teams.txt` 一致。
- `passwords.txt`（可選）：若想自訂密碼可填入，若留空將自動隨機產生。若提供，行數需與 `teams.txt` 一致。

## ⚙️ 腳本變數設定

在執行前，請至 `.py` 腳本 (`create_team.py` 與 `create_account.py`) 中修改全域變數，以符合您的比賽設定：

- `iterater_team_id`：設定第一個帳號的起始編號。例如設為 `1`，將會依序產生 `team001`, `team002`...（請注意不要與 DOMjudge 系統中既有的隊伍編號衝突）。
- `else_team_count`：欲額外產生的「備用帳號」數量。備用帳號除了供現場臨時隊伍使用外，在計分板上的預設名稱會跟隨其帳號 ID。
- `CATAGORIES_EXTERNAL_ID`：隊伍隸屬的群組（Group）。需至 DOMjudge 後台的 `Team Categories` 複製其 `external_id`。
- `ORGANIZATION_EXTERNAL_ID`：隊伍隸屬的機構（Organization）。需至 DOMjudge 後台的 `Team Affiliations` 複製 `external_id`（若不需要設定，在程式中將相關附值註解掉即可）。
- `LOCATION`：隊伍所屬的國家 / 區域代碼（預設為 `TWD`）。

### 🏆 計分板 (Scoreboard) 隊名顯示設定

- **顯示自創隊名**：至 `create_team.py` 的 `create_team_data()` 函式內，將 `"display_name": str(team_name)` 取消註解，這樣計分板上就會顯示 `teams.txt` 內的自設隊名。
- **匿名隊名 (預設)**：程式預設將 `display_name` 設定為 `"team{:03}".format(iterater_team_id)`。計分板上將統一顯示帳號名稱（`teamXXX`），但密碼紙依舊會打上真實隊名以便現場人員發放。

## 🚀 使用流程

1. **安裝依賴套件**
   本專案使用 `python-docx` 來產生密碼紙 Word 檔案。在執行前請確保已安裝該套件：
   ```bash
   pip install python-docx
   ```

2. **準備資料**
   填寫前述提到的 `teams.txt` 及其他對應的文字檔。
   *(如果想直接大量建立純編號隊伍，請將 `teams.txt` 留空，並調整 `else_team_count` 指定要創建的數量即可)*

3. **執行腳本**
   分別或一併執行這兩個產生腳本：
   ```bash
   python create_team.py
   python create_account.py
   ```
   腳本執行完畢後，資料夾內會產生 `teams.json`、`accounts.json`，以及給選手的密碼紙 `passwords.docx` (名稱根據腳本設定而定)。

4. **匯入至 DOMjudge**
   進入 DOMjudge 的系統管理員後台：
   - 前往 **Import -> Import JSON / YAML**
   - **第一步 (隊伍)**：Type 選擇 `team`，File 選擇剛剛產生的 `teams.json`，點擊匯入。
   - **第二步 (帳號)**：Type 選擇 `account`，File 選擇剛剛產生的 `accounts.json`，點擊匯入。

   > **⚠️ 注意事項：**
   > 必須嚴格遵守上述順序 (先 Teams 後 Accounts)。
   > 因為 DOMjudge 匯入時不挑檔名，若您要將不同群組 (如不同 `organization_id`) 的隊伍分開創立，請採分批處理：修改變數 👉 執行腳本 👉 匯入 DOMjudge 👉 修改變數並處理下一批。