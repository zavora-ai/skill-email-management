# Email Management Skill

> Multi-backend email operations for AI agents — compose professional emails, manage inbox, search history, and deliver invoices/follow-ups across SMTP, AWS SES, SendGrid, Gmail, and Microsoft Graph.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--email-green)](https://github.com/zavora-ai/mcp-email)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 9 email tools into **professional communication workflows** — ensuring every outbound email is clear, targeted, and actionable. Email is the universal delivery layer for invoices, follow-ups, and customer communication.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Compose & Send | 1 | Professional email with clear CTA |
| Read Inbox | 1-2 | Filtered inbox with key messages |
| Search | 1-2 | Find messages by sender/subject/date |
| Reply | 2 | Read context → reply in thread |
| Organize | 1-2 | Move, label, archive |

### Without this skill:
- Emails sent without verifying recipient
- No clear subject lines or calls-to-action
- Walls of text instead of scannable content
- CC overuse (everyone gets everything)
- No templates for recurring communications

### With this skill:
- Recipient verified before every send
- Clear subject (action + context in < 60 chars)
- Scannable body (purpose in first sentence, bullets for lists)
- CC only relevant parties
- Templates for invoices, follow-ups, reminders

## Installation

### Claude Code
```bash
git clone https://github.com/zavora-ai/skill-email-management.git \
  ~/.skills/skills/email-management
```

### ADK-Rust
```bash
cp -r email-management /path/to/project/.skills/skills/
```

## Requirements

**Required:**
- `mcp-email` server connected (SMTP, SES, SendGrid, Gmail, or Microsoft Graph)

**Revenue-accelerating combos:**
- `mcp-finance` — deliver invoices with payment links
- `mcp-crm` — send follow-ups after sales calls
- `mcp-payments` — include payment links in collection emails
- `mcp-customer-service` — proactive outreach for at-risk customers

## Folder Structure

```
email-management/
├── SKILL.md                       # Decision tree + 5 workflows + quality rules
├── assets/
│   └── email-templates.md         # Invoice, follow-up, reminder templates
├── references/
│   ├── tool-sequences.md          # 9 tools with exact patterns
│   ├── cross-mcp-workflows.md     # Email + Finance + CRM + ITSM + CS
│   └── examples.md                # 3 real scenarios with traces
├── README.md
└── LICENSE
```

## How It Works

### Decision Tree

```
User request arrives
├── "send", "email", "write to"? → Compose & Send
├── "inbox", "unread"? → Read Inbox
├── "find", "search"? → Search
├── "reply", "respond"? → Reply (read first, then respond)
├── "organize", "move", "archive"? → Organize
```

### Email Quality Rules (enforced automatically)

1. **Verify recipient** before sending
2. **Clear subject** — action + context in < 60 chars
3. **First sentence = purpose** — don't bury the lead
4. **Under 200 words** for business emails
5. **Clear CTA** — what do you need from the reader?
6. **No sensitive data** in email body (credentials, PII)

## Example

**User:** "Send the proposal to Sarah at Acme"

**Agent behavior:**
1. Composes with clear subject, scannable body, and CTA
2. Verifies recipient address
3. Sends via configured backend

**Result:**
```
✅ Sent to sarah@acme.com

Subject: Proposal: Enterprise Plan — Acme Corp
Body: Professional, scannable, with next-step CTA
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on email queries |
| Delivery rate | 100% successful sends |
| No misdirected | Always verify recipient before sending |
| Professional quality | Clear subject + scannable body + CTA |

## MCP Server Compatibility

Designed for [mcp-email](https://github.com/zavora-ai/mcp-email):

| Capability | Tools |
|-----------|-------|
| Send | send_email, reply_to_email |
| Read | list_inbox, get_email, get_attachments |
| Search | search_emails |
| Organize | list_labels, move_to_folder, mark_read |

## Related Skills

- [skill-finance-accounting](https://github.com/zavora-ai/skill-finance-accounting) — Invoice delivery
- [skill-crm-customer-management](https://github.com/zavora-ai/skill-crm-customer-management) — Follow-up emails
- [skill-customer-service-operations](https://github.com/zavora-ai/skill-customer-service-operations) — Proactive outreach

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
