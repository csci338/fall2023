---
layout: two-column
title: Publish your first web page using GitHub
type: activity
abbreviation: Activity 2
draft: 1
num: 2
---

<!-- 
TODO for next time:
git config --global user.name "Sarah"
git config --global user.email "my_email@gmail.com"

On Mac, people had to install XCode Tools
-->
<style>
    img {
        max-width: 750px;
        width: 60%;
        border: solid 1px #000;
    }
    img.large {
        max-width: 100%;
        width: 100%;
        border: solid 1px #000;
    }
    .schematic {
        border: none;
        max-width: 850px;
        width: 70%;
        display: block;
        margin: auto;
    }
    table.instructions td, table.instructions th {
        font-size: 1.0em;
    }
    table.instructions td:first-child {
        white-space: nowrap;
    }
    ul.spaced li, ol.spaced li {
        margin-bottom: 25px;
    }

</style>


{:.blockquote-no-margin}
> ## Activity Overview.
> Today, you will be publishing the web page you made in tutorial02 to GitHub. To do this, please complete the following:
>
> 1. [Complete the Background Readings](#part1)
> 1. [Install git](#part2)
> 1. [Register for GitHub](#part3)
> 1. [Configure the Git / Visual Studio Code Plugin](#part4)
> 1. [Configure Git Pages](#part5)


{:#part1}
## 1. Background Readings
Please complete the following readings / videos:
1. [Intro to git and GitHub](https://medium.com/the-underdog-writing-project/introduction-to-git-and-github-a5fdf5633923). A little technical, but please do your best to read it and come to class with questions.
2. [Using GitHub with Visual Studio Code](https://youtu.be/i_23KUAEtUM). How we will be using GitHub in this class.

{:#part2}
## 2. Install Git
In order to interact with GitHub, you need to install git. Before you install it, check and make sure it’s not already installed by:

1. Windows: search for the software program "GitBash." If you find it, git is already installed. 
2. Mac:
    1. Opening your Terminal and type the word `git` at the command prompt. 
    2. If you get a message that says "not recognized" or something along those lines, then you need to install it.

If you need to install it, follow these instructions:   <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git" target="_blank">https://git-scm.com/book/en/v2/Getting-Started-Installing-Git</a>.

{:#part3}
## 3. Register for an account on GitHub
If you don’t already have a GitHub account, register for one: <a href="https://github.com/" target="_blank">https://github.com/join</a>. Some notes:

1. Please have your password close at hand. Particularly if you are using the computer lab computers, you will keep being prompted for your password.
2. Mac users may also need to create a **"Personal Access Token"**. The process is described <a href="https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token" target="_blank">here</a>.


{:#part4}
## 4. Configure the Git / Visual Studio Code Plugin

### 1. Tell the system who you are 
Tell your computer who you are on Git by running the following commands in GitBash (Windows) or in the Terminal (Mac):

```bash
git config --global user.name "Sarah"
git config --global user.email "my_email@gmail.com"
```

Please use **your name**, and the **email you used when registering with GitHub**.

> #### Note for Computer Lab Computers
> If you are using a computer lab computer, you will need to complete this step each time you use git.

### 2. Verify your file structure

Please ensure that your `csci185` folder looks like this:

```shell
csci185
├── lectures
│   └── lecture02
│       ├── images
│       ├── index.html
│       └── styles.css
└── tutorials
    └── tutorial01
        ├── images
        ├── index.html
        ├── music.html
        ├── style.css
        └── videos.html
```

It's OK if your lectures folder isn't set up yet, but make sure your tutorials folder looks like the one shown above. This is very important. Ask Sarah if you're unsure whether your folder nesting is correct (`tutorial02` should be contained within `tutorials` which should contained within `csci185`).

### 3. Initialize a Git Repository
After you've doublechecked your file structure, open your entire `csci185` folder in VS Code. Your file list should look like this (click on the icon that looks like two pieces of paper in the upper left-hand corner of your screen):

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss1.png" />

Next, click on the icon that looks like a tree branch, and click the blue button that says "Initialize Repository":

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss2.png" />

You have now created a git repository on your computer in the same folder as your `csci185` folder. Now, you will want to "stage" all of your changes. Click the button with the three dots, then select "Changes", and then "Stage All changes":

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss3.png" />

After you "stage" your changes, you will note that the left-hand panel has changed. Specifically:

{:.compact}
* The panel lists all of the files that are "staged" to be committed, with an "A" next to each file (indicating that you are adding the files for the first time). 
* To commit these changes, type a message in the text box that says "My First Commit" and then click the check button to actually issue the commit:

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss4.png" />

Afterwards, a button will appear that says "Publish Branch." Click this button. It may prompt you to install a GitHub plugin. Please agree that you are OK to install the GitHub plugin.

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss5.png" />

You will now create a new GitHub repository called `csci185-coursework`. Please ensure that you create a PUBLIC repository:

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss6.png" />

After VS code issues the "create repository" request to GitHub, it will give you a message indicating that your files are being sent up to GitHub. When the file transfer is complete, you will see a blue button that says "Open On GitHub". Click that button. 

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss7.png" />

Clicking the button will open your newly created `csci185-coursework` repository and show you all of your files (which are now in the cloud):

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss8.png" />




{:#part5}
## 5. Finally, Configure GitHub Pages
GitHub also allows you to host pages. To enable GitHub pages:

{:.compact}
1. Go to your repository and click on the settings tab. 
2. Click the "GitHub Pages" link in the left-hand menu
3. Click the dropdown menu that asks you to select a branch.
4. Select the "master" branch
5. Click "Save"

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss9.png" />

This will generate a link to your GitHub site. 

<img class="large" src="/fall2023/assets/images/activities/github-activity/ss10.png" />

> ### A note on GitHub Pages
> * It make take a few minutes for your webpage to display
> * In order to preview the webpage you made in `tutorial02`, you have to append the `/tutorials/tutorial02/index.html` file path to the end of your github pages to indicate which file to display.
> * Example: 
>    * Sarah's homepage is here: <a href="https://vanwars.github.io/csci185-coursework/" target="_blank">https://vanwars.github.io/csci185-coursework/</a>. You will replace "vanwars" with your GitHub username.
>    * Sarah's Tutorial 2 is here: <a href="https://vanwars.github.io/csci185-coursework/tutorials/tutorial02" target="_blank">https://vanwars.github.io/csci185-coursework/tutorials/tutorial02</a>. Note the `/tutorials/tutorial02/index.html`.