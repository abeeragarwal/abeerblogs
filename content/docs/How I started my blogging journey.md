---
Title: How I started my blogging journey
date: 2025-08-03
draft: false
tags:
  - blog
  - tech-journey
  - obsidian
  - hugo
  - github
---
# The Hardest Step is the First step

>*“You don’t have to be great to start, but you have to start to be great.” — Zig Ziglar*

For the longest time, I hesitated to start a blog.

Not because I didn’t want to share—but because I thought I needed to be “ready.” Maybe after mastering Data Structures and Algorithms. Or after solving 500 problems on LeetCode. Or after building a perfect portfolio. But to be really honest, I realised that I could never find that perfect time to suffice my perfectionist personality. And, I do believe that this is one of my most important discoveries in life...

The fact that: **there is no perfect time to start**—except now. 

---

# What led me to start a blog

It all began when I realized I was learning so many new things every day - whether while debugging a piece of code, understanding a tricky DSA question, or setting up a personal project like this very blog. I felt a need to:

- Document what I **learn**
    
- Reflect on my **growth**
    
- **Help** others who are walking the same path

I have always been fond of teaching. As a human being, I feel that it is one of duties to help others of our own kind, and in this **selfish** world I believe **kindness** has slowly began starting to **vanish**. But, back to the topic, These points are primarily what drove me to start blogging. Regardless of who **judges** me, **criticises** me, I wish to build this space for the sake of it.

---

# The Twist — Why I Didn’t Choose the Easy Route

When I finally decided to start blogging, I didn’t want to go the conventional route—like WordPress, Medium, or some drag-and-drop editor.

I chose the harder path on purpose.

Instead of using pre-made platforms, I decided to build my blog using the very skills I’ve been learning—**coding**. I set it up with **Hugo**, a static site generator, and connected it to my **Obsidian notes** so I could write and publish directly from my personal vault. All hosted via **GitHub Pages**.

Sounds like a lot of effort? It was.  
But to me, it felt **right**.

Why? Because I didn't just want to write—I wanted the process of writing itself to reflect my identity as a **developer**.

Most people might wonder:

> *"Why complicate things when there are so many simpler options?"*

But I believe in building the kind of workflow that grows **with me**, not against me. I saw it as an investment—making things a bit harder now so they become **effortless** later.

And most importantly: it made the whole thing **mine**. My system. My process. My voice.

Yes, obsidian is a well known note taking platform. Yes, Hugo, is a well known static site builder. Yes, GitHub Pages is a well known platform for aspiring bloggers like me. But, the way to connect all of it, only a **handful** (LOL) hundred thousand people know about it. 

---

## Obsidian

### What is Obsidian?

**Obsidian** is a powerful, minimalist note-taking app that lets you write in **Markdown** and organize your notes in a local folder.

Unlike typical note apps, Obsidian works like a **personal knowledge base**—it lets you create internal links (`[[like this]]`), graph connections between ideas, and treat your notes like a second brain.

---

### Why I Use Obsidian for Blogging

For me, Obsidian isn’t just a place to jot thoughts—it’s where I:

- Write drafts in Markdown
    
- Link ideas across blog posts
    
- Organize my thoughts without distraction
    
- Sync with my Hugo blog setup for seamless publishing

It keeps everything **offline**, fast, **and** fully in my **control**.

Just like this blog that I was drafting Obsidian before posting it on this blog!

---

## Hugo

### What is Hugo?

**Hugo** is a fast, open-source static site generator written in Go. Instead of dynamically generating pages with a backend server, Hugo builds your entire website into plain HTML files that can be served anywhere—blazing fast and completely secure.

With Hugo, you write your content in Markdown, and it handles the layout, theme styling, navigation, and even SEO. It's highly customizable and used by developers who want **speed**, **control**, and **minimal dependencies**.

---

### Why I Use Hugo for building my site

Hugo is the core engine that transforms my plain-text notes into a structured, styled blog.

Here’s what it enables me to do:

- **Convert Markdown to beautiful HTML** with themes like PaperMod which I also used for this blog
    
- **Organize posts** using folders and front matter (metadata like title, date, tags)
    
- **Customize the layout** of pages exactly how I want them
    
- **Build the entire site instantly** with a single command (`hugo`)

It fits perfectly into my writing workflow with Obsidian, where all content is already in Markdown. I can edit locally, build locally, and preview everything before it goes live.

---

### Hugo + GitHub = Seamless Publishing

This is where the magic happens.

Hugo generates the final HTML files, and I use **GitHub Pages** to host them for free. All I do is push the generated `public/` folder (or let a GitHub Action do it automatically), and my blog is updated instantly.

In other words:

- **Obsidian** → where I write
    
- **Hugo** → where I build
    
- **GitHub Pages** → where I publish

It’s like a pipeline:

`Markdown` → `Hugo` → `HTML` → `GitHub Pages` → **Live blog**

This setup gives me full control over everything—from how my blog looks, to when and how it’s updated. No ads, no paywalls, no platform rules. Just code and content.

---

## Connecting to GitHub Pages

Once Hugo generates the final version of my site (plain HTML, CSS, and JS files), I need a way to **put it online**. That’s where **GitHub Pages** comes in.

### What is GitHub Pages?

**GitHub Pages** is a free hosting service provided by GitHub that lets you deploy static websites directly from a GitHub repository. No servers, no hosting fees—just push your files, and your site is live.

### How I Use GitHub Pages

Here’s how the process works for my blog:

1. **I write posts** in Obsidian (Markdown files).
    
2. **Hugo builds** them into a full website.
    
3. I **push the generated site** (from the `public/` folder) to a GitHub repository.
    
4. GitHub Pages **serves the site automatically** to the world.

### Bonus: Automating the Deploy

To make things even easier, I’ve connected my main content repo to a **GitHub Action**—a small script that runs whenever I push changes.

So instead of manually running `hugo` and copying files, I just:

- Write 
	
- Commit 
	
- Push 
	
- Blog is live

### Why This Matters to Me

This setup:

- Keeps my workflow **entirely developer-friendly**
    
- Allows me to **version control** my writing like I would with code
    
- Gives me **complete control** over hosting, themes, and design
    
- Costs me **nothing** to run

In a world full of no-code tools, I chose to build my own workflow—not because it was easy, but because it was **me**.

---

# Final Thoughts

Starting this blog wasn’t just about publishing posts—it was about **taking ownership** of my learning journey. From writing in Obsidian, building with Hugo, hosting on GitHub Pages, to automating everything with scripts—I’ve created a system that reflects not just what I do, but **who I am** as a developer.

It’s not perfect. It’s not flashy. But it’s **mine**.

If there’s one thing I’ve learned through all of this, it’s that the hardest step is always the first. But once you take it, the path ahead doesn’t feel as scary anymore.

So if you’ve been waiting for the _perfect_ moment to start your own blog, project, or passion—this is your sign:  
**Start now. Build messy. Learn fast. Refine later.**

Your voice matters. And someone out there is waiting to hear it.