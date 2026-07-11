# FDE 必備知識教科書

Forward Deployed Engineer（FDE）必備知識的完整教學：LLM 基礎、Prompt Engineering、RAG、Agent 與 Tool Use、MCP、Evals、技術選型、安全、企業部署——共 9 章，每章含比喻教學、常見誤解與自我檢測。

**線上閱讀：https://katelin013.github.io/fde-textbook/**

## 本地開發

```bash
uvx --from mkdocs-material mkdocs serve    # 本地預覽 http://127.0.0.1:8000
uvx --from mkdocs-material mkdocs gh-deploy # 建置並部署到 GitHub Pages
```

內容源檔在 `docs/`，站台設定在 `mkdocs.yml`。
