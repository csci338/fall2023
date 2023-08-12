---
layout: two-column
title: "Quiz 2: Taco Temple Part II"
type: tutorial
draft: 1
points: 6
num: 4
due_date: 2023-02-10
---

<style>
    img.preview {
        max-width: 60%;
        min-width: 500px;
    }

    .verify {
        margin-top: 40px;
        display: grid;
        grid-template-columns: 3fr 2fr;
        column-gap: 30px;
    }
    .verify > section {
        border: solid 1px #CCC;
        border-radius: 4px;
        padding: 10px;
    }
    .verify img {
        width: 100%;
        margin-top: 20px;
    }
</style>

> ## Guidelines
> * Read the instructions that are outlined under each section very carefully. 
> * Complete as many tasks as you can by the end of the quiz. 
> * Make your pages look as close to the screenshots / demos as possible.
> * You may use your notes, any sample code, any prior work you've completed, and the Internet
> * You **may not** communicate with anyone during the quiz.
> * Partial credit given. Just do your best.
> {:.compact}


## Set-Up

<a href="/fall2023/course-files/quizzes/quiz02.zip" class="nu-button">Quiz 2 Starter Files <i class="fas fa-download"></i></a>  <a href="/fall2023/course-files/quizzes/quiz02_answers.zip" class="button">Quiz 2 Solutions <i class="fas fa-download"></i></a>

* Download the starter files and unzip them. They should be unzipped in a folder called `quiz02`.
* Move your `quiz02` folder into your `csci185/quizzes` folder.
* Open your entire `csci185` folder in VS Code.

Your directory structure should look something like this (it's OK if your file structure looks different, so long as the quizzes folder looks like the one below):

```bash
csci185
├── homework
├── index.html
├── lectures
├── quizzes
│   ├── quiz01
│   └── quiz02
├── styles.css
└── tutorials
```

When you're done with that, complete the Parts 1-7 as described below:

1. (20pts) [Header](#part1)
1. (15pts) [Google Fonts](#part2)
1. (25pts) [Main](#part3)
1. (10pts) [Accessibility](#part4)
1. (10pts) [Pseudo-classes &nbsp; transitions](#part5)
1. (15pts) [Responsive layout](#part6)
1. (5pts) [Link from your homepage](#part7)
{:.compact}

## Your Tasks

{:#part1}
### Part 1. Header [20pts]
Make the header section look like the picture below, following the guidelines provided:

* [10pts] Use **Flex**
* [5pts] Links should be white with no underline
* [5pts] Don't forget the spacing surrounding the image and navigation
{:.compact}

<img class="large" src="/fall2023/assets/images/quizzes/quiz02/header.png" />


{:#part2}
### Part 2. Google Fonts & Header Styling [15pts]

* [10pts] Use the "Passion One" Google font to style the `h1`, `h2`, and `h3` tags.
* [2.5pts] Center-align the `h1` tag (Our Menu)
* [2.5pts] Add some top margin to the `h1` and `h2` tags.
{:.compact}

When you're done, the fonts should look like the ones pictured in [Part 3](#part3).


{:#part3}
### Part 3. Main [25pts]
Within the `main` section of your HTML page, create layout shown below by following the guidelines:

* [12.5pts] The section with the class of "cards" should be a two-column grid (each column should be the same width).
    * Hint: you'll only need to specify the columns, **not** the rows, as the cards will be positioned into the next available grid cell by default.
    * Note the spacing between columns and rows
* [12.5pts] Each section with a class of "card" should also be a two-column grid (the second column should be narrower than the first).
    * Make sure you add a border around each card
    * Make sure you apply some padding within each card
{:.compact}

<a style="text-decoration: none; border: none;" href="/fall2023/assets/images/quizzes/quiz02/main.png" target="_blank"><img class="frame large" src="/fall2023/assets/images/quizzes/quiz02/main.png" /></a>


{:#part4}
### Part 4. Accessibility [10pts]
Use the WAVE browser extension to fix any accessibility errors. When you're done, you should have no accessibility errors.
* You **do NOT** have to submit a screenshot of your accessibility report.
* You **do** have to correct all the errors.

<img class="medium" src="/fall2023/assets/images/quizzes/quiz02/wave.png" />

{:#part5}
### Part 5: Pseudo-classes & Transitions [10pts]
Create a rule for all of the "card" sections so when you hover over them:

* [2.5pts] the text color turns white
* [2.5pts] the background color turns navy blue (`#013672`)
{:.compact}

[5pts] Ensure that the transition is smooth:

<img class="frame large" src="/fall2023/assets/images/quizzes/quiz02/transitions.gif" />


{:#part6}
### Part 6: Responsive Layout [15pts]
Create a media query that activates when the width of the screen is **800px or less**. Within the media query, implement the following rules:

* [10pts] Overide the section with the class of “cards” so that it's a one-column grid.
* [5pts] Target the `nav` element and set its display to "none" so that the navigation does not display in the tablet or mobile views.


{:#part7}
### Part 7: Add a link from your homepage [5pts]
1. Update your homepage by adding a link to the `index.html` file that you made in this quiz (and make sure you are using a relative link). Sarah's quiz looks like this:
* <a href="https://vanwars.github.io/csci185-coursework/" target="_blank">https://vanwars.github.io/csci185-coursework/</a>
2. Commit and sync your changes to GitHub.

## Submit to the Moodle

### Before you submit

Verify that you've completed **all 7 tasks** and that you're final Taco Temple menu page (mobile/tablet and desktop) looks as similar as possible to the animations (shown below):

<div class="verify">
    <section>
        <h4>Desktop Layout</h4>
        <img src="/fall2023/assets/images/quizzes/quiz02/desktop-ui.gif" alt="Animation of Desktop layout" />
    </section>
    <section>
        <h4>Tablet / Mobile</h4>
        <img src="/fall2023/assets/images/quizzes/quiz02/tablet-ui.gif" alt="Animation of Tablet / Mobile layout" />
    </section>
</div>

### Submit to the Moodle
**Please Read Carefully:** To submit Quiz 2, paste the following links into the Moodle under the Quiz 2 submission section:

1. A link to your **homepage** on GitHub pages.
2. A link to your GitHub **code repository** (where your code files are stored).

If your GitHub is not working for whatever reason, just zip your **COMPLETED** `quiz02` folder and upload it to the Moodle.