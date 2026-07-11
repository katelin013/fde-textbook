# FDE 轉職學習筆記

> 一個寫了十多年程式的工程師，想轉職成為 Forward Deployed Engineer（FDE），一邊學習、一邊整理的筆記。

## 什麼是 FDE？

Forward Deployed Engineer（前線部署工程師）是由 Palantir 開創、近年被 AI 公司發揚光大的角色：不是待在總部開發產品，而是被「部署」到客戶那裡——嵌入客戶的環境，把公司的產品（現在多半是 AI）變成客戶業務裡真正能用的東西。從業務需求拆解、快速原型、系統整合，到部署上線與持續維運，端到端負責。

我讀過最傳神的一句定義來自 Palantir：「FDE 的職責類似新創公司的 CTO——小團隊、端到端擁有高風險專案的執行。」一般工程師是「一個能力，服務多個客戶」；FDE 是「一個客戶，動用多種能力」。

## 為什麼這個角色重要？

因為 AI 模型的能力（一個會回話的 API）和企業真正要的價值（一個尊重權限、不亂幻覺、真的替團隊省時間的系統）之間，隔著一段很長的距離：資料整合、權限、評估、合規、維運。模型愈強，這段「最後一哩」的工程愈值錢——而它沒辦法遠端隔空完成，需要有人進到客戶的環境裡把它補起來。這個人就是 FDE。

這也是為什麼從 2025 年起 FDE 職缺爆發性成長、被稱為最熱門的工程職位之一：從 OpenAI、Palantir 到台灣的 AI 公司都在招。對像我這樣有多年系統開發經驗、又投入 AI 協作開發的工程師來說，它是一條把過去累積和新技能接在一起的轉職路徑。

## 為什麼有這份筆記

準備轉職的過程中我發現，FDE 需要的知識散得很開——LLM 原理、RAG、Agent、評估方法、企業部署的眉角，各自在不同的文件和文章裡，成體系的中文整理又少。與其零碎地讀，我選擇把自己讀過、消化過、動手試過的東西整理成一份有順序的筆記：先讓自己複習用，如果剛好能幫到同樣在準備的人，那就更好了。

先說在前面：我不是 AI 專家。內容以公開資料與我自己的實作經驗為主，難免有理解不到位的地方，歡迎開 [Issue](https://github.com/katelin013/fde-textbook/issues) 指正，我會很感激。

## 筆記涵蓋的九個主題

| 章 | 主題 | 我用來幫助自己理解的比喻 |
|---|---|---|
| [Ch1](docs/ch1-llm-basics.md) | LLM 是怎麼運作的 | 超強的接龍機器：token、context window、成本與天生限制 |
| [Ch2](docs/ch2-prompt-engineering.md) | Prompt Engineering | 把玄學變工程：prompt 是規格書，不是咒語 |
| [Ch3](docs/ch3-rag.md) | RAG | 讓模型開卷考試：chunking、embedding、hybrid search、reranking |
| [Ch4](docs/ch4-agents.md) | Agent 與 Tool Use | 從回答問題到完成任務：做錯事的半徑控制 |
| [Ch5](docs/ch5-mcp.md) | MCP | AI 界的 USB-C：用標準協定解掉 N×M 整合問題 |
| [Ch6](docs/ch6-evals.md) | Evals | 怎麼知道 AI 系統真的有效：demo 與 production 的分界線 |
| [Ch7](docs/ch7-choosing-approach.md) | 技術選型 | Prompting vs RAG vs Fine-tune：由便宜到貴的決策順序 |
| [Ch8](docs/ch8-security.md) | 安全 | Prompt Injection 與縱深防禦：prompt 不是安全邊界 |
| [Ch9](docs/ch9-enterprise-deployment.md) | 企業部署 | 從 demo 到 production：「模型做得到」與「組織敢不敢用」之間的距離 |

## 每章的結構

這是我自己讀書時習慣的整理方式：

1. **本章目標**——讀完應該能做到什麼（盡量寫成可驗證的能力，不是「了解」）
2. **主體筆記**——比喻開場、白話整理、架構圖與程式範例
3. **常見誤解**——多半是我自己踩過、或差點就誤解的地方
4. **自我檢測**——口頭作答題附參考答案，我拿來檢查自己有沒有真的懂

## 目前為止學到最重要的幾件事

- **限制都有工程對策**：LLM 的每個限制（幻覺、視窗、知識過期）都有成熟的工程解法——難的不是模型，是周邊工程有沒有做齊
- **沒有 eval 就只是 demo**：改動好不好不能靠肉眼看幾個例子，eval set 就是 AI 系統的測試套件
- **prompt 不是安全邊界**：權限過濾要做在檢索層與工具層，靠 prompt 防守等於在門上貼「請勿闖入」的紙條
- **企業在乎的是治理**：SSO、權限、審計、變更管理不是附錄——這正是 FDE 這個角色存在的原因

## 在本地閱讀

筆記用 MkDocs 整理，可以直接在 GitHub 讀 `docs/` 內的 markdown，或在本地起一個帶搜尋和目錄的閱讀介面：

```bash
git clone https://github.com/katelin013/fde-textbook.git
cd fde-textbook
uvx --from mkdocs-material mkdocs serve   # http://127.0.0.1:8000
```

```
.
├── mkdocs.yml     # 站台設定
├── scripts/       # 整理用小工具
└── docs/
    ├── index.md   # 導讀
    └── ch1–ch9    # 九章筆記
```
