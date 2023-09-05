---
layout: two-column
title: Git & GitHub
parent: resources
type: resource
category: "Version Control"
---


## Useful Online Resources

* <a href="https://git-scm.com/book/en/v2" target="_blank">Pro Git Book</a>. Great reference
* <a href="https://www.youtube.com/watch?v=_wQdY_5Tb5Q" target="_blank">Collaborating using Git and GitHub</a>: Branches, Pull Requests, Merging vs Rebasing (Video walkthrough)
* <a href="https://www.youtube.com/watch?v=_UZEXUrj-Ds" target="_blank">What is git rebase?</a>
* <a href="https://www.atlassian.com/git/tutorials/comparing-workflows" target="_blank">Article explaining how to rebase + handle merge conflicts</a>

## Git Cheatsheet
### Basic Commands

| **git clone** | Copies a remote repository (e.g., one hosted on a GitHub server) onto your local machine (within your current directory). |
| **git status** | Tells you which of the files in your current directory are different from the latest commit in the repo. |
| **git add** | Stages the specified files to be committed |
| **git log** | Shows you the commit history |
| **git commit** | Saves a snapshot of your staged files at the moment the commit is issued. Each commit represents the state of your code at a particular moment in time. |
| **git push** | Uploads your commits to a remote repo |
| **git pull** | Downloads changes from a remote repo to your local repo |

### Branch Commands 

|  **git checkout -b my-new-branch** | Creates a new branch |
| **git branch** | Tells you which branch you’re on |
| **git checkout main** | Switches you from your current branch to the main branch |
| **git checkout my-new-branch** | Switches you from your current branch to the my-new-branch branch |
| **git branch -d my-new-branch** | Deletes my-new-branch from your local repo |
| **git merge my-new-branch** | Merges changes from my-new-branch into the current branch. |
| **git rebase my-new-branch** | Rebases changes from my-new-branch into the current branch. |
