# Ch10 Infrastructure Refresher: Linux, Networking, K8s

> This is positioned as an **interview refresher**, not teaching from scratch — it polishes rusty ops knowledge back up to the "can explain it at a whiteboard" level. (Almost every FDE job description spells it out: Linux, Networking, Cloud-Native & Container.)

## Chapter Goals

By the end you'll be able to: (1) walk through the whole "type a URL in the browser to the page showing up" flow at a whiteboard; (2) explain clearly what happens to a K8s Pod from `apply` to Running, and how to debug it when it breaks; (3) use basic tools in a customer environment to pin down "the service is unreachable / running slow."

---

## 10.1 The Classic Question: From Typing a URL to Seeing the Page

When you get asked this in an interview, deliver it with an "outside-in, one sentence per layer" rhythm:

1. **DNS**: the browser asks "whose IP does this name map to" — first the local cache → OS/hosts → recursive resolver (ISP or 8.8.8.8) → root → TLD → authoritative server. The answer carries a TTL for caching.
2. **TCP three-way handshake**: SYN → SYN-ACK → ACK, establishing the connection (being able to say who goes first is enough).
3. **TLS handshake**: exchange the certificate, negotiate keys — "prove identity + set up an encrypted channel." The certificate chain is signed by a CA, with trust anchors built into the browser.
4. **HTTP request/response**: methods, status codes (2xx success / 3xx redirect / 4xx client error / 5xx server error — be clear on 401 unauthenticated vs 403 no permission).
5. **What it may pass through along the way**: CDN (caches static content close to the user), reverse proxy / load balancer (next section).

> Enterprise-field mapping: when a customer says "we can't reach your service," your debugging order is exactly this chain: is DNS resolving correctly (`dig`) → is the network reachable (`ping`/firewall) → is the port open (`nc -zv host 443`) → has the TLS certificate expired (the browser padlock / `openssl s_client`) → what's the HTTP status code (`curl -v`). **Work down the chain in order — don't jump around guessing.**

## 10.2 Load Balancing and Reverse Proxies

- **Reverse proxy** (nginx-type): the doorman standing in front of your servers — TLS termination, caching, compression, forwarding requests to the backends.
- **LB strategies**: round robin (take turns) / least connections (give it to whoever's idle) / IP hash (pin the same client to the same backend — for when you need session stickiness).
- **L4 vs L7**: L4 forwards by IP/port (fast, doesn't understand the content); L7 looks at the HTTP content (can route by path/header, can do canary releases). In one line: "if you want to split traffic by URL, you must use L7."
- **Health checks**: the LB periodically probes the backends and kicks the dead ones out of rotation — this is the foundation of "rolling updates with no downtime."

## 10.3 The Minimum You Need to Know About Containers and Networking

- **Container vs VM**: a container shares the host kernel; what's isolated is the process view (namespace) and resources (cgroup) — that's why it's light and fast; a VM carries a whole OS each.
- **Image layering**: each instruction in a Dockerfile is a layer, and layers are cached — "change the code but not the dependencies, and the build only reruns the last few layers."
- **Container networking basics**: a container has its own network namespace; to expose it externally you need port mapping; containers connect to each other over the network (compose/K8s give them DNS names).
- **Common pitfalls**: inside a container, `localhost` is not the host machine; baking secrets into an image (use environment variables / secret management instead).

## 10.4 K8s: Turning Your Ops Experience into Interview Language

**Core objects, one-liner version**:
- **Pod**: the smallest deployable unit (one or more containers that live and die together).
- **Deployment**: declares "I want N copies of this Pod," and handles rolling updates and rollbacks.
- **Service**: Pods die and get new IPs, so a Service gives one stable virtual IP + DNS name and directs traffic to the live Pods (ClusterIP for internal / NodePort/LoadBalancer for external).
- **Ingress**: the L7 routing entry point (forwards to different Services by domain/path).
- **ConfigMap/Secret**: mounting configuration and secrets.

**A must-know flow: what happens after `kubectl apply`**
The API Server receives it and stores it in etcd → the Scheduler picks a node → that node's kubelet pulls the image and starts the container → only after the readiness probe passes does it enter the Service's rotation.

**The Pod-broke debugging playbook (memorize it — you'll use it daily in the field)**:
```
kubectl get pods                 # check status
kubectl describe pod <pod>      # check Events: scheduling failure? can't pull the image? OOMKilled?
kubectl logs <pod> [--previous] # check the container logs (--previous shows the run before the crash)
```
- `ImagePullBackOff` → wrong image name / no credentials for the private registry
- `CrashLoopBackOff` → the container dies as soon as it starts; check logs --previous
- `Pending` → not enough resources or a scheduling constraint; describe to see the Events
- `OOMKilled` → the memory limit is too low, or it's genuinely leaking

**liveness vs readiness** (commonly asked): liveness fails → restart the container; readiness fails → just temporarily stop sending it traffic. The consequence of mixing them up: repeatedly restarting a service that's "still warming up."

## 10.5 The Linux Field Toolbox (When the Customer Environment Has No GUI)

| What to check | Tool | In one sentence |
|---|---|---|
| Who's eating CPU/memory | `top` / `htop` | Start with load and the resource-hungry processes |
| Is the disk full | `df -h`, `du -sh *` | The common truth behind "the service died" is a full disk |
| Who's listening on which port | `ss -tlnp` | Is the service up, is the port right |
| Can it reach out | `curl -v`, `nc -zv host port` | Distinguish DNS error / connection refused / timeout |
| Service logs | `journalctl -u <svc> -f`, `tail -f` | Look at the most recent errors first |
| Find the error in a file | `grep -rn "ERROR" logs/` | Pair it with `less` — don't flood the screen with cat |
| Permission problems | `ls -l`, `id` | The first reaction to Permission denied |

**How to say it in an interview**: you don't need to memorize every flag — saying "here's my debugging order" already wins half the battle: "first resources (top/df), then networking (ss/curl), then logs (journalctl), narrowing the scope by the evidence."

---

## Common Misconceptions

1. **"A K8s interview means memorizing every object"** — no. Getting fluent on the four (Pod/Deployment/Service/Ingress) plus the debugging playbook beats memorizing 20 terms.
2. **"liveness and readiness are about the same"** — the consequences are completely different (restart vs remove from traffic); mixing them up will make the interviewer's eyes light up (the bad kind).
3. **"Unreachable means it's a network problem"** — "network problem" isn't an answer, it's where the question starts: DNS? routing? firewall? port? certificate? the service itself? Talk it through down the chain.
4. **"A container = a lightweight VM"** — the isolation levels are different; this line will come across as unprofessional in front of a security-sensitive customer.

## Self-Check

1. Walk through "typing a URL to the page appearing" at a whiteboard, one sentence per layer (within 3 minutes).
2. A customer reports "we can't reach your service" — narrate your debugging chain and the command you use at each step.
3. From `kubectl apply` to the Pod being Running, what happens in between?
4. What do `CrashLoopBackOff` and `ImagePullBackOff` each mean, and how do you debug each?
5. The difference between liveness and readiness, and the consequence of mixing them up?
6. How do L4 and L7 load balancing differ? What requirement absolutely needs L7?

## Key Points for the Reference Answers

    1–2. See 10.1 (the debugging chain: dig → ping/firewall → nc port → TLS → curl status code).
    3. See the flow in 10.4 (API Server→etcd→Scheduler→kubelet→readiness→into traffic).
    4. Dies as soon as it starts (check logs --previous) vs can't pull the image (name/credentials); for both, describe first to see the Events.
    5. Restart vs remove from traffic; mixing them up repeatedly kills a service that's still warming up.
    6. L4 looks at IP/port, L7 looks at the HTTP content; routing by path/domain and canary releases need L7.
