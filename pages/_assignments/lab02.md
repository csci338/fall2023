---
layout: assignment-two-column
title: "Version Control and Branch Management with git and GitHub"
type: lab
draft: 0
points: 6
abbreviation: Lab 2
show_schedule: 2
num: 2
start_date: 2023-08-31
due_date: 2023-09-03
---

## 1. Lab Readings

### Required
* <a href="https://www.youtube.com/watch?v=_wQdY_5Tb5Q" target="_blank">Collaborating using Git and GitHub</a>: Branches, Pull Requests, Merging vs Rebasing (Video walkthrough)

### Recommended
* <a href="https://www.youtube.com/watch?v=_UZEXUrj-Ds" target="_blank">What is git rebase?</a>
* <a href="https://www.atlassian.com/git/tutorials/comparing-workflows" target="_blank">Article explaining how to rebase + handle merge conflicts</a>
<!-- 
## 2. Add your GitHub username to the spreadsheet
If you haven't already, please register for a GitHub account, and then add your full name and your GitHub username to <a href="https://docs.google.com/spreadsheets/d/1UYLm8ZoEivGhikw6pbh2CTGSh3lixfvceGENRD3z-No/edit?usp=sharing" target="_blank">this spreadsheet</a>. Semmy and I will invite you to be a contributor to the relevant repos.
* Note that **you will have to confirm this invitation** via email.

## 3. Setting up your copy of the coursework repository
In this class, we're going to have two repositories:
* **`class-exercises-fall2023`** -- For in-class exercises and labs.
* **`app`** -- for our class project

Before we get into the details of the GitHub workflow, let's set up a clone of **`class-exercises-fall2023`** on your laptop while practicing some basic git commands. Please complete the following tasks:

1. Within your `csci338` directory, clone this repo:
<a href="https://github.com/csci338/class-exercises-fall2023" target="_blank">https://github.com/csci338/class-exercises-fall2023</a>
1. Look at commit history (`git log`)
1. Create a folder with your GitHub username (e.g. `vanwars`) within the `class-exercises-fall2023` folder.
1. Within the `<your-username>` folder, create a text file called `README.md` (note the case). 
1. Within the `README.md` file, add the sentence “hello world!” (or anything, really). You can use vim, VS Code, or another text editor.
1. Issue the `git status` command. What happened?
1. Stage your changes using `git add .` (the dot indicates that you want to stage all of the files that have been added / deleted / edited).
1. Commit your changes using `git commit -am "adding my user directory"`.

## 4. Authentication Using Git / GitHub
While there are many ways of authenticating via GitHub, one of the most common ways of accessing other servers is by using public and private keys. The workflow is as follows:
1. Generate a public / private keys pair. 
    * We will be doing this on the command line using the **`ssh-keygen`** program.
    * the program will generate your private key inside the `.ssh` folder inside your home directory. Typically, the private key is  called `id_rsa` and the public key is called `id_rsa.pub`.

### Configure Public Key on Arden
1. Copy your public key onto the server.
    * Use a file copy program like scp: `scp ~/.ssh/id_rsa.pub svanwart@arden.cs.unca.edu/.`
1. Configure your public key:
    * If your home directory on the remote server doesn't already contain a `~/.ssh/authorized_keys` file, create oneas follows:
        * `mkdir -p ~/.ssh`<br>`touch ~/.ssh/authorized_keys`
    * Then, append your public key to the `authorized_keys` file: `cat ~/id_rsa.pub >> ~/.ssh/authorized_keys`

### Configure Public Key on GitHub
1. Follow the <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account" target="_blank">GitHub instructions</a>

Read More here: <a href="https://kb.iu.edu/d/aews" target="_blank">https://kb.iu.edu/d/aews</a>

## 5. Collaborative Work: Editing a Shared File



## 6. What to Turn In
You **do not** have to submit anything to the Moodle, but you **do** need to make sure that the following are completed before Sunday at midnight:

{:.checkbox-list}
* You have successfully committed and pushed your **username** directory and `README.md` file to the coursework repo (<a href="https://github.com/csci338/class-exercises-fall2023" target="_blank">https://github.com/csci338/class-exercises-fall2023</a>).
* You have successfully committed and pushed your `README.md` edits to the class project repo (<a href="https://github.com/csci338/app" target="_blank">https://github.com/csci338/app</a>). -->