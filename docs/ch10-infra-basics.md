# Ch10 基礎設施複習：Linux、Networking、K8s

> 定位是**面試複習**，不是從零教學——把生鏽的維運知識擦亮成「白板上講得出來」的程度。（FDE 職缺的 JD 幾乎都明列：Linux、Networking、Cloud-Native & Container。）

## 本章目標

讀完你能：(1) 白板走完「瀏覽器輸入網址到頁面出現」全流程；(2) 講清楚 K8s Pod 從 apply 到 Running 發生什麼、掛了怎麼查；(3) 在客戶環境用基本工具定位「服務連不上／變慢」。

---

## 10.1 經典題：從輸入網址到看到頁面

面試被問這題，用「由外而內、每層一句話」的節奏講：

1. **DNS**：瀏覽器問「這名字的 IP 是誰」——先查本機快取 → OS/hosts → 遞迴解析器（ISP 或 8.8.8.8）→ 根 → TLD → 權威伺服器。答案帶 TTL 快取。
2. **TCP 三向交握**：SYN → SYN-ACK → ACK，建立連線（講得出誰先誰後即可）。
3. **TLS 交握**：交換憑證、協商金鑰——「驗明正身＋建立加密通道」。憑證鏈由 CA 簽發、瀏覽器內建信任錨。
4. **HTTP 請求/回應**：方法、狀態碼（2xx 成功／3xx 轉導／4xx 客戶端錯／5xx 伺服器錯——401 未認證 vs 403 無權限要分得清）。
5. **中間可能經過**：CDN（就近快取靜態內容）、反向代理／Load Balancer（下一節）。

> 企業現場對應：客戶說「連不上你們的服務」，你的除錯順序就是這條鏈：DNS 解析對不對（`dig`）→ 網路通不通（`ping`/防火牆）→ 埠開不開（`nc -zv host 443`）→ TLS 憑證有沒有過期（瀏覽器鎖頭／`openssl s_client`）→ HTTP 狀態碼是什麼（`curl -v`）。**按鏈路排查，不要跳著猜。**

## 10.2 Load Balancing 與反向代理

- **反向代理**（nginx 類）：站在伺服器前面的門房——TLS 終結、快取、壓縮、把請求轉給後端。
- **LB 策略**：round robin（輪流）／least connections（誰閒給誰）／IP hash（同客戶固定同後端——需要 session 黏著時）。
- **L4 vs L7**：L4 看 IP/埠轉發（快、不懂內容）；L7 看 HTTP 內容（能按路徑/標頭路由、能做金絲雀）。一句話：「按 URL 分流就必須 L7。」
- **健康檢查**：LB 定期探測後端，掛的踢出輪替——這是「滾動更新不中斷」的基礎。

## 10.3 容器與網路的最小必要知識

- **容器 vs VM**：容器共用宿主核心、隔離的是行程視角（namespace）與資源（cgroup）——所以輕、快；VM 各帶整個 OS。
- **映像分層**：Dockerfile 每條指令一層、層會快取——「改 code 不改依賴，build 只重跑最後幾層」。
- **容器網路常識**：容器有自己的網路命名空間；對外要 port mapping；容器之間靠網路互連（compose/K8s 給 DNS 名稱）。
- **常見坑**：容器內 `localhost` 不是宿主機；映像裡塞 secrets（要用環境變數／secret 管理）。

## 10.4 K8s：把你的維運經驗變成面試語言

**核心物件一句話版**：
- **Pod**：最小部署單位（一個或多個容器同生共死）。
- **Deployment**：宣告「我要 N 份這個 Pod」，負責滾動更新與回滾。
- **Service**：Pod 會死會換 IP，Service 給一個穩定的虛擬 IP＋DNS 名，把流量導到活著的 Pod（ClusterIP 對內／NodePort/LoadBalancer 對外）。
- **Ingress**：L7 路由入口（按網域/路徑轉發到不同 Service）。
- **ConfigMap/Secret**：設定與機密的掛載。

**必考流程：`kubectl apply` 之後發生什麼**
API Server 收到並存進 etcd → Scheduler 挑節點 → 該節點 kubelet 拉映像、起容器 → readiness probe 過了才進 Service 輪替。

**Pod 掛了的排查劇本（背下來，客戶現場天天用）**：
```
kubectl get pods                 # 看狀態
kubectl describe pod <pod>      # 看 Events：排程失敗？拉不到映像？OOMKilled？
kubectl logs <pod> [--previous] # 看容器日誌（--previous 看崩潰前那次）
```
- `ImagePullBackOff` → 映像名錯／私有倉庫沒憑證
- `CrashLoopBackOff` → 容器起來就死，看 logs --previous
- `Pending` → 資源不夠或排程約束，describe 看 Events
- `OOMKilled` → 記憶體上限太低或真的漏

**liveness vs readiness**（常考）：liveness 失敗 → 重啟容器；readiness 失敗 → 只是暫時不給流量。搞混的後果：把「還在暖機」的服務反覆重啟。

## 10.5 Linux 現場工具箱（客戶環境沒有圖形介面時）

| 要查什麼 | 工具 | 一句話 |
|---|---|---|
| CPU/記憶體誰在吃 | `top` / `htop` | 先看 load 與吃資源的行程 |
| 磁碟滿了嗎 | `df -h`、`du -sh *` | 「服務掛了」的常見真相是磁碟滿 |
| 誰在聽哪個埠 | `ss -tlnp` | 服務起了沒、埠對不對 |
| 連線得出去嗎 | `curl -v`、`nc -zv host port` | 分清 DNS 錯／拒連／逾時 |
| 服務日誌 | `journalctl -u <svc> -f`、`tail -f` | 先看最近的錯誤 |
| 找檔案裡的錯誤 | `grep -rn "ERROR" logs/` | 配 `less` 別用 cat 灌螢幕 |
| 權限問題 | `ls -l`、`id` | Permission denied 的第一反應 |

**面試講法**：不用背全部參數，講出「我的排查順序」就贏一半——「先資源（top/df）、再網路（ss/curl）、再日誌（journalctl）、按證據縮小範圍」。

---

## 常見誤解

1. **「K8s 面試要背所有物件」**——不用。Pod/Deployment/Service/Ingress 四個講熟＋排查劇本，勝過背 20 個名詞。
2. **「liveness 和 readiness 差不多」**——後果完全不同（重啟 vs 摘流量），搞混會把面試官眼睛聽亮（負面的那種）。
3. **「連不上就是網路問題」**——「網路問題」不是答案，是問題的開始：DNS？路由？防火牆？埠？憑證？服務本身？按鏈路講。
4. **「容器=輕量 VM」**——隔離層級不同；這句話在資安敏感的客戶面前會顯得不專業。

## 自我檢測

1. 白板走一遍「輸入網址到頁面出現」，每層一句話（3 分鐘內）。
2. 客戶回報「你們的服務連不上」——口述你的排查鏈與每步用的指令。
3. `kubectl apply` 之後到 Pod Running，中間發生什麼？
4. `CrashLoopBackOff` 和 `ImagePullBackOff` 各代表什麼、各怎麼查？
5. liveness 與 readiness 的差別與搞混的後果？
6. L4 與 L7 負載均衡差在哪？什麼需求一定要 L7？

??? note "參考答案要點"

    1–2. 見 10.1（排查鏈：dig → ping/防火牆 → nc 埠 → TLS → curl 狀態碼）。
    3. 見 10.4 流程（API Server→etcd→Scheduler→kubelet→readiness→進流量）。
    4. 起來就死（看 logs --previous）vs 映像拉不到（名稱/憑證）；都先 describe 看 Events。
    5. 重啟 vs 摘流量；搞混會把暖機中的服務反覆殺掉。
    6. L4 看 IP/埠、L7 看 HTTP 內容；按路徑/網域路由、金絲雀發布要 L7。

## 面試連結

Dcard JD 明列「能熟練操作 Linux」「理解基本 Networking」「Cloud-Native & Container」；AIFT JD 的 on-prem/K8s troubleshooting 整段就是 10.4–10.5。你的加分故事：艾立運能管 GCP/K8s 的實際維運經驗——把當年處理過的一次事故整理成 STAR 故事（S4 候補素材）。
