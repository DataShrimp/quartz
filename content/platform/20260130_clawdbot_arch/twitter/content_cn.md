# Twitter Thread (中文) - Clawdbot 架构解析

## Thread

**T1 (Hook)**
我在 Mac Mini 上跑了一个 AI "员工" 两周了。

它帮我筛邮件、监控市场、甚至打电话订餐。

这是让 AI 真正"有手"的架构 👇

---

**T2 (Context)**
Clawdbot 在 GitHub 几周内斩获 100k+ Star。

这不是炒作，这是范式转移：

从 **对话型 AI** → **执行型 AI**

AI 不再只是告诉你怎么做，而是自己动手做。

---

**T3 (The Architecture)**
核心秘密：三层架构

🧠 **Brain** – LLM 解析意图
🏠 **Body** – 本地 Node.js 进程，有文件系统权限
🤝 **Hands** – 绑定 Telegram/Slack/微信

这就是把聊天机器人变成打工人的方法。

---

**T4 (Key Differentiator)**
它和 ChatGPT 有什么区别？

| ChatGPT | Clawdbot |
|---------|----------|
| 会话级记忆 | 持久化记忆 |
| 沙盒隔离 | 全系统权限 |
| 被动响应 | 主动触发 |

它有一个 `memory.md` 文件，每次交互都在成长。

---

**T5 (Proactive AI)**
"心跳" 机制：

每 15 分钟自动醒来：
• 检查系统状态
• 扫描未读邮件
• 监控市场变化

发现异常，主动 ping 你。

---

**T6 (Wild Use Cases)**
真实骚操作：

✅ 邮件自动分拣，只推送 VIP 消息
✅ 网页订餐失败？直接用语音 API 打电话
✅ 用 Grok API 实时抓取推特舆情

这才是 Problem Solving。

---

**T7 (The Dark Side)**
但有坑。

有用户让 Agent "找出项目真相"。

结果它把整个 `home` 目录结构 dump 到了公开群...

Shell 权限是双刃剑。⚠️

---

**T8 (The Fix)**
解决方案：**每日复盘**

用 "Reviewer Agent" 审计 "Operator Agent"：

1. 提取行为日志
2. 回放决策过程
3. 纠正错误
4. 更新长期记忆

像带实习生一样带 AI。

---

**T9 (TL;DR)**
总结：

• Clawdbot = AI Agent 网关（Brain-Body-Hands）
• 本地优先，隐私+速度
• 心跳机制实现主动触发
• 风险：上下文腐烂 + 安全事故
• 解法：复盘循环 + 沙盒隔离

---

**T10 (CTA)**
到 2027 年，虚拟员工将成标配。

但决定上限的，依然是人类的**品味**——懂得什么是好活。

完整深度文章：
🔗 blog.datashrimp.space

关注 @datashrimp 获取更多 AI 架构解析。
