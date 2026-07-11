# FDE 必備知識教科書

> Forward Deployed Engineer（FDE）必備知識的完整中文教學——從 LLM 原理到企業部署，9 章、比喻先行、面試導向。

**線上閱讀：https://katelin013.github.io/fde-textbook/**

---

## 為什麼有這本書

FDE 被稱為 2026 年最熱門的工程職位：嵌入客戶環境、從需求拆解到上線維運、端到端交付 AI 解決方案的工程師——半工程師、半顧問、全責任者。這個角色由 Palantir 開創，如今從 OpenAI 到台灣的 AI 新創都在招募。

但 FDE 需要的知識散落各處：LLM 原理在論文裡、RAG 實務在部落格裡、企業部署的眉角在踩過坑的人腦子裡，而且**成體系的中文教材幾乎不存在**。這本書把它們整理成一條可以循序學習的路徑。

## 這本書寫給誰

- 有工程底子、想系統性補齊 AI 應用知識的後端／全端工程師
- 準備 FDE、Solutions Engineer、AI Engineer 等客戶導向職位面試的人
- 需要向企業客戶解釋 AI 系統「為什麼能用、為什麼可信」的技術顧問

不需要機器學習背景——全書從零講起，白話與比喻優先，數學公式零出現。

## 章節目錄

| 章 | 主題 | 核心比喻 |
|---|---|---|
| [Ch1](https://katelin013.github.io/fde-textbook/ch1-llm-basics/) | LLM 是怎麼運作的 | 超強的接龍機器：token、context window、成本與天生限制 |
| [Ch2](https://katelin013.github.io/fde-textbook/ch2-prompt-engineering/) | Prompt Engineering | 把玄學變工程：prompt 是規格書，不是咒語 |
| [Ch3](https://katelin013.github.io/fde-textbook/ch3-rag/) | RAG | 讓模型開卷考試：chunking、embedding、hybrid search、reranking 全鏈路 |
| [Ch4](https://katelin013.github.io/fde-textbook/ch4-agents/) | Agent 與 Tool Use | 從回答問題到完成任務：做錯事的半徑控制 |
| [Ch5](https://katelin013.github.io/fde-textbook/ch5-mcp/) | MCP | AI 界的 USB-C：用標準協定解掉 N×M 整合問題 |
| [Ch6](https://katelin013.github.io/fde-textbook/ch6-evals/) | Evals | 怎麼證明 AI 系統真的有效：demo 與 production 的分界線 |
| [Ch7](https://katelin013.github.io/fde-textbook/ch7-choosing-approach/) | 技術選型 | Prompting vs RAG vs Fine-tune：由便宜到貴的決策順序 |
| [Ch8](https://katelin013.github.io/fde-textbook/ch8-security/) | 安全 | Prompt Injection 與縱深防禦：prompt 不是安全邊界 |
| [Ch9](https://katelin013.github.io/fde-textbook/ch9-enterprise-deployment/) | 企業部署 | 從 demo 到 production：「模型做得到」與「組織敢不敢用」之間的全部工程 |

## 每章固定結構

1. **本章目標**——讀完你能做到什麼（可驗證的能力，不是「了解」）
2. **主體教學**——比喻開場、白話講解、架構圖與程式範例
3. **常見誤解**——實務與面試中最容易踩的坑，逐條拆解
4. **自我檢測**——口頭作答題附摺疊參考答案，適合自測或互考
5. **面試連結**——這章對應 FDE 面試的哪些考點

## 貫穿全書的立場

- **工程對策思維**：LLM 的每個限制（幻覺、視窗、過期）都接一個工程解法——企業導入 AI 的瓶頸從來不是模型不夠聰明，而是周邊工程沒做齊
- **Eval 驅動**：沒有評估體系的 AI 系統只是 demo；eval set 就是 AI 系統的測試套件
- **安全即架構**：權限過濾做在檢索層、人審關卡做在動作層——靠 prompt 防守等於在門上貼「請勿闖入」的紙條
- **企業現實優先**：SSO、RBAC、審計、變更管理不是附錄，是 FDE 工作的主體

## 本地開發

```bash
git clone https://github.com/katelin013/fde-textbook.git
cd fde-textbook
uvx --from mkdocs-material mkdocs serve     # 本地預覽 http://127.0.0.1:8000
uvx --from mkdocs-material mkdocs gh-deploy # 建置並部署到 GitHub Pages
```

```
.
├── mkdocs.yml     # 站台設定（MkDocs Material、繁中介面、全文搜尋）
└── docs/
    ├── index.md   # 首頁導讀
    └── ch1–ch9    # 九章內容
```
