# Email Cross-MCP Workflows

## Email + Finance: Invoice Delivery
```
FINANCE: create_invoice(customer: "acme", total: 55000) → {id: "inv_123"}
EMAIL: send_email(to: "billing@acme.com", subject: "Invoice #123 — $550.00", body: "Pay online: [link]")
CRM: create_activity(type: "email", subject: "Invoice #123 sent")
```

## Email + ITSM: Ticket Resolution Notification
```
ITSM: close_ticket(id: "INC-1001", resolution: "Fixed")
EMAIL: send_email(to: requester, subject: "INC-1001 Resolved", body: "Your issue has been resolved...")
```

## Email + CRM: Follow-up After Call
```
CRM: create_activity(type: "call", subject: "Discovery call")
EMAIL: send_email(to: contact, subject: "Great speaking with you", body: "As discussed, here are next steps...")
CRM: create_activity(type: "email", subject: "Follow-up sent")
```

## Email + Customer Service: Proactive Outreach
```
CS: assess_churn_risk(id: "cust_789") → {risk: "high"}
EMAIL: send_email(to: customer, subject: "Checking in", body: "Hi, I noticed...")
CS: start_conversation(customer_id, subject: "Proactive outreach")
```
