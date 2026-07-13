# FDE 轉職學習筆記

> 說明在前：這份筆記由 Claude Code 起頭撰寫——我在準備轉職 Forward Deployed Engineer（FDE）的過程中，與它協作整理出這套內容，並持續修訂。我不是 AI 專家，內容難免有理解不到位之處，歡迎到 [GitHub 開 Issue](https://github.com/katelin013/fde-textbook/issues) 指正。

一個寫了十多年程式的工程師，想轉職成為 FDE，一邊學習、一邊整理的筆記。每章從零講起、白話優先、比喻先行。

## 這份筆記講什麼

FDE 是嵌入客戶環境、從需求拆解到上線維運、端到端交付 AI 解決方案的工程師——半工程師、半顧問、全責任者。這份筆記整理了我認為這個角色需要的十個主題。

## 章節目錄

| 章 | 主題 | 一句話 |
|---|---|---|
| [Ch1](ch1-llm-basics.md) | LLM 是怎麼運作的 | 超強的接龍機器：token、context、成本與天生限制 |
| [Ch2](ch2-prompt-engineering.md) | Prompt Engineering | 把玄學變工程：prompt 是規格書，不是咒語 |
| [Ch3](ch3-rag.md) | RAG | 讓模型開卷考試：檢索增強生成全鏈路 |
| [Ch4](ch4-agents.md) | Agent 與 Tool Use | 從回答問題到完成任務：做錯事的半徑控制 |
| [Ch5](ch5-mcp.md) | MCP | AI 界的 USB-C：N×M 問題的標準解 |
| [Ch6](ch6-evals.md) | Evals | 怎麼證明 AI 系統真的有效：demo 與 production 的分界線 |
| [Ch7](ch7-choosing-approach.md) | 技術選型 | Prompting vs RAG vs Fine-tune：由便宜到貴的決策順序 |
| [Ch8](ch8-security.md) | 安全 | Prompt Injection 與縱深防禦：prompt 不是安全邊界 |
| [Ch9](ch9-enterprise-deployment.md) | 企業部署 | 從 demo 到 production：組織敢不敢用的工程 |
| [Ch10](ch10-infra-basics.md) | 基礎設施複習 | Linux、Networking、K8s：把生鏽的維運知識擦亮成白板等級 |

## 每章結構

1. **本章目標**——讀完你能做到什麼
2. **主體筆記**——比喻開場、白話整理、圖解與程式範例
3. **常見誤解**——實務中最容易踩的坑
4. **自我檢測**——附參考答案（點開摺疊區塊對答案）

## 建議讀法

- **第一次讀**：Ch1 → Ch2 → Ch3 → Ch6（先建立「LLM—prompt—RAG—評估」的主幹），再讀 Ch4/Ch5（agent 與整合），最後 Ch7/Ch8/Ch9（決策、安全、企業）。
- **快速複習時**：直接刷各章的「常見誤解」與「自我檢測」。
- **維運基礎生疏時**（Linux／網路／K8s）：隨時翻 Ch10 複習，它是獨立的。

