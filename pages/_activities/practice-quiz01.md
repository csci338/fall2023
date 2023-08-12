---
layout: two-column
title: Practice for Quiz 1
type: tutorial
draft: 1
points: 6
num: 4
due_date: 2023-02-03
---

<style>
    img {
        max-width: 70%;
    }
</style>

To study for Quiz 1, please complete the practice quiz by downloading the starter files and following the instructions (below). If you have questions, please ask during class time or in office hours. 

<a href="/fall2023/course-files/activities/practice-quiz01.zip" class="nu-button">Download Starter Files <i class="fas fa-download"></i></a>

## Part 1: Setup
You are going to build the webpage pictured below:

<img src="/fall2023/assets/images/quizzes/practice_quiz01/exercise01.png" />

Inside of the `practice-quiz01` folder, create a brand new HTML file called `index.html` that is a ***direct child*** of the `practice-quiz01` folder. If you did it correctly, your file structure should look like this:

```shell
practice-quix01
├── images
│   ├── landscape1_300x200.jpg
│   ├── landscape2_300x200.jpg
│   └── landscape3_300x200.jpg
├── index.html
└── pages
    ├── about.html
    └── gallery.html
```

Edit `index.html` file by adding an HTML “skeleton” with the following tags:

```html
<!DOCTYPE html>
<html lang="en">
   <head>
   </head>
   <body>
   </body>
</html>
```

## Part 2: HTML Tasks
Edit the `index.html` pages as follows:

### 2.1. Metadata
1. Add a `title` tag inside of the `head` tag, with the display text of "Practice Quiz 1: Your Name."

### 2.2. Header Section
1. Add a `header` tag inside the `body` tag (don’t get the head and the header tag confused). 
1. Inside the `header` tag, create an `h1` tag that displays the text "Practice Quiz 1: Your Name."

### 2.3. Navigation
1. Below the `header` tag, create a navigation section using the `nav` tag. 
1. Inside of the `nav` tag, create three hyperlinks:
    * One that links to `gallery.html` (in the pages folder) with the display text of “Photo Gallery”. Use a **relative path**.
    * One that links to `about.html` with the display text of “About Us”. Also use a **relative path**.
    * One that links to Instagram's home page, the display text of “Instagram”. Use an **absolute path**.

**Note:** you may not move the gallery.html or about.html files outside of the `pages` folder. 

### 2.4. Main Section
1. Below the `nav` tag, create a `main` tag. 
1. Inside the `main` tag, create a section that has an id of “images”.
1. Inside of the section you just made, create 3 `img` tags that display the three images in the `images` folder, using **relative paths**. 
    * Don’t forget to use the `alt` attribute to give each image a description (for people who use a screen reader).

### 2.5. Footer
Create a footer section below your `main` section using the `footer` tag. Within the footer, create a paragraph tag that says “Copyright Your Name, 2023.”


## Part 3: Styling tasks
Create a CSS file called `styles.css` that is a ***direct child*** of the `practice-quiz01` folder. If you did it correctly, your file structure should look like this:

```shell
practice-quix01
├── images
│   ├── landscape1_300x200.jpg
│   ├── landscape2_300x200.jpg
│   └── landscape3_300x200.jpg
├── index.html
├── pages
│   ├── about.html
│   └── gallery.html
└── styles.css
```

Edit your `index.html` file by adding a link to your stylesheet. Then, complete the following tasks within `styles.css`:

1. Create a rule for the `body` element that sets the background color to a light gray (`#F0F4EF`).
1. Create some style rules for the `header` element (and any relevant child elements) to:
    * Set the background color to `#b4cded`
    * Center the text horizontally and vertically.
    * Set the font family to `Impact`.
1. Create some style rules for the `nav` element (and any relevant child elements) to:
    * Center-align the hyperlinks
    * Turn the background color to black
    * Set the link color to white, no underline, and bold ([hint](https://www.w3schools.com/css/css_link.asp)).
1. Create some style rules to ensure that the three images are all in a row, evenly spaced, and with the same width. You may use any technique you want to do this, so long as you’re using CSS. See the screenshot above.
1. Create some style rules to set the footer’s background color to `#344966`, and the footer’s text color to white.


## What to Submit (if this were a real quiz)
If this were the real quiz, you would commit and push your changes (like we've been doing in class). Then, you would paste two links into the Quiz 1 section;
1. A link to your code repository (e.g., [https://github.com/vanwars/csci185-coursework](https://github.com/vanwars/csci185-coursework))
2. A link to your homepage (e.g., [https://vanwars.github.io/csci185-coursework](https://vanwars.github.io/csci185-coursework))