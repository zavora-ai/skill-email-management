# Email Tool Sequences

## Tools (9)
| Tool | Purpose |
|------|---------|
| `send_email` | Compose and send |
| `list_inbox` | List messages (filter: unread, from, date) |
| `get_email` | Full message content |
| `search_emails` | Search by query |
| `reply_to_email` | Reply in thread |
| `list_labels` | Available folders/labels |
| `move_to_folder` | Organize messages |
| `mark_read` | Mark as read |
| `get_attachments` | Download attachments |

## Sequence: Send Professional Email (1 call)
```
send_email(to: "client@acme.com", subject: "Invoice #123 — $550 due Feb 15", body: "Hi Sarah,\n\nPlease find attached...\n\nBest,\nTeam", cc: "billing@company.com")
```

## Sequence: Process Inbox (3 calls)
```
1. list_inbox(unread_only: true, limit: 10) → [{id, from, subject, date}]
2. get_email(id: "msg_important") → full body + headers
3. reply_to_email(id: "msg_important", body: "Thanks, I'll review and get back to you by EOD.")
```
