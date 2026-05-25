# Email Examples

## Example 1: "Send the proposal to Sarah"
```
send_email(to: "sarah@acme.com", subject: "Proposal: Enterprise Plan — Acme Corp", body: "Hi Sarah,\n\nAttached is our proposal for the Enterprise plan as discussed.\n\nKey highlights:\n- Unlimited users\n- Priority support\n- Custom integrations\n\nHappy to schedule a call to walk through it.\n\nBest regards")
```
Response: "✅ Proposal sent to sarah@acme.com"

## Example 2: "Check my inbox for anything from Acme"
```
search_emails(query: "from:acme.com") → [{subject: "Re: Contract terms", date: "2h ago"}, {subject: "Invoice question", date: "yesterday"}]
get_email(id: "msg_1") → full content
```
Response: "2 emails from Acme:\n1. 'Re: Contract terms' (2h ago) — Sarah confirmed legal review complete\n2. 'Invoice question' (yesterday) — Billing asked about pro-rating"

## Example 3: "Reply to the contract email"
```
get_email(id: "msg_1") → {from: "sarah@acme.com", subject: "Re: Contract terms"}
reply_to_email(id: "msg_1", body: "Great news! I'll send the final contract for signature today.")
```
Response: "✅ Replied to Sarah's contract email."
