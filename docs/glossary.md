# 名詞速查表

FDE 必備 AI 術語一覽——英文全名、中文、一句話說明。依主題分組，對應各章內容，可快速掃過查閱。

## LLM 基礎（Ch1）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **LLM**（Large Language Model） | 大型語言模型 | 讀過海量文字、靠「預測下一個字」運作的模型；會寫程式、對話、推理，但本質是接龍不是查證。 |
| **Token** | 詞元 | 模型處理文字的最小單位；成本、容量、速度都以它計量。 |
| **Context Window** | 上下文視窗 | 模型單次能「看見」的 token 總量上限；塞不下的內容模型就看不到。 |
| **Temperature** | 溫度 | 控制輸出隨機性的參數；低＝穩定可重現，高＝多樣有創意。 |
| **Hallucination** | 幻覺 | 模型一本正經地講錯話；源於它在接龍而非查證。 |
| **Streaming** | 串流輸出 | 邊生成邊回傳，讓使用者更快看到第一個字。 |
| **TTFT**（Time To First Token） | 首字延遲 | 使用者從送出到看到第一個字的等待時間；體驗關鍵指標。 |
| **Inference** | 推論 | 模型「跑一次、產生輸出」的過程；對應訓練（training）。 |
| **Prompt Caching** | 提示快取 | 把每次都一樣的開頭（前綴）快取起來，省成本、加速。 |

## Prompt Engineering（Ch2）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **Prompt** | 提示詞 | 你餵給模型的指令與內容，決定它怎麼回答。 |
| **System Prompt** | 系統提示 | 設定模型角色與規則的最高層指令，通常放在對話最前面。 |
| **Zero-shot / Few-shot** | 零樣本 / 少樣本 | 不給範例 / 給幾個範例讓模型照著做。 |
| **Chain-of-Thought**（CoT） | 思維鏈 | 讓模型「一步一步想」再作答，提升推理正確率。 |
| **Structured Output** | 結構化輸出 | 要求模型輸出固定格式（如 JSON），方便程式接手處理。 |

## RAG（Ch3）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **RAG**（Retrieval-Augmented Generation） | 檢索增強生成 | 先從你的資料庫撈相關內容，再餵給模型作答，讓它用上私有知識。 |
| **Embedding** | 嵌入向量 | 把文字轉成一串數字（向量），讓語意相近的內容數值也相近。 |
| **Vector Database** | 向量資料庫 | 專門存放 embedding、支援「找語意最相近」查詢的資料庫。 |
| **Chunking** | 切塊 / 分段 | 把長文件切成小段再做嵌入與檢索。 |
| **Semantic Search** | 語意搜尋 | 依「意思」而非關鍵字比對來找內容。 |
| **Reranking** | 重排序 | 對初步檢索結果再精排一次，把最相關的往前放。 |

## Agent（Ch4）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **Agent** | 代理 / 智能體 | 能自己規劃步驟、呼叫工具、循環執行以達成目標的 AI 系統。 |
| **Tool Use / Function Calling** | 工具呼叫 / 函式呼叫 | 讓模型呼叫外部函式（查資料、算數、打 API），取得它本身沒有的能力。 |
| **ReAct**（Reason + Act） | 推理並行動 | 「思考→行動→觀察」循環的經典 agent 模式。 |
| **Orchestration** | 編排 | 協調多個步驟／工具／模型的整體流程控制。 |

## MCP（Ch5）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **MCP**（Model Context Protocol） | 模型情境協定 | 讓 AI 應用用統一標準連接外部工具與資料源的開放協定。 |
| **MCP Server / Client** | MCP 伺服端 / 用戶端 | Server 提供工具與資料，Client（AI 應用）去連接使用。 |

## 技術選型（Ch7）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **Fine-tuning** | 微調 | 用額外資料再訓練模型，改變它的行為或風格。 |
| **Prompt vs RAG vs Fine-tune** | 三種調校手段 | 由便宜到貴的選型順序：先 Prompt、再 RAG、最後才 Fine-tune。 |

## Evals（Ch6）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **Evals**（Evaluations） | 評估 | 用測試集量化 AI 輸出品質的機制，是 AI 版的自動化測試。 |
| **Ground Truth** | 標準答案 / 基準真值 | 拿來比對模型輸出對錯的正確答案。 |
| **LLM-as-a-Judge** | 以 LLM 當評審 | 用另一個 LLM 來自動評分模型輸出的好壞。 |
| **Regression** | 回歸（測試） | 改動後用測試集確認「原本會的沒變壞」。 |

## 安全（Ch8）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **Prompt Injection** | 提示注入 | 攻擊者把惡意指令藏在輸入資料裡，騙模型執行。 |
| **Jailbreak** | 越獄 | 用話術繞過模型的安全限制，讓它做本該拒絕的事。 |
| **Guardrails** | 護欄 | 在模型前後加的檢查與過濾機制，擋住不當輸入／輸出。 |

## 企業部署與基礎設施（Ch9 / Ch10）

| 名詞 | 中文 | 一句話說明 |
|---|---|---|
| **Latency** | 延遲 | 從請求到回應的耗時；直接影響使用者體驗。 |
| **Throughput** | 吞吐量 | 單位時間能處理的請求量；影響規模與成本。 |
| **Batch API** | 批次 API | 把不急的工作批次送出、非即時處理，通常半價。 |
| **SLA**（Service Level Agreement） | 服務等級協議 | 供應商對可用度／延遲等的承諾指標。 |
| **FDE**（Forward Deployed Engineer） | 前進部署工程師 | 進到客戶現場、把 AI 產品實際落地整合的工程師角色。 |

---

## AI CLI 工具跨工具對照

三大 AI 編碼 CLI：**Claude Code**（Anthropic）、**Gemini CLI**（Google）、**Codex CLI**（OpenAI）。同一個功能在三個工具常有不同名稱／檔名，下表對照，並附一句用途。

| 概念（用途） | Claude Code | Gemini CLI | Codex CLI |
|---|---|---|---|
| **專案指令／記憶檔**<br>告訴 AI 專案規則、慣例、架構，每次對話都會讀 | `CLAUDE.md` | `GEMINI.md` | `AGENTS.md` |
| **設定檔**<br>權限、預設模型、環境變數等組態 | `.claude/settings.json` | `.gemini/settings.json` | `~/.codex/config.toml` |
| **自訂斜線指令**<br>把常用 prompt 存成 `/指令` 一鍵重用 | 斜線指令<br>`.claude/commands/*.md` | 自訂指令<br>`.gemini/commands/*.toml` | 自訂 prompt<br>`~/.codex/prompts/*.md` |
| **Skills 技能**<br>附教學檔的工作流，AI 依情境自動套用 | Agent Skills（`SKILL.md`，自動觸發） | 由 Extensions 提供 | Skills（`~/.codex/skills/…/SKILL.md`） |
| **Subagents 子代理**<br>開分身、以獨立情境跑子任務 | Subagents（`.claude/agents/*.md`） | 原生尚無 | 原生尚無（可搭 Agents SDK） |
| **Plugins／Extensions 外掛**<br>把技能、指令、MCP 打包成可安裝、可版控的單元 | Plugins（打包 skills／agents／commands／hooks／MCP） | Extensions（`gemini-extension.json`） | 無官方外掛系統 |
| **Marketplace 市集**<br>讓外掛可被搜尋、安裝、更新的來源 | 有（`/plugin marketplace add …`） | 有（`gemini extensions install …`） | 無官方市集 |
| **MCP 伺服器**<br>用統一協定讓 AI 連接外部工具與資料源 | 支援 | 支援 | 支援 |

### 規則要定義在哪？

要幫這三個 CLI 定專案規則（慣例、架構、風格、禁止事項），就寫進各自的**專案指令檔**——放在專案根目錄，每次對話都會自動讀入：

- **Claude Code** → `CLAUDE.md`
- **Gemini CLI** → `GEMINI.md`
- **Codex CLI** → `AGENTS.md`

三者也都支援放在家目錄（如 `~/.claude/CLAUDE.md`）當作跨專案的**全域規則**。其中 **`AGENTS.md` 正逐漸成為跨工具的開放標準**：Codex CLI 原生讀它，Gemini CLI 也能在 `settings.json`（`context.fileName`）設定改讀 `AGENTS.md`——想「寫一份規則餵多個工具」，優先選 `AGENTS.md`。

（`.cursor/rules`、`.windsurfrules` 這類「rules」檔是 Cursor／Windsurf 等**編輯器型**工具的用法，跟上面三個 CLI 無關。）

---

## AI 工程範式演進：從 Prompt 到 Loop

跟 AI 協作的「主要技能」這幾年一路往上抽象——瓶頸從「你說的字」→「你給的上下文」→「你寫的規格」→「你設計的迴圈」。四個階段是**累加**的，不是互相取代：loop engineering 裡面照樣用得到 prompt engineering。

| 演進階段 | 年代 | 核心提問 | 一句話說明 |
|---|---|---|---|
| **Prompt Engineering**<br>提示工程 | ~2022–2024 | 「我該怎麼說，才能得到最好的一次輸出？」 | 雕琢單次指令：few-shot、CoT、角色扮演、XML 標籤。追求「一次輸入 → 一次最佳輸出」。 |
| **Context Engineering**<br>情境工程 | 2025 | 「我該在上下文視窗裡放什麼？」 | 由 Karpathy 帶起：單一 prompt 不夠，要動態組裝整個 context——檢索文件、對話歷史、工具定義、RAG 結果。 |
| **Spec-Driven Development**<br>規格驅動開發（SDD，又稱 Spec Engineering） | 2025 | 「我該寫出什麼規格，讓 agent 照著蓋？」 | 不再逐句下指令，而是先寫清楚規格書，交給 agent 實作（GitHub Spec Kit、AWS Kiro 是代表工具）。 |
| **Loop Engineering**<br>循環工程（又稱 Harness Engineering） | 2026 | 「我該設計什麼系統，讓 agent 自己找事、做完、驗證、記住——不用我在迴圈裡？」 | 2026 年 6 月出現。重點從「寫 prompt」變成「設計驅動 agent 的迴圈」：生成端便宜地重複跑，真正的瓶頸在 verifier（驗證器）。 |

> **給 FDE 的重點**：談到「prompt engineering 會不會被淘汰」，正確框架是——它沒被淘汰，是被**包進**更上層的技能裡。能講出這條演進線（prompt → context → spec → loop）、並說明「瓶頸為何一路往上移」，就是在展現你跟得上、也想得清楚。

*註：`spec engineer` 與 `sdd engineer` 其實是同一件事（SDD ＝ Spec-Driven Development），上表已合併；`context engineering` 是你原本清單漏掉、但很關鍵的一環，已補上。*
