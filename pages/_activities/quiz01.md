---
layout: two-column
title: Quiz 1
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
</style>

<a href="/fall2023/course-files/quizzes/quiz01.zip" class="nu-button">Quiz 1 Starter Files <i class="fas fa-download"></i></a> <a href="/fall2023/course-files/quizzes/quiz01_answers.zip" class="button">Quiz 1 Solutions <i class="fas fa-download"></i></a>

## Set Up
* Inside your `csci185` folder, create a folder called `quizzes`. 
* Download the starter files and unzip them. They should be unzipped in a folder called `quiz01`.
* Move your `quiz01` folder into  the `quizzes` folder.
* Open your entire `csci185` folder in VS Code.

Your directory structure should look something like this (it's OK if your file structure looks different, so long as the quizzes folder looks like the one below):

```bash
csci185
├── homework
├── index.html
├── lectures
├── quizzes
│   └── quiz01
├── styles.css
└── tutorials
```

When you're done with that, complete the Parts 1-4 as described below:

1. (30pts) [HTML Tasks (index.html)](#part1)
1. (30pts) [Styling tasks](#part2)
1. (30pts) [HTML Tasks (other files)](#part3)
1. (10pts) [Link from your homepage](#part4)
{:.compact}

> ### Guidelines
> * You may not move or rename any of the files.
> * Read the instructions that are outlined under each section very carefully. 
> * Complete as many tasks as you can by the end of the quiz. 
> * If it doesn't look exactly like the screenshot, don't stress -- partial credit is given!
> * Just do your best.
> {:.compact}


{:#part1}
## Part 1. HTML Tasks (index.html) [30pts]
For this section, you will be editing the `index.html` file in order to create the following structure inside of your `body` tag:

<img class="preview" src="/fall2023/assets/images/quizzes/quiz01/schematic.png" />

### 1. Stylesheet Link
1. Inside of the `head` tag in your `index.html` file, add a link to the `styles.css` stylesheet (located in the `assets` > `css` folder).
    * If you did it correctly, the background of your web page should turn dark blue.

### 2. Semantic Structure
1. Add three empty semantic tags inside the body tag:
    * a `header` tag
    * a `main` tag
    * a `footer` tag

### 3. Header & Navigation Sections
1. Inside the `header` tag, add an `img` tag that links to the `taco-temple-logo.webp` file (in the `images` folder).
1. Next to the `img` tag (but still inside the `header` tag), add a `nav` tag.
1. Inside the `nav` tag, add 3 hyperlinks:
    * One called **Menu** that links to `menu.html`
    * One called **Contact** that links to `contact.html` 
    * One called **Hours & Location** that links to `location-hours.html` 

Note that `menu.html`, `contact.html` , and `location-hours.html` are all located inside of the `site-pages` folder.

<img class="preview" src="/fall2023/assets/images/quizzes/quiz01/ss01.png" />

### 4. Main Section
1. Give the `main` tag a class called `"landing"`.
1. Inside the `main` tag, add two tags:
1. An `img` tag that links to the `landing-image.webp` file (in the images folder).
2. A `section` tag. Inside the section tag, add two tags:
    * An `h1` that says: "Call 828-255-8098<br> for take-out or click below to order online!"
    * A hyperlink that links to the Taco Temple order online page here: <a href="https://www.mamacitastacotemple.com/s/order" target="_blank">https://www.mamacitastacotemple.com/s/order</a>. The link text should say "Order now".

<img class="preview" src="/fall2023/assets/images/quizzes/quiz01/ss02.png" />

### 5. Footer
Within the `footer` tag, create a paragraph tag that says “Copyright 2023, Taco Temple.”

<img class="preview" src="/fall2023/assets/images/quizzes/quiz01/ss03.png" />


{:#part2}
## Part 2: Styling tasks [30pts]

### 1. Style the header 
Create a ruleset for **`header` elements** that applies the following styles:

```css
padding: 25px 13vw;
display: flex;
align-items: center;
justify-content: space-between;
```

### 2. Style the image inside the header element
Create a ruleset for **`img` elements <u>inside of</u> a `header` element** that sets the `width` property to `180px` 

### 3. Style the hyperlinks inside the nav element
Create a ruleset for **`a` elements <u>inside of</u> a `nav` element** that applies the following styles:

```css
color: white;
text-decoration: none;
margin: 10px;
text-transform: uppercase;
```

### 4. Style the main element
Create a ruleset for **`main` elements** that applies the following styles:

```css
padding: 100px 25vw 50px 25vw;
min-height: 55vh;
```

### 5. Style the "landing" class
Create a ruleset for the **`landing` class** that applies the following styles:

```css
background: white;
padding: 50px 15vw 100px 15vw;
display: grid;
grid-template-columns: 60% 40%;
align-items: center;
justify-content: center;
```

### 6. Style the image inside of the "landing" class
Create a ruleset for **`img` elements <u>inside of</u> a `landing` class element** that sets the `width` property to `100%`.

### 7. Style the "h1" and "h2" elements
Apply the following style rules to **all `h1` and `h2`** elements:
```css
font-family: Malamondo;
font-weight: 400;
text-transform: uppercase;
text-align: center;
``` 

This should give your `h1` and `h2` tags tag a funky custom font (which you'll notice as you complete Part 3).

### 8. Style the "h1" element inside of the "landing" class
Apply the following style rules to **`h1` elements <u>inside of</u> a `landing` class element**:

```css
color: black;
line-height: 1.2em;
font-size: 1.7em;
font-family: Malamondo-Alt;
```

This should give your `h1` tag on the landing page a slightly different custom font.

### 9. Style the link inside of the "landing" class to look like a button
Apply the following style rules to **`a` elements <u>inside of</u> a `landing` class element**:

```css
 text-align: center;
background-color: #013672;
color: white;
border: solid 2px white;
padding: 10px 20px;
font-weight: 300;
margin: auto;
display: block;
width: 100px;
border-radius: 4px;
text-decoration: none;
```

### 10. Style the footer element
Create a ruleset for **`footer` elements** to:

1. Give the footer `50px` of padding
2. center the text inside of the footer
{:.compact}


### 11. Add rulesets to style the other pages
Below the styles you just created, add the following rulesets
to style the other pages:

```css
ul {
    margin-bottom: 50px;
}

h2 {
    text-align: left;
}

.location-hours {
    margin-top: 50px;
}

.location-hours p {
    margin: 0;
}

form {
    margin: 0 auto;
    width: 600px;
    padding: 20px;
    border-radius: 4px;
}


form label {
    display: inline-block;
    width: 75px;
    padding: 10px 0px 5px 0;
    margin-top: 10px;
}

form input, form textarea {
    width: 550px;
    padding: 10px;
    border-radius: 4px;
    background: #FFF;
    border: solid 1px #CCC;
    padding-bottom: 20px;
    font-size: 1.2em;
    margin-bottom: 10px;
}

form button {
    border: solid 2px #fff;
    padding: 10px 20px;
    text-transform: none;
    background: #013672;
    color: white;
    font-family: 'Work Sans', sans-serif;
    font-weight: 300;
    font-size: 1.1em;
}
```


### Verify that you're done with the styling
When you're done, the homepage should look like this:

<img class="large frame" src="/fall2023/assets/images/quizzes/quiz01/ss04.png" />


{:#part3}
## Part 3. HTML Tasks (other files)  [30pts]
Please complete the following tasks for each of the three HTML files:
1. `menu.html`
2. `contact.html`
3. `location-hours.html`

### 1. Stylesheet Link
1. Add a `link` tag inside the `head` tag of each of the three HTML pages that links to `styles.css` (located in the `assets` folder). 
    * Note that the relative path will be different from what it was in `index.html`

### 2. Header Section
1. Copy the entire `header` tag (and everything inside of it) from `index.html` and paste it into each of the HTML pages **above** the `main` tag, but still within the `body` tag.
2. Adjust the file paths for the relative links so that the relative paths don't break (now that you're editing a file in the `site-pages` folder).
3. **[Optional -- 2pts Extra Credit]** Make the Taco Temple logo into a link by wrapping a hyperlink (`a` tag) around the `img` tag. This link should point to `index.html` in the parent directory.

When you're done, `menu.html`, `contact.html`, and `location-hours.html` should all link to one another.

### 3. Footer Section
1. Copy the entire `footer` tag  (and everything inside of it) from `index.html` and paste it **below** the `main` tag.


{:#part4}
## Part 4: Link from your homepage  [10pts]
When you're done with the exercise:
1. Update your homepage (that you made during Tutorial 3) by adding a link to the `index.html` file that you made in this quiz (and make sure you are using a relative link). Sarah's quiz looks like this:
* <a href="https://vanwars.github.io/csci185-coursework/" target="_blank">https://vanwars.github.io/csci185-coursework/</a>
2. Commit and sync your changes to GitHub.

## Submit

### 1. Verify that you're done with the quiz
When you're done with Parts 1-4, double-check that you're done:

#### A. HTML structure
All 4 of the HTML pages you just edited should have the  semantic structure (pictured below)
<img class="preview" src="/fall2023/assets/images/quizzes/quiz01/ss05.png" />

#### B. Links all work
Every page should link to every other page (no broken links).
* Note that linking from the detail pages to the index.html page is optional.

#### C. The website should look like this animation
<img class="preview" src="/fall2023/assets/images/quizzes/quiz01/tt-final.gif" />

#### D. Your homepage should link to the quiz.

### 2. Submit to the Moodle
**Please Read Carefully:** To submit Quiz 1, paste the following links into the Moodle under the Quiz 1 submission section:

1. A link to your **homepage** on GitHub pages.
2. A link to your GitHub **code repository** (where your code files are stored).

If your GitHub is not working for whatever reason, just zip your **COMPLETED** `quiz01` folder and upload it to the Moodle.