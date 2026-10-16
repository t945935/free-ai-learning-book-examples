# 不花錢學 AI｜範例下載

這個公開儲存庫提供《不花錢學 AI》讀者練習檔案；書稿本身不在此 repo。

下載方式：

- ZIP：<https://github.com/t945935/free-ai-learning-book-examples/archive/refs/heads/main.zip>
- GitHub 專案頁：<https://github.com/t945935/free-ai-learning-book-examples>
- 若使用 Git：`git clone https://github.com/t945935/free-ai-learning-book-examples.git`

下載 ZIP 並解壓後，進入 `examples/text-cleaner/`。在 macOS、Linux 或 WSL 終端機執行：

```sh
python3 -m unittest -v
```

若要測試文字清理器：

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

本範例只使用 Python 標準函式庫，不連網、不保存輸入，也不要求模型或 API。Windows 使用者可透過 WSL 執行上述指令；PowerShell 的替代輸入指令尚未在作者環境驗證。

`opencode.json` 是練習用權限設定範例，不是作業系統沙箱。沒有確認費用及資料處理方式的模型時，跳過 Agent 連線即可完成程式與測試練習。不要在範例中放入密碼、API 金鑰、個資或公司資料。

作者驗證範圍：Python 3.14.7 下 4 個單元測試通過；OpenCode 1.19.0 的設定解析已確認，但未連接模型，未驗證工具實際拒絕／詢問行為。其他版本與平台請自行依官方文件核對。

此儲存庫是另行發行之書籍的補充範例，不包含章稿、整合書稿或內部審閱文件。此 repo 目前未附授權檔；若需再散布或用於商業用途，請先取得作者授權。