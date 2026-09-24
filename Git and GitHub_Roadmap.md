# Git & GitHub Roadmap

> A practical Beginner → Intermediate roadmap for learning Git and GitHub through understanding, practice, real workflows, and projects.
>
> **Core principle:** Do not learn Git as a list of commands. Understand the model, then use Git continuously while building software.

---

# Table of Contents

1. [How to Use This Roadmap](#1-how-to-use-this-roadmap)
2. [Git vs GitHub](#2-git-vs-github)
3. [The Core Mental Model](#3-the-core-mental-model)
4. [Phase 1 — Git Foundations](#4-phase-1--git-foundations)
5. [Phase 2 — Commits and History](#5-phase-2--commits-and-history)
6. [Phase 3 — GitHub and Remote Repositories](#6-phase-3--github-and-remote-repositories)
7. [Phase 4 — Branching and Merging](#7-phase-4--branching-and-merging)
8. [Phase 5 — Undoing, Recovering, and Inspecting](#8-phase-5--undoing-recovering-and-inspecting)
9. [Phase 6 — GitHub Collaboration](#9-phase-6--github-collaboration)
10. [Phase 7 — Professional Git Habits](#10-phase-7--professional-git-habits)
11. [Everyday Workflows](#11-everyday-workflows)
12. [Python Project Workflow](#12-python-project-workflow)
13. [Common Problems and How to Think About Them](#13-common-problems-and-how-to-think-about-them)
14. [Command Reference](#14-command-reference)
15. [Project Ladder](#15-project-ladder)
16. [Mastery System](#16-mastery-system)
17. [Completion Checklist](#17-completion-checklist)
18. [What to Learn Later](#18-what-to-learn-later)

---

# 1. How to Use This Roadmap

The learning cycle is:

```text
Concept
   ↓
Small practice
   ↓
Problem solving
   ↓
Real workflow
   ↓
Project
   ↓
Reflection
   ↓
Next concept
```

Do not wait until you know Git completely before using it.

Instead:

```text
Learn enough
    ↓
Use Git
    ↓
Encounter a problem
    ↓
Understand the problem
    ↓
Learn the required command/concept
    ↓
Continue
```

## What "good enough" means

You do not need to memorize every Git command.

You should be able to:

- Understand where your changes currently exist.
- Create meaningful commits.
- Read project history.
- Work with branches.
- Push and pull from GitHub.
- Clone repositories.
- Resolve basic merge conflicts.
- Undo common mistakes safely.
- Use `.gitignore`.
- Work with Pull Requests.
- Recover from ordinary mistakes without panic.
- Learn unfamiliar Git operations from documentation.

---

# 2. Git vs GitHub

## Git

**Git** is a distributed version control system.

It runs locally on your computer and records the history of your project through commits.

Git lets you:

- Track changes.
- Create versions.
- Compare versions.
- Create branches.
- Merge work.
- Restore or reverse changes.
- Work offline.

## GitHub

**GitHub** is an online platform for hosting Git repositories and collaborating around them.

GitHub adds things such as:

- Remote repositories.
- Pull Requests.
- Issues.
- Code review.
- Discussions.
- Project management features.
- Collaboration.

```text
Git
= version control

GitHub
= online platform built around Git
```

Git does **not** require GitHub.

You can use Git entirely locally.

---

# 3. The Core Mental Model

This is the most important part of the entire roadmap.

## The three local areas

### 1. Working Directory

The actual files you are currently editing.

### 2. Staging Area

The changes you have selected for the next commit.

### 3. Local Repository

Git's local database containing committed project history.

The basic flow is:

```text
Working Directory
       │
    git add
       ↓
Staging Area
       │
   git commit
       ↓
Local Repository
       │
    git push
       ↓
GitHub / Remote Repository
```

When receiving remote work:

```text
GitHub / Remote
       │
   git fetch
       ↓
Local Git Repository

git pull
= fetch + integrate
```

## The simplest mental model

Think:

```text
I changed something
      ↓
I selected what I want to record
      ↓
I recorded it
      ↓
I sent that record to GitHub
```

Corresponding commands:

```text
change
  ↓
git add
  ↓
git commit
  ↓
git push
```

## Why the staging area exists

It lets you decide exactly what belongs in the next commit.

Suppose you changed:

```text
calculator.py
README.md
notes.txt
```

You might want the commit to contain only:

```text
calculator.py
```

So:

```bash
git add calculator.py
git commit -m "Fix calculator input handling"
```

The other changes can remain uncommitted.

---

# 4. Phase 1 — Git Foundations

## Goal

Understand what version control is and become comfortable with the basic local Git workflow.

## 4.1 Why Version Control Matters

Without version control:

```text
project-final.py
project-final-2.py
project-final-real.py
project-final-real-new.py
project-final-real-new-2.py
```

With Git:

```text
A → B → C → D
```

Each commit represents a meaningful point in the project's history.

Git gives you a history rather than a pile of manually renamed files.

---

## 4.2 Install and Configure Git

Verify installation:

```bash
git --version
```

Configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

View configuration:

```bash
git config --list
```

---

## 4.3 Initialize a Repository

Inside an existing project:

```bash
git init
```

Git creates a hidden `.git` directory.

```text
project/
├── main.py
├── README.md
└── .git/
```

`.git` contains the repository's internal data.

> Do not manually modify `.git` unless you understand exactly what you are doing.

---

## 4.4 Check Repository State

```bash
git status
```

This is one of your most important commands.

Use it constantly.

It tells you things such as:

- Current branch.
- Untracked files.
- Modified files.
- Staged changes.
- Whether the working tree is clean.

### Habit

When confused:

```bash
git status
```

Do not guess what Git thinks is happening.

---

## 4.5 Track Changes

Stage one file:

```bash
git add main.py
```

Stage several files:

```bash
git add main.py README.md
```

Stage changes in the current directory:

```bash
git add .
```

Understand:

```text
Working Directory
       ↓
    git add
       ↓
Staging Area
```

`git add` does not create a commit.

---

## 4.6 Create a Commit

```bash
git commit -m "Add calculator program"
```

A commit records the currently staged changes.

Important:

```text
Modified ≠ committed
Staged ≠ committed
Committed = recorded in Git history
```

---

## 4.7 Write Useful Commit Messages

Prefer:

```text
Add calculator input validation
Fix division by zero handling
Add README
Create expense tracker CLI
```

Avoid vague messages:

```text
update
changes
stuff
final
asdf
```

A commit message should tell you what changed.

---

## 4.8 First Practice

Create a tiny project:

```text
git-practice/
└── hello.txt
```

Then practice:

```bash
git init
git status
git add hello.txt
git commit -m "Add hello file"
git status
```

Then modify the file and repeat the workflow.

---

# 5. Phase 2 — Commits and History

## Goal

Understand Git history instead of treating commits as mysterious save points.

---

## 5.1 View History

```bash
git log
```

Compact form:

```bash
git log --oneline
```

Example:

```text
8a31f2c Add input validation
1bc91d0 Add calculator
4f2a7c1 Initial commit
```

The short strings identify commits.

---

## 5.2 View Changes

Unstaged changes:

```bash
git diff
```

Staged changes:

```bash
git diff --staged
```

Mental model:

```text
git diff
→ What changed in Working Directory compared with Staging Area?

git diff --staged
→ What is staged compared with the last commit?
```

---

## 5.3 The Commit Graph

Imagine:

```text
A ─── B ─── C
```

Each letter is a commit.

Your project is not simply "the latest file."

It is a history of states.

---

## 5.4 Commit Quality

Good commits are:

- Small enough to understand.
- Related to one logical change.
- Descriptive.
- Frequent enough to create useful history.

Bad pattern:

```text
Work for 4 days
      ↓
One enormous commit
```

Better:

```text
Add project structure
      ↓
Add input validation
      ↓
Add file storage
      ↓
Fix loading bug
      ↓
Update documentation
```

---

# 6. Phase 3 — GitHub and Remote Repositories

## Goal

Understand how local Git repositories communicate with repositories hosted on GitHub.

---

## 6.1 Remote Repository

A remote is another copy/location of the repository.

Commonly:

```text
Local Git repository
        ↕
      GitHub
```

The conventional remote name is:

```text
origin
```

Check remotes:

```bash
git remote -v
```

---

## 6.2 Create a GitHub Repository

Typical process:

1. Create a repository on GitHub.
2. Connect your local repository to it.
3. Push your commits.

Connect:

```bash
git remote add origin <repository-url>
```

Verify:

```bash
git remote -v
```

---

## 6.3 Push

Push local commits to GitHub:

```bash
git push
```

For a first push:

```bash
git push -u origin main
```

The exact branch name may be `main` or another branch.

`-u` establishes an upstream/tracking relationship.

After that, future pushes can usually be:

```bash
git push
```

---

## 6.4 Clone

If a repository already exists:

```bash
git clone <repository-url>
```

Cloning normally:

- Downloads the project.
- Downloads its Git history.
- Creates a local repository.
- Configures the remote, usually as `origin`.

Compare:

```text
git init
→ Turn an existing local project into a Git repository.

git clone
→ Get an existing Git repository locally.
```

---

## 6.5 Pull

```bash
git pull
```

Conceptually:

```text
git pull
≈
git fetch + integrate
```

Use it when you want your current branch updated with changes from its remote tracking branch.

---

## 6.6 Fetch

```bash
git fetch
```

Fetch downloads information from the remote without automatically integrating it into your current branch.

Think:

```text
fetch
→ "Tell me what changed."

pull
→ "Get the changes and integrate them."
```

---

## 6.7 GitHub README

A `README.md` explains your project.

A useful README can contain:

```markdown
# Project Name

Short description.

## Features

- Feature 1
- Feature 2

## Installation

Instructions.

## Usage

Example commands.

## Project Structure

Explanation.

## Future Improvements

Possible next steps.
```

The README is part of your project's communication, not just decoration.

---

## 6.8 `.gitignore`

Create:

```text
.gitignore
```

Example Python project:

```text
__pycache__/
*.pyc
.venv/
.env
```

Use it for files that should not normally be tracked, such as:

- Generated files.
- Cache files.
- Virtual environments.
- Local configuration.
- Secrets.

Important:

> `.gitignore` does not automatically untrack a file that Git is already tracking.

Never commit passwords, API keys, tokens, or other secrets.

---

# 7. Phase 4 — Branching and Merging

## Goal

Learn how to work on changes separately without disturbing the main line of development.

---

## 7.1 What Is a Branch?

A branch is a separate line of development.

Imagine:

```text
A ─── B ─── C       main
           \
            D ─── E feature
```

`main` and `feature` now represent different development lines.

---

## 7.2 Create a Branch

List branches:

```bash
git branch
```

Create:

```bash
git branch feature
```

Create and switch:

```bash
git switch -c feature
```

Switch:

```bash
git switch feature
```

Switch back:

```bash
git switch main
```

---

## 7.3 When Should You Use a Branch?

Use a branch when you want isolated work such as:

- A new feature.
- An experiment.
- A bug fix.
- A refactor.
- Work that may take several commits.

Do not create branches merely because you think "professional Git users must create lots of branches."

Use them when they solve a real problem.

---

## 7.4 Merge

Suppose:

```text
main
  ↓
A ─── B

feature
      \
       C ─── D
```

To merge the feature into `main`:

```bash
git switch main
git merge feature
```

The branch you are currently on is the branch receiving the merge.

---

## 7.5 Fast-Forward Merge

If `main` has not moved since the feature branch was created, Git may simply move the branch pointer forward.

```text
Before:

main    → A
feature → B

After:

main    → B
feature → B
```

This is a fast-forward merge.

---

## 7.6 Merge Conflicts

A conflict happens when Git cannot safely combine competing changes.

Example:

```text
main:
print("Hello")

feature:
print("Hi")
```

If both branches changed the same part differently, Git may mark the conflict:

```text
<<<<<<< HEAD
print("Hello")
=======
print("Hi")
>>>>>>> feature
```

Your job is to decide what the final code should be.

Then:

```bash
git add <file>
git commit
```

General workflow:

```text
git merge feature
       ↓
Conflict
       ↓
Read the conflicting file
       ↓
Understand both changes
       ↓
Choose/fix the final version
       ↓
Remove conflict markers
       ↓
git add <file>
       ↓
git commit
```

A conflict is not necessarily a failure. It means Git needs a human decision.

---

# 8. Phase 5 — Undoing, Recovering, and Inspecting

## Goal

Understand common mistakes and recover safely.

The most important rule:

> Before undoing something, identify where the change currently exists.

Ask:

```text
Is it:
- unstaged?
- staged?
- committed?
- pushed?
```

---

## 8.1 Discard Unstaged Changes

```bash
git restore <file>
```

This can discard uncommitted changes to that file.

Use carefully.

---

## 8.2 Unstage a File

```bash
git restore --staged <file>
```

This removes the file from the staging area while keeping your working changes.

```text
Staged
  ↓
git restore --staged
  ↓
Unstaged
```

---

## 8.3 Revert a Commit

For a committed change you want to reverse:

```bash
git revert <commit-id>
```

This creates a new commit that reverses the selected commit.

Example:

```text
A → B → C
          ↓
       revert C
          ↓
A → B → C → D
```

`D` reverses the effect of `C`.

This is generally a safer approach for changes that have already been shared.

---

## 8.4 HEAD

`HEAD` represents your current position in Git.

Usually:

```text
HEAD
 ↓
main
 ↓
latest commit
```

On another branch:

```text
HEAD
 ↓
feature
 ↓
latest feature commit
```

---

## 8.5 Detached HEAD

You can inspect a specific commit:

```bash
git switch --detach <commit-id>
```

Now `HEAD` points directly to a commit rather than a branch.

This is useful for inspecting or testing historical states.

Return to a branch:

```bash
git switch main
```

Do not casually make important work in detached HEAD unless you understand how to preserve it.

---

## 8.6 `git checkout`

`git checkout` is an older multi-purpose command.

Modern clearer commands are:

```text
git switch
→ branch operations

git restore
→ file restoration
```

You should understand `checkout` because you will encounter it in older tutorials and repositories.

---

# 9. Phase 6 — GitHub Collaboration

## Goal

Understand how Git and GitHub work together in collaborative software development.

---

## 9.1 Pull Requests

A Pull Request (PR) is a GitHub collaboration feature for proposing changes from one branch into another.

Typical workflow:

```text
Create feature branch
        ↓
Make commits
        ↓
Push branch
        ↓
Open Pull Request
        ↓
Review / discussion
        ↓
Changes if needed
        ↓
Merge
        ↓
main
```

A Pull Request is a **GitHub feature**, not a Git command.

---

## 9.2 Issues

GitHub Issues can track:

- Bugs.
- Features.
- Tasks.
- Questions.
- Improvements.

Example:

```text
Issue #12
"Calculator crashes when input is empty."
```

You can then create a branch to work on the issue.

---

## 9.3 Forks

A fork is a GitHub-side copy of another repository under your own account.

A common open-source workflow is:

```text
Original repository
        ↓
      Fork
        ↓
Clone locally
        ↓
Create branch
        ↓
Make changes
        ↓
Push
        ↓
Pull Request to original repository
```

You do not need forks for your own normal projects.

---

## 9.4 Basic Collaboration Workflow

A simplified team workflow:

```text
main
 │
 ├── feature/login
 │
 ├── feature/search
 │
 └── fix/input-error
```

Each branch can be developed independently.

Then:

```text
branch
  ↓
push
  ↓
Pull Request
  ↓
review
  ↓
merge
  ↓
main
```

---

# 10. Phase 7 — Professional Git Habits

## Goal

Use Git as a development tool rather than as a command checklist.

---

## 10.1 Commit Frequently, but Meaningfully

Commit after a logical unit of work.

For example:

```text
Add command-line interface
Add input validation
Add JSON persistence
Fix loading error
Update README
```

Not:

```text
commit every five seconds
```

and not:

```text
one commit after three weeks
```

---

## 10.2 Keep Commits Understandable

A good commit answers:

> What changed?

A good history should allow another developer—or your future self—to understand the project's evolution.

---

## 10.3 Inspect Before You Act

When something seems wrong:

```bash
git status
git log --oneline
git diff
git branch
git remote -v
```

Then decide what to do.

Do not blindly run random commands from a tutorial.

---

## 10.4 Do Not Commit Secrets

Never put credentials directly into Git.

Bad:

```python
API_KEY = "real-secret-key"
```

Prefer environment variables or an appropriate secret-management approach.

Use `.gitignore` for local secret files such as:

```text
.env
```

But remember:

> Ignoring a secret before it is committed is good. Adding it to `.gitignore` after it has already been committed does not erase it from Git history.

If a real secret is exposed, treat it as compromised and rotate/revoke it.

---

## 10.5 Git Is Not a Backup Replacement

Git helps preserve project history, but Git alone is not automatically a complete backup strategy.

A remote repository provides another copy, but important projects should still be treated with proper backup practices.

---

# 11. Everyday Workflows

## Workflow A — New Local Project

```bash
mkdir my-project
cd my-project

git init

# Create files...

git status
git add .
git commit -m "Initial commit"
```

---

## Workflow B — Connect to GitHub

```bash
git remote add origin <repository-url>
git push -u origin main
```

Then:

```bash
git push
```

for later pushes.

---

## Workflow C — Normal Development

```text
Edit
 ↓
git status
 ↓
git diff
 ↓
git add
 ↓
git diff --staged
 ↓
git commit
 ↓
git push
```

You do not have to run every command every time, but understand what each step is doing.

---

## Workflow D — Clone an Existing Project

```bash
git clone <repository-url>
cd project
```

Then:

```bash
git status
```

---

## Workflow E — Feature Branch

```bash
git switch -c feature-name

# Work...

git status
git add .
git commit -m "Add feature"
git push -u origin feature-name
```

Then create a Pull Request on GitHub when appropriate.

---

## Workflow F — Update Your Local Work

```bash
git pull
```

For more deliberate control:

```bash
git fetch
```

Then inspect the incoming changes before deciding how to integrate them.

---

## Workflow G — Basic Conflict Resolution

```text
Pull/Merge
   ↓
Conflict
   ↓
git status
   ↓
Open conflicting files
   ↓
Understand both versions
   ↓
Edit final version
   ↓
git add <file>
   ↓
Complete merge
```

---

# 12. Python Project Workflow

Since Git is most useful when attached to real projects, use it continuously with Python.

Example:

```text
calculator/
├── main.py
├── README.md
├── .gitignore
└── tests/
```

Initial setup:

```bash
git init
git add .
git commit -m "Create calculator project"
```

Then development:

```text
Build feature
    ↓
Test
    ↓
Fix problems
    ↓
Commit meaningful change
    ↓
Continue
```

Example history:

```text
Create calculator project
Add arithmetic operations
Add input validation
Handle division by zero
Add tests
Improve README
```

This makes Git part of development rather than a separate subject.

---

# 13. Common Problems and How to Think About Them

## Problem 1 — "I changed a file but Git doesn't show what I expected."

Start with:

```bash
git status
```

Then:

```bash
git diff
git diff --staged
```

Ask:

```text
Where is my change?
Working Directory?
Staging Area?
Commit?
```

---

## Problem 2 — "I committed the wrong thing."

Do not immediately run an unfamiliar destructive command.

First determine:

- What was committed?
- Has it been pushed?
- Do you need to preserve the history?
- Is the problem the content, the commit message, or both?

For shared history, `git revert` is often relevant.

---

## Problem 3 — "My branch is behind GitHub."

First inspect:

```bash
git status
git fetch
```

Then understand the relationship between your local branch and the remote branch before integrating changes.

---

## Problem 4 — "I got a merge conflict."

Do not panic.

Git is telling you:

> "I found two changes that I cannot safely combine automatically."

Read the conflict.

Understand both sides.

Choose the correct final state.

Then stage the resolved file and complete the merge.

---

## Problem 5 — "I forgot a command."

That is normal.

Use:

```bash
git help <command>
```

Examples:

```bash
git help commit
git help branch
git help merge
```

You can also use:

```bash
git <command> --help
```

The goal is not perfect command memorization.

The goal is knowing what you are trying to accomplish and how to find the correct Git operation.

---

# 14. Command Reference

| Command | Purpose |
|---|---|
| `git --version` | Check Git version |
| `git config` | Configure Git |
| `git init` | Initialize repository |
| `git clone <url>` | Clone repository |
| `git status` | Show repository state |
| `git add <file>` | Stage a file |
| `git add .` | Stage changes in current directory |
| `git commit -m "..."` | Create commit |
| `git log` | View history |
| `git log --oneline` | Compact history |
| `git diff` | View unstaged changes |
| `git diff --staged` | View staged changes |
| `git remote -v` | Show remotes |
| `git remote add origin <url>` | Add remote |
| `git push` | Push commits |
| `git pull` | Fetch and integrate remote changes |
| `git fetch` | Fetch remote information |
| `git branch` | List branches |
| `git branch <name>` | Create branch |
| `git switch <name>` | Switch branch |
| `git switch -c <name>` | Create and switch branch |
| `git merge <branch>` | Merge branch |
| `git restore <file>` | Discard unstaged file changes |
| `git restore --staged <file>` | Unstage file |
| `git revert <commit>` | Reverse a commit with a new commit |
| `git switch --detach <commit>` | Inspect a specific commit |
| `git checkout ...` | Older multi-purpose command |
| `git help <command>` | Read Git documentation |

---

# 15. Project Ladder

Do not only practice commands in isolation.

Build projects around them.

## Level 1 — Git Basics

Create:

```text
git-practice/
└── notes.txt
```

Practice:

- `git init`
- `git status`
- `git add`
- `git commit`
- `git log`
- `git diff`

### Goal

Understand:

```text
Working Directory
→ Staging Area
→ Commit
```

---

## Level 2 — GitHub Project

Take a small Python project.

Practice:

- Create repository.
- Create `.gitignore`.
- Write README.
- Commit changes.
- Connect GitHub.
- Push.
- Clone it into another directory.
- Make changes.
- Push and pull.

### Goal

Understand:

```text
Local ↔ GitHub
```

---

## Level 3 — Branching Project

Take an existing project.

Create:

```text
main
feature-a
feature-b
```

Practice:

- Create branches.
- Switch branches.
- Make different changes.
- Merge branches.
- Create a deliberate simple conflict.
- Resolve it.

### Goal

Understand parallel development.

---

## Level 4 — GitHub Collaboration Simulation

Use your own repository to simulate a team workflow.

Practice:

```text
Issue
 ↓
Feature branch
 ↓
Commits
 ↓
Push
 ↓
Pull Request
 ↓
Review
 ↓
Merge
```

### Goal

Understand the workflow, not merely the buttons.

---

## Level 5 — Real Python Project

Use Git from the first day of a real project.

Example:

```text
Project
 ↓
Repository
 ↓
README
 ↓
.gitignore
 ↓
Small commits
 ↓
Branches when useful
 ↓
GitHub
 ↓
Pull Request when appropriate
```

### Goal

Make Git a natural part of software development.

---

# 16. Mastery System

Do not ask:

> "Have I finished Git?"

Ask:

> "Can I use Git to solve normal development problems?"

## Concept Mastery

For each major concept, you should be able to:

- Explain it in your own words.
- Explain why it exists.
- Predict what a command will do.
- Recognize when it is useful.
- Distinguish it from related concepts.

For example:

```text
git fetch vs git pull
git add vs git commit
git restore vs git revert
git init vs git clone
Git vs GitHub
```

---

## Workflow Mastery

You should be able to perform without step-by-step guidance:

```text
Create repository
    ↓
Make changes
    ↓
Stage
    ↓
Commit
    ↓
Connect remote
    ↓
Push
```

And:

```text
Clone
    ↓
Create branch
    ↓
Make changes
    ↓
Commit
    ↓
Push branch
    ↓
Pull Request
    ↓
Merge
```

---

## Problem-Solving Mastery

When something goes wrong, your first reaction should be investigation rather than random commands.

Use:

```bash
git status
git diff
git log --oneline
git branch
git remote -v
```

Then reason about the state.

---

# 17. Completion Checklist

You are ready to move beyond the fundamentals when you can:

## Git Fundamentals

- [ ] Explain what Git is.
- [ ] Explain what GitHub is.
- [ ] Explain why Git exists.
- [ ] Explain repositories.
- [ ] Explain Working Directory.
- [ ] Explain Staging Area.
- [ ] Explain commits.
- [ ] Initialize a repository.
- [ ] Check repository status.
- [ ] Stage changes.
- [ ] Create commits.
- [ ] Read commit history.
- [ ] Inspect changes.

## Remote Work

- [ ] Explain remote repositories.
- [ ] Add a GitHub remote.
- [ ] Push changes.
- [ ] Pull changes.
- [ ] Fetch changes.
- [ ] Clone a repository.
- [ ] Understand `origin`.
- [ ] Create and use `.gitignore`.
- [ ] Write a useful README.

## Branching

- [ ] Explain branches.
- [ ] Create branches.
- [ ] Switch branches.
- [ ] Merge branches.
- [ ] Understand fast-forward merges.
- [ ] Understand basic merge conflicts.
- [ ] Resolve a simple conflict.

## Recovery

- [ ] Unstage a file.
- [ ] Discard an unstaged change when appropriate.
- [ ] Explain `git revert`.
- [ ] Understand HEAD.
- [ ] Understand detached HEAD.
- [ ] Know when to stop and inspect before running commands.

## GitHub

- [ ] Understand Pull Requests.
- [ ] Understand Issues.
- [ ] Understand forks conceptually.
- [ ] Understand a basic collaborative workflow.

## Practical Mastery

- [ ] Use Git on a real Python project.
- [ ] Make meaningful commits.
- [ ] Use branches when they provide value.
- [ ] Push projects to GitHub.
- [ ] Resolve a basic merge conflict.
- [ ] Recover from common mistakes.
- [ ] Read Git documentation when you forget something.

---

# 18. What to Learn Later

You do **not** need all advanced Git topics immediately.

Learn them when your projects require them.

Possible later topics:

- Interactive rebase.
- `git rebase`.
- Cherry-pick.
- Stash.
- Tags.
- Bisect.
- Reflog.
- Submodules.
- Worktrees.
- Advanced merge strategies.
- Signing commits.
- Git hooks.
- GitHub Actions.
- Release workflows.
- Advanced branching strategies.
- Large repository optimization.

These are useful, but they should not become another information-collection project.

---

# Final Mental Model

Remember this:

```text
                 YOUR PROJECT
                      │
               Working Directory
                      │
                   git add
                      ↓
                Staging Area
                      │
                 git commit
                      ↓
               Local Repository
                      │
                  git push
                      ↓
                    GitHub
                      │
                 git fetch
                      ↓
              Remote Information
                      │
                  git pull
                      ↓
                Local Branch
```

And for parallel work:

```text
                  main
                   │
              A ─── B
                    \
                     C ─── D
                          feature
                              │
                           Pull Request
                              │
                            review
                              │
                            merge
                              ↓
                            main
```

The goal is not:

> Know every Git command.

The goal is:

> Understand project history, control your changes, collaborate safely, and use Git confidently while building software.

---

# Recommended Learning Loop

```text
Learn one concept
      ↓
Use the command
      ↓
Observe what changed
      ↓
Explain the result
      ↓
Break something safely
      ↓
Recover it
      ↓
Use it in a real project
      ↓
Move on
```

**Git becomes easy when the mental model becomes clear.**
