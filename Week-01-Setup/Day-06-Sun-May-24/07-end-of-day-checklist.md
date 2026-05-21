# 07 — Day 6 End-of-Day Checklist

Sunday wrap. Tomorrow is the buffer day + week reckoning + first weekly Hashnode post.

---

## ✅ Tooling verification

```bash
# Tracker
# (manual check — open Notion or Linear and confirm Week 1 + Days 1-6 entries exist)

# AWS
aws --version                              # 2.x ✅
aws sts get-caller-identity                # Arn ends with :user/<your-admin>, not :root ✅
ls -la ~/.aws/                             # credentials chmod 0600 ✅

# Verification script
verify-ai
# 5/5 checks passed. Week 1 stack is healthy. 🎉 ✅
```

If `verify-ai` is not 5/5, **stop and fix it tonight**. Don't carry red checks into Week 2.

---

## ✅ Knowledge checks

- [ ] Why must you never daily-drive the AWS root user? *(blast radius — root can delete the account; IAM admin can't)*
- [ ] What does `aws sts get-caller-identity` prove? *(your CLI credentials are valid + tells you which user/role)*
- [ ] What's the contract of `scripts/week1_verify.py`? *(prints ✅/❌ for each of the 5 hello-worlds; returns exit code 0 only if all pass)*
- [ ] Difference between AWS Bedrock and Vertex AI in one sentence? *(both are managed foundation-model APIs — Bedrock on AWS, Vertex on GCP; same role in their respective ecosystems)*

---

## ✅ Tracker hygiene

Open Notion / Linear and fill in **today's** entry:

- Today's intent: "Tracker + AWS + verification script"
- Done? — all 3 checked
- What I learned (1-3 bullets):
  - …
  - …
- Tomorrow's first move: "Write the Weekly Reckoning + draft Week 1 retrospective blog post"

---

## 🧠 The big idea of Day 6

> **You now have observability over your own stack.**
> `verify-ai` is the first piece of *infrastructure* you'll keep extending for 35 weeks.
> Every new SDK becomes a new check; every check is a tiny insurance policy against
> "I broke something last week and didn't notice."

This is exactly the mindset FDEs need when juggling customer environments.

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
