# 02 — Hashnode Setup

## 🧒 Layman explanation

Hashnode is a free blogging platform built **for developers**. Code blocks render correctly. Markdown is first-class. Custom domains are free. The audience is other developers — which is your target.

Today: create an account, claim a subdomain, set up your profile so it looks like a real engineer's blog (not a side-project landing page).

---

## 💻 Hands-on — sign up and configure

### Step 1 — Create your account

1. Open https://hashnode.com
2. Sign up with the **same email** you use for GitHub (link them later — easier)
3. Verify email
4. **Pick a username carefully** — this becomes part of your URL forever-ish. Use your real name or a stable handle (e.g., `swapnildoye`).

### Step 2 — Create your personal blog

1. Click **+ Create Blog**
2. Blog name: something like *"Swapnil's Engineering Notes"* or your name. Avoid clever names — the title carries no weight; the posts do.
3. Subdomain: `<your-handle>.hashnode.dev` (you can map a custom domain later for free if you own one)
4. Pick a tagline like *"Building toward Forward-Deployed AI Engineer in 2026"*

### Step 3 — Profile basics (5 min)

- Add a clear headshot (selfie OK; not anime avatar)
- Bio (~150 chars): *"iOS engineer @ Walmart Global Tech. Studying AI Engineering full-time. Writing what I learn."*
- Link to your GitHub
- Link to your LinkedIn

### Step 4 — Settings to flip on Day 1

- **Settings → Newsletter:** Enable. This collects emails from readers — your future "interview reach" list.
- **Settings → Custom Domain:** Skip for now; revisit in Phase 2 if you want `yourname.dev`.
- **Settings → Integrations → GitHub:** Connect your GitHub. Hashnode can pull from a public repo (the "publish from markdown in git" workflow); useful but optional today.
- **Settings → Analytics:** Built-in works fine. Optional: connect Plausible later for sharper metrics.
- **Settings → SEO:** Add canonical URL pattern. Defaults are fine.

### Step 5 — Pick a clean theme

Hashnode has 3–4 free themes. Pick **"Edition" or "Hashnode Default"** — minimal, high readability, mobile-good. Don't tweak CSS today.

---

## 📊 What success looks like by end of this lesson

```
https://<your-handle>.hashnode.dev      →  loads, shows empty blog with your headshot + tagline
```

Save a screenshot of the landing page — you'll include it in your Sunday Reckoning.

---

## 🔧 Technical note — Hashnode's underlying model

Hashnode posts are **markdown files** with frontmatter:

```markdown
---
title: "Going from iOS to AI Engineer in 7 months"
subtitle: "Why I'm betting on Gemini + ADK"
slug: ios-to-ai-engineer-2026
publishedAt: "2026-05-23T08:00:00Z"
tags: ["ai", "career", "llm"]
canonical: https://<your-handle>.hashnode.dev/ios-to-ai-engineer-2026
---

# Body starts here...
```

That means you can **draft your post in VS Code** as a `.md` file and paste it in later. This is the recommended workflow — VS Code's preview pane is much better than Hashnode's editor for long posts.

I'll set up a `posts/` folder in your portfolio repo on Thursday for exactly this.

---

## 📚 References

- **Hashnode docs** — https://support.hashnode.com
- **Hashnode markdown reference** — https://support.hashnode.com/docs/editor
- **"Anatomy of a great dev blog"** — Hamel Husain — https://hamel.dev

---

## ✅ Exit criteria

- [ ] Hashnode account created
- [ ] Blog created at `<your-handle>.hashnode.dev`
- [ ] Headshot, bio, GitHub link, LinkedIn link all set
- [ ] Newsletter feature enabled
- [ ] Subdomain loads successfully
- [ ] Screenshot saved

**Next:** [`03-blog-structure-for-engineers.md`](03-blog-structure-for-engineers.md)

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
