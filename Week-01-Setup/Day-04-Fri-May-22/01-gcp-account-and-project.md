# 01 — GCP Account + First Project

## 🧒 Layman explanation

GCP is structured like a tree:

```
Organization  (skip — only enterprises have this)
├── Folder    (skip)
│   └── Project   ← This is YOUR sandbox
│       ├── Cloud Run services
│       ├── Vertex AI calls
│       ├── Secret Manager secrets
│       └── ...everything else
```

A **GCP project** is the **isolation boundary** for everything: APIs, IAM, billing, quotas. You'll create one personal project today for your AI Engineer work. Everything for the next 8 months lives inside it.

Two important rules:

1. **One project per "thing".** Don't mix Walmart experiments with personal portfolio work — separate projects. We're creating a **personal-portfolio** project today.
2. **Use a personal email.** Don't use `@walmart.com` — corporate workspaces can't independently own GCP projects (they roll up to the org).

---

## 💻 Hands-on — create the account + project

### Step 1 — Sign up for GCP

1. Open https://console.cloud.google.com/freetrial
2. Sign in with your **personal Google email** (Gmail / personal Workspace)
3. Country: India (or wherever you legally reside)
4. Accept terms
5. **Add a credit card** for verification. The $300 free trial credit is yours; you won't be charged for Vertex hello-world calls (they cost ~$0.001 each).
6. Complete the welcome wizard

### Step 2 — Create your first project

GCP auto-creates a "My First Project" — rename it or create a fresh one. I recommend a fresh one with a clean name.

1. Top bar → project selector (says "My First Project")
2. Click **New Project**
3. **Project name:** `ai-engineer-portfolio`
4. **Project ID:** GCP auto-generates one like `ai-engineer-portfolio-123456`. **Save this** — it's the immutable handle you'll use everywhere.
5. **Organization:** No organization
6. **Billing account:** Auto-attached (the one you signed up with)
7. Click **Create**
8. Once created, the top bar switches to the new project

### Step 3 — Note your IDs

You'll need three values for the rest of Week 1+2. Write them down:

| Value                | Where to find it                                      | Used for                                |
|----------------------|-------------------------------------------------------|------------------------------------------|
| **Project ID**       | Project selector → shows under name                  | Everything — Vertex calls, gcloud, IAM   |
| **Project Number**   | Project selector → details                            | IAM bindings, service accounts           |
| **Default Region**   | Pick `us-central1`                                    | Vertex location for Gemini calls         |

> 💡 **Why `us-central1`?** Vertex AI Gemini availability is broadest there. `asia-south1` (Mumbai) is closer for you latency-wise but has fewer model SKUs available. Stick with `us-central1` for now — the latency hit is < 200ms, acceptable for dev.

### Step 4 — Optional but recommended: pin to your shell

For convenience, store the project ID in your `~/.zshrc`:

```bash
echo 'export GCP_PROJECT_ID="ai-engineer-portfolio-123456"  # replace with yours' >> ~/.zshrc
echo 'export GCP_LOCATION="us-central1"' >> ~/.zshrc
source ~/.zshrc
```

Now `echo $GCP_PROJECT_ID` works in every new terminal. You'll use it shortly.

---

## 🔧 Technical deep-dive — what a GCP project actually is

```mermaid
flowchart TD
    PROJ[Project: ai-engineer-portfolio] --> APIs[Enabled APIs<br/>Vertex, GenLang, Cloud Run...]
    PROJ --> IAM[IAM policies<br/>who can do what]
    PROJ --> RES[Resources<br/>Cloud Run services, buckets, etc.]
    PROJ --> BILL[Linked billing account]
    PROJ --> QUOTA[Per-service quotas]
    PROJ --> LOGS[Cloud Logging<br/>everything logged here]

    BILL -.alerts.-> EMAIL[your-email@]
```

Everything you do this year happens inside this project box. Deleting the project deletes everything — clean for personal projects, terrifying for prod.

---

## 🚨 The "$300 free trial credit" trap

GCP gives new accounts $300 of free credit valid for 90 days. After 90 days OR after you spend $300 (whichever first), you're billed normally.

This week you'll spend pennies. But two future traps:

1. **Don't enable BigQuery casually** — it has minimum storage costs that can sneak up
2. **Don't keep a Cloud SQL instance idle** — even 0-traffic instances run ~$50/mo
3. **DO enable the $50/month alert** (next lesson)

---

## 📚 References

- **GCP Free Tier explanation** — https://cloud.google.com/free
- **Project naming rules** — https://cloud.google.com/resource-manager/docs/creating-managing-projects
- **"My First Project" guide** — https://cloud.google.com/docs/get-started

---

## ✅ Exit criteria

- [ ] GCP account active under my personal email
- [ ] Project `ai-engineer-portfolio` (or similar) created
- [ ] I know my **Project ID** + **Project Number**
- [ ] Billing account attached
- [ ] (Optional) `GCP_PROJECT_ID` env var pinned in `~/.zshrc`

**Next:** [`02-enable-apis.md`](02-enable-apis.md)

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
