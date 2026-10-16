# 文字清理器：全書練習範例

需求：從標準輸入讀取文字，移除每行前後空白，刪除空白行，保留非空行內部的空格與 Unicode 文字。只使用 Python 標準函式庫；不呼叫網路、不保存輸入。

此範例可從 GitHub 下載：<https://github.com/t945935/free-ai-learning-book-examples>。ZIP 解壓後，進入 `examples/text-cleaner/`。

## 執行與測試

在此資料夾執行：

```sh
python3 text_cleaner.py <<'EOF'
  第一行

  第二行
EOF
```

預期輸出：

```text
第一行
第二行
```

執行測試：

```sh
python3 -m unittest -v
```

預期為 4 個測試通過。測試實際結果應以讀者本機輸出為準。

## OpenCode 練習設定

資料夾內的 `opencode.json` 是本練習專用權限設定範例：預設拒絕未列出的操作，允許專案內讀取／列檔／路徑搜尋但拒絕 grep，編輯和執行命令都需詢問，禁止工作目錄外存取與網頁工具。OpenCode 設定會合併全域與專案設定；若全域設定或受管理設定不同，實際權限需在目前版本確認。此設定檔已在隔離的 OpenCode 1.19.0 設定環境由 `opencode debug config` 解析；尚未用模型實際測試拒絕／詢問行為。使用前仍請依 OpenCode 官方 Permissions 文件複核。

OpenCode CLI 已在作者環境確認版本 1.19.0，`opencode --help` 顯示可用專案路徑啟動；未連接模型、未呼叫 `opencode run`，也未驗證模型對話。若你已確認不會產生費用、且有可用模型，可在此資料夾執行 `opencode .` 開啟介面。若沒有免費可用模型，跳過 Agent 對話，仍可完成本範例程式與測試；不要為完成本書啟用計費。

## 安全邊界

此範例只處理標準輸入文字，不存檔、不連網、不安裝第三方套件。任何模型連線都可能將提示與必要上下文送至所選服務，勿輸入敏感內容。專案權限設定是額外保護，不是作業系統沙箱；開始前檢查實際載入設定與工作目錄。

## 檔案

- `.gitignore`：忽略 Python 執行測試產生的 `__pycache__/` 與位元組碼，不把它們當成程式變更。
- `text_cleaner.py`：可執行程式。
- `test_text_cleaner.py`：標準函式庫單元測試。
- `opencode.json`：練習用權限設定；不是沙箱。
